from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/python')
def python():
    html = """
    <html>
        <h1>Python Programming Language</h1>
    </html>
    """
    return html
