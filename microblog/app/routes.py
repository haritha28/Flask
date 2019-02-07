from flask import render_template
from app import app

# route() is used to bind a URL to a function.
#@app.route are decorators. We can use decorators to register them to function callbacks to a certain event
@app.route('/')
@app.route('/index')

#Initially the view function returned a string
#Now we expand it to return a complete HTML page

#The function render template is used to import a function that comes with the Flask framework.
#Fucntion has template name and the lsit of arguments used by the HTML page.

def index():
    user = {'username' : 'Haritha'}
    #list is used to represent the post field, where each element is a dictionary.
    posts = [
        {
            'author': {'username': 'John'},
            'body' : ' Beautiful day in Portland!'
        },
        {
            'author' : {'username': 'Susan'},
            'body': ' The Avengers movie was cool!'

        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


#<html>
#    <head>
#        <title> Home Page - Microblog </title>
#    </head>
#    <body>
#        <h1>Hello, ''' + user['username'] + '''!</h1>
#   </body>
#</html>

##Adding the HTML file in the return would give us a complex code and hence we seperate the layout and logic of the
#application seperately. For this we use templates
