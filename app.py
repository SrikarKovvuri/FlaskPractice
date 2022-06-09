from flask import Flask

app = Flask(__name__)

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

