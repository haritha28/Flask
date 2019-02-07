#This file maintains the configuration of the application which are defined
#as class variables inside the Config class
import os


class Config(Object):
    #Secret key is used to protect against the Cross-site Request Forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #The value of secret key is either the value of the env variable SECRET_KEY
    # or the 'you-will-never-guess'

