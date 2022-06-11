from bottle import Bottle,route,run

app = Bottle()

@route('/')
@app.route('/hello')

def Hello():
    return 'Hello World'
run(app, host='localhost', port=8080,  debug=True)
   