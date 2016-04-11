from app import myapp

@myapp.route('/')
@myapp.route('/index')
def index():
    return "Hello, World!"