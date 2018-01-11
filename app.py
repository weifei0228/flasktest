from flaskr.factory import create_app
#from flaskr.blueprints.flaskr import init_db

app=create_app()
#init_db()
with app.app_context():
	
	if __name__=="__main__":
		app.run(host='0.0.0.0', port=8080)
	
		#app.run()
	