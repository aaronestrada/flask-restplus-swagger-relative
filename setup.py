from distutils.core import setup

setup(
    name='flask-restplus-relative-swagger',
    version='0.0.1',
    description='Flask-RESTplus manual path assignment for Swagger assets, '
                'it changes the relative path for Swagger assets generated by Flask-RESTplus framework',
    license='BSD',
    author='Aaron Estrada Poggio',
    author_email='aaron.estrada.poggio@gmail.com',
    url='https://github.com/aaronestrada/flask-restplus-swagger-relative',
    packages=['flask_restplus_relative_swagger'],
    python_requires='>=3',
    install_requires=[
        'Flask==1.0.2',
        'flask-restplus==0.11.0'
    ]
)
