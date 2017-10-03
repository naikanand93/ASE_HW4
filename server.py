from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("input_form.html")


@app.route("/save", methods=['GET', 'POST'])
def saveData():
	data = request.get_data()
	print(data)
	#save data to db
	return "Hello World!"
	#return data & id generated in db.


