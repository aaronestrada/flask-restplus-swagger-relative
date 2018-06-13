# Flask RESTplus Swagger relative path
This extension allows to change the relative path for Swagger assets generated by Flask RESTplus. 

## Requirements
* Python 3
* Flask 1.0.2
* Flask-RESTplus 0.11.0

## Motivation
Sometimes API applications need different relative paths for Swagger assets, especially if there are many application services running on the same domain and orchestrated with NGINX.

## How to use the extension
Include the extension library and initialize the Flask application. Check for this example.

```python
from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus_swagger_relative import FlaskRestplusSwaggerRelative

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Change Swagger relative path on server
api_doc = FlaskRestplusSwaggerRelative()
api_doc.init_app(app=app, url='/this_is_a_new/path_for_swagger/')

if __name__ == '__main__':
    app.run(debug=True)
```

Using the previous example, the path for **swagger-ui-bundle.js** is: 

```
http://localhost:5000/this_is_a_new/path_for_swagger/swaggerui/swagger-ui-bundle.js

 instead of

http://localhost:5000/swaggerui/swagger-ui-bundle.js
``` 