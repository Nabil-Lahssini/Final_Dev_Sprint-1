import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#this is the route to get the ip of the client (it can be used to block brute force attack or ddos)
@app.route("/test", methods=["GET"])
def test():
    return "correct"


app.run()