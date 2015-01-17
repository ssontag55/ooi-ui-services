#!/usr/bin/env python
'''
ooiservices

Initializes the application and necessary application logic
'''
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #This line should be moved to a defaults.py in the future
    app.config['LOG_FILE'] = True
    #Adding logging capabilities.
    if app.config.get('LOG_FILE') == True:
        import logging
        logger = logging.getLogger('replicate')
        logger.setLevel(logging.DEBUG)

        # TODO: Add log_filename to YAML config, maybe set up a logging directory in the config as well
        log_directory = basedir + '/logs/'
        log_filename = log_directory + 'ooiservices.log'
        if not os.path.exists(os.path.dirname(log_filename)):
            os.makedirs(os.path.dirname(log_filename))
        file_handler = logging.FileHandler(log_filename, mode='a+')

        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(module)s:%(lineno)d - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)
        #app.logger.addHandler(stream_handler)
        app.logger.setLevel(logging.DEBUG)
        app.logger.info('Application Process Started')

    db.init_app(app)
    login_manager.init_app(app)

    from .main import api as main_blueprint
    app.register_blueprint(main_blueprint)

    return app