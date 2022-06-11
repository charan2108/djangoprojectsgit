from bottle import Bottle,route,run,template

app = Bottle()

@route('/')
@app.route('/hello/<name>')

def Hello(name='Programmer'):
    return template('Hello , {{name}}, how r u', name=name)
run(app, host='localhost', port=8080,  debug=True)
   