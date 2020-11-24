#!/usr/bin/env python
from fastcgi import *
from fastcore.all import *

@fastcgi('/var/run/caddy/fcgi.sock')
def run():
    print(f'Content-type: text/plain\n')
    try: _,user,repo = os.environ['PATH_INFO'].split('/')
    except ValueError: return print('!!!Invalid path')
    try: rels=urljson(f'https://api.github.com/repos/{user}/{repo}/releases/latest')['assets']
    except: return print(f'!!!Could not access {user}/{repo}')
    print('\n'.join(L(rels).itemgot('browser_download_url')))
