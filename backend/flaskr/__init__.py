import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # creates the Flask instance  
    app = Flask(__name__, instance_relative_config=True)
    # name -> current py module name
    # instance_relative_config=True -> congi files are relative to the instance folder
    app.config.from_mapping(
        SECRET_KEY='dev', # when deploying: override it with a random val
        DATABASE=os.path.join(app.instance_path, 'members.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # when deploying, this can be used to set a real SECRET_KEY.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app