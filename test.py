from flask import Flask  
app = Flask(__name__)   
@app.route('/')         
def hello_world():
    return 'Hello World!'
    

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:num>/<name>')
def repeat( name,num):
    return f"{ num * name}"


if __name__=="__main__":      
    app.run(debug=True) 