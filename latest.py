#!/usr/bin/env python
from fastcgi import *
from fastcore.all import *

@fastcgi('/var/run/caddy/fcgi.sock')
def run():
    print(f'Content-type: text/plain\n')
    try: _,pre,user,repo,*search = os.environ['PATH_INFO'].split('/')
    except ValueError: return print('!!!Invalid path')
    if pre not in ('pre', 'latest'): return print('!!!first component should be "pre" or "latest"')
    gh = f'https://api.github.com/repos/{user}/{repo}/releases'
    if pre=='latest': gh += '/latest'
    try: rels=urljson(gh)
    except Exception as e: return print(f'!!!Could not access {gh}; {e}')
    if pre=='pre': rels = rels[0]
    urls = L(rels['assets']).itemgot('browser_download_url')
    if search: urls = [o for o in urls if search[0] in o]
    print('\n'.join(urls))
