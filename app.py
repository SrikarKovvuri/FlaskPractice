from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI') = "sqlite///posts.db"
db = SQLAlchemy(app)

class BlogPost(db.model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.text, nullable = False)
    author = db.Column(db.String(20, nullable = False, default = "N/A"))
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return 'Blog Post' + str(self.id)

all_posts = [
        {
            "title": "Post1",
            "content": "This is one of content posts",
            "author": "Aaron"
        },
        {
            'title': "Post2",
            "content": "Content of post 2"
        }
    ]

@app.route('/home/data/')
def getData():
    return all_posts

@app.route('/')
def index():
    return "Home"

#introducing a parameter in the url - good for dynamic urls
@app.route('/home/users/<string:name>/posts/<int:id>') 
def hello(name, id):
    return "Hello, " + name + ". You are " + str(id) + "years old"

@app.route('/onlyget', methods = ['GET', 'POST'])
def getReq():
    return "Only this"

if __name__ == "__main__":
    app.run(debug=True)

