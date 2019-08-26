from views import index
# from views import poll
def setup_routes(app):
	app.router.add_get('/',index)
	# app.router.add_get('/poll',poll)
