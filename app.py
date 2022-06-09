from flask import Flask

app = Flask(__name__)

#introducing a parameter in the url - good for dynamic urlsm
@app.route('/home/users/<string:name>/<int:id>') 
def hello(name, id):
    return "Hello, " + name + ". You are " + str(id) + "years old"

if __name__ == "__main__":
    app.run(debug=True)

