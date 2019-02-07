from app import app

# route() is used to bind a URL to a function.
#@app.route are decorators. We can use decorators to register them to function callbacks to a certain event
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
