def configure_routes(app):
    @app.route('/')
    def home():
        return {'message': 'Late Show API is running'}
