from flask import url_for
from flask_restx import Api


class FlaskRestplusRelativeSwaggerApi(Api):
    """
    Flask-Restplus Api children class with capability of overriding "specs_url" property in order to:

    - Allow changing swagger.json without specifying scheme (http or https). Useful whenever the application
      is behind a proxy server (e.g. NGINX) and there is no possibility to set the X-FORWARDED-PROTO parameter.

    - Allow changing URL for an outside swagger.json file (containing documentation)
    """
    specs_url_f = None
    swagger_path = None
    external_specs = True

    def set_external_swagger_specs(self, external: bool):
        """
        Set external swagger specification as external or internal (no scheme)

        :param external: Whether swagger.json specification on documentation generation is accessible as external or not
        :return:
        """
        self.external_specs = external

    def set_swagger_external_url(self, url):
        """
        Set swagger.json file URL

        :param url: URL to set for Swagger documentation
        :return:
        """
        self.swagger_path = url

    def set_specs_url(self, f):
        """
        Decorator class to override specs_url property

        :param f: Function/method to set as overriding method
        :return:
        """
        self.specs_url_f = f

    @property
    def specs_url(self):
        """
        Specs_url property for Swagger documentation

        :return:
        """
        # Check if there is no method substituting specs_url property
        if self.specs_url_f is not None:
            url = self.specs_url_f(self)
        elif self.swagger_path is None:
            # Use internal/external specs
            url = url_for(self.endpoint('specs'), _external=self.external_specs)
        else:
            url = self.swagger_path

        return url
