import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/test", methods=["GET"])
def test():
    return "correct"


app.run()