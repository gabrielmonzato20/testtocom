import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7890767889990'
