# from flask import url_for
# from flask import Flask
# from markupsafe import escape

# app = Flask(__name__)

# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


# @app.route('/')
# def index():
#     return 'index'


# @app.route('/login')
# def login():
#     return 'login'


# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'
