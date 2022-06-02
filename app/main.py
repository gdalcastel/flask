from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "FLASK SERVER!"

app.run(host="0.0.0.0", port=5000)	