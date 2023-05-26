from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/tables')
def table():
    return render_template('tables.html')

@app.route('/billing')
def billing():
    return render_template('billing.html')

@app.route('/virtual-reality')
def virtual():
    return render_template('virtual-reality.html')

@app.route('/rtl')
def rtl():
    return render_template('rtl.html')

@app.route('/notifications')
def notification():
    return render_template('notifications.html')

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")