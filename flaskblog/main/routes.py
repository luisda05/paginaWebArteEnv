from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")

@main.route("/inicio")
def inicio():
    return render_template('inicio.html', title='inicio')


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/productos")
def productos():
    return render_template('productos.html', title='Productos')

@main.route("/album")
def album():
    return render_template('album.html', title='album')

