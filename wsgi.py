from bottle import get,run,Bottle,route

app = Bottle()

@app.get('/')
def welcome():
	return "Hello, welcome to knowurcoding!"

if __name__=="__main__":
	run(app, host='localhost', port=8088)

