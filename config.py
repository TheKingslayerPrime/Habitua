import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///habitua.db"

    def init_app(self, app):
        app.config.from_object(self)
