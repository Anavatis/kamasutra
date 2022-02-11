import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):
    Debug = True


class ProductionConfig(BaseConfig):
    Debug = False
