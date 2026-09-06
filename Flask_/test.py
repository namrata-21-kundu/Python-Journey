from flask import Flask
app = Flask(__name__) #creates a Flask Application
@app.route('/') #connects the home URL (/) to a function
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True) #starts local server