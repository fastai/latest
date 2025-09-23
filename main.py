#!/usr/bin/env python
from fasthtml.common import *
from latest.core import *

app = FastHTML()
rt = app.route

@rt('/{path:path}')
def index(path:str): return find_releases(path)

serve()

