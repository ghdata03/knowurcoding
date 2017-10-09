from bottle import run,Bottle

app = Bottle()

@get('/')
def welcome():
	return "Hello, welcome to knowurcoding!"



