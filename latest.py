#!/usr/bin/env python
import re
from fasthtml.common import *
from fastcore.all import *

app = FastHTML()
rt = app.route

@rt('/{path:path}')
def index(path:str):
    try: pre,user,repo,*search = path.split('/')
    except ValueError: return '!!!Invalid path'
    if pre not in ('pre', 'latest'): return '!!!first component should be "pre" or "latest"'
    gh = f'https://api.github.com/repos/{user}/{repo}/releases'
    if pre=='latest': gh += '/latest'
    try: rels=urljson(gh)
    except Exception as e: return f'!!!Could not access {gh}; {e}'
    if pre=='pre': rels = rels[0]
    urls = L(rels['assets']).itemgot('browser_download_url')
    if search: urls = [o for o in urls if re.search(search[0], o)]
    return '\n'.join(urls)

serve()

