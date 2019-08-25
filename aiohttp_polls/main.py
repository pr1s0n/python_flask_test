from aiohttp import web
from routes import setup_routes
from settings import config,BASE_DIR
from db import close_pg,init_pg
import aiohttp_jinja2
import jinja2

app = web.Application()

app['config'] = config
aiohttp_jinja2.setup(app,loader = jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttp_polls' / 'templates')))
setup_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

web.run_app(app)
