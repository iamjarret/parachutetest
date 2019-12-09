from connect import tests,runs

from flask import Flask


app = Flask(__name__)

@app.route("/")
def home_page():
	experiments = tests.find({})
	return render_template("index.html",experiments=experiments)


@app.route("/test/<name>")
def focus(name):
	test = tests.find({'testname':name})
	exp = runs.find({'testname':name})
	return render_template("details.html",test=test, exp=exp)


if __name__ == '__main__':
    app.run()
