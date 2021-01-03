from sympy import *

x = Symbol('x')

diff(x**2, x)
diff(log(x**2), x)


import flask

app = flask.Flask('web')

@app.route('/diff')
def res():
    res = diff(eval(flask.request.args['eq']), x)
    return 'The answer is: <b>%s</b>' % str(res)


@app.route('/')
def home():
    return '''
<h1>Welcome</h1>
<form action="/diff">
<input name="eq">
<input type="submit">
</form>
'''

app.run(debug=True)
