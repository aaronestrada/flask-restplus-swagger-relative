import os
from flask import url_for
from flask_restplus import apidoc


def create_custom_apidoc(url=None):
    """
    Create API document object for SwaggerUI generator
    :param url: URL to store static files for documentation
    :return: APIdoc object
    """
    if url is None:
        url = '/'

    relative_name = 'restplus_relative_doc{0}'.format(url)
    custom_apidoc = apidoc.Apidoc(relative_name, __name__,
                                  template_folder='templates',
                                  static_folder=os.path.dirname(apidoc.__file__) + '/static',
                                  static_url_path='/swaggerui')

    @custom_apidoc.add_app_template_global
    def swagger_static(filename):
        """
        Change Swagger static file path
        :param filename: Filename from Swagger
        :return:
        """
        return url_for('{0}.static'.format(relative_name), filename=filename)

    return custom_apidoc


class FlaskRestplusRelativeSwagger:
    """
    Relative path for Flask-restplus documentation with SwaggerUI.
    """

    def __init__(self, app=None, url=None):
        """
        Class constructor
        :param url: Name of new documentation blueprint
        """
        self.url = url

        if app is not None:
            self.app = app
            self.init_app(app=app, url=url)

    def init_app(self, app=None, url=None):
        """
        Initialize application
        :return:
        """
        if app is None:
            app = self.app

        if url is None:
            url = self.url

        if app is not None:
            # Register new blueprint with custom API documentation pointing to relative path
            app.register_blueprint(
                create_custom_apidoc(url=url),
                url_prefix=url
            )
