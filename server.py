from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# connect to MongoDB server
app.config['MONGOMLAB_HOST'] = 'ds161584.mlab.com'
app.config['MONGOMLAB_PORT'] = 61584
app.config['MONGOMLAB_DBNAME'] = 'users_impromptu'
app.config['MONGOMLAB_USERNAME'] = 'abhishek'
app.config['MONGOMLAB_PASSWORD'] = '12345'

mongo_mlab = PyMongo(app, config_prefix='MONGOMLAB')

@app.route("/")
def hello():
    return render_template("input_form.html")

@app.route("/get", methods=['GET', 'POST'])
def getAllUsers():
	# Confirm how to get the list of users
	mongo_query = mongo_mlab.db.active_users.find()
	print(mongo_query)

	users_list = []

	for user in mongo_query:
		user_name = user['first_name'] + " " + user['last_name']
		user_likes =  user['likes']

		users_list.append([user_name,user_likes])

	return jsonify(users_list)


@app.route("/save", methods=['GET', 'POST'])
def saveData():
	data = request.get_data()

	list_response = data.split('&')

	first_name = list_response[0].split('=')[1]
	last_name = list_response[1].split('=')[1]
	likes = list_response[2].split('=')[1]

	print first_name, last_name, likes
	#print list_response[1], list_response[3], list_response[5]

	docid = mongo_mlab.db.active_users.insert({
			'first_name': first_name, 
			'last_name': last_name,
			'likes': likes
			})

	return "Saved with id: ", docid
	#return data & id generated in db.

def test_saveData():
	assert 1==1