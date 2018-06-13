from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus_relative_swagger import FlaskRestplusRelativeSwagger

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# New relative assignment
api_doc = FlaskRestplusRelativeSwagger()
api_doc.init_app(app=app, url='/this_is_a_new/path_for_swagger/')

if __name__ == '__main__':
    app.run(debug=True)
