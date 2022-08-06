import flask
import socket

app=flask.Flask(__name__)
app.config["DEBUG"]=True


@app.route('/display',methods=['GET'])
def display_fun():
    return f"This is a simple load balanced application, served by instance: {socket.gethostname()}"


#app.run(host="0.0.0.0")
