from flask import Flask, url_for
from flask_restplus import Resource, Api
from flask_restplus_relative_swagger import FlaskRestplusRelativeSwagger, FlaskRestplusRelativeSwaggerApi

app = Flask(__name__)

# -----------------------------------------------------------
# Api definition and Swagger definition on documentation page
# -----------------------------------------------------------
api = FlaskRestplusRelativeSwaggerApi(app=app)


# ---------------------------------------------------------------
# Only one option is needed. Comment the options you do not need.
# ---------------------------------------------------------------
# Option 1: overriding specs_url property for Api object
@api.set_specs_url
def overwrite_api_specs_url(self: Api):
    return url_for(self.endpoint('specs'), _external=True, _scheme='https')


# Option 2: set Swagger specs in documentation generation with no scheme
api.set_external_swagger_specs(external=False)

# Option 3: set an external URL for swagger to use as documentation
api.set_swagger_external_url(url='http://myotherdomain.com/swagger.json')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# ---------------------------------------------------------
# New relative assignment (for internal documentation only)
# ---------------------------------------------------------
api_doc = FlaskRestplusRelativeSwagger()
api_doc.init_app(app=app, url='/this_is_a_new/path_for_swagger_internal_documentation/')

if __name__ == '__main__':
    app.run(debug=True)
