from app.blog import views


def setup_routes(app):
    app.router.add_get("/", views.index)
