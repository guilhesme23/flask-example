from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(hello='world')


@app.route('/devel')
def the_devel():
    return """
        <h1>Hey you're in the dev env</h1>
    """


@app.route('/<name>')
def hello_name(name):
    return jsonify(hello=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
