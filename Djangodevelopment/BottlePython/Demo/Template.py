from bottle import run,route,template

@route('/')
def hello():
    return template("Hello, {{name}}, welcome to bottle", name="User")
run(host="localhost", port="8080", debug=True)