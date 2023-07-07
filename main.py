from aiohttp import web


def setup_routes(application):
    from app.blog.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)


def setup_app(application):
    setup_routes(application)


def create_app():
    app = web.Application()
    setup_app(app)
    return app
