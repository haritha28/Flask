#creates the application  object as an instance of flask
from flask import Flask
#__name__ is a predefined variable which is set to the name of the module in which it is used
#the app variable is referenced as an instance of the flask in this file.

app = Flask(__name__)

#it imports the routes modules
#the app here refers to the app package
#The route module is imported at the last and not in the top.

from app import routes
