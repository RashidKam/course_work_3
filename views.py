from flask import render_template, Blueprint
from class_template import PostLine
from utils import *
file_posts = 'data/posts.json'
file_comments = 'data/comments.json'

# line_blueprint = Blueprint('line_blueprint', __name__, template_folder='./templates')
app = Flask(__name__)
# @line_blueprint.route('/')


@app.route('/')
def index_page():
    '''Летна постов'''
    all_posts = get_posts_all(file_posts)
    return render_template('index.html', all_posts=all_posts)


@app.route('/post/<pk>')
def post_page(pk):
    '''Страница поста'''
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments, len_comments=len(comments))


@app.route('/user-feed/<poster_name>')
def user_posts(poster_name):
    '''Все посты определенного пользователя'''
    user_posts = get_posts_by_user(poster_name)
    return render_template('user-feed.html', user_posts=user_posts)


@app.route('/search/', methods=['GET'])
def search_page():
    '''Поиск постов'''
    query = request.args.get('s')
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts)



app.run()
