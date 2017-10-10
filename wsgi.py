from bottle import get,run,Bottle,route
import os

PORT = int(os.environ['LEANCLOUD_APP_PORT'])

app = Bottle()

@app.get('/')
def welcome():
	return "Hello, welcome to knowurcoding!"

if __name__=="__main__":
	run(app, host='localhost', port=PORT)

