#!/usr/bin/env python
from fastcgi import *
from fastcore.all import *

@fastcgi('/var/run/caddy/fcgi.sock')
def run():
    print(f'Content-type: text/plain\n')
    try: _,user,repo,*search = os.environ['PATH_INFO'].split('/')
    except ValueError: return print('!!!Invalid path')
    gh = 'https://api.github.com/repos'
    try: rels=urljson(f'{gh}/{user}/{repo}/releases/latest')['assets']
    except: return print(f'!!!Could not access {user}/{repo}')
    urls = L(rels).itemgot('browser_download_url')
    if search: urls = [o for o in urls if search[0] in o]
    print('\n'.join(urls))
