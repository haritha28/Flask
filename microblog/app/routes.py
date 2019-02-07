from app import app

# route() is used to bind a URL to a function.
#@app.route are decorators. We can use decorators to register them to function callbacks to a certain event
@app.route('/')
@app.route('/index')

#Initially the view function returned a string
#Now we expand it to return a complete HTML page

def index():
    user = {'username' : 'Haritha'}
    return '''
<html>
    <head>
        <title> Home Page - Microblog </title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

