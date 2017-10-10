from bottle import get,run,Bottle,route
import os,leancloud
from leancloud import Engine


PORT = int(os.environ['LEANCLOUD_APP_PORT'])
APP_ID = os.environ['LEANCLOUD_APP_ID']                
APP_KEY = os.environ['LEANCLOUD_APP_KEY']              
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']    

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

app = Bottle()

@app.get('/')
def welcome():
	return "Hello, welcome to knowurcoding!"

engine = Engine(app)

if __name__=="__main__":
	run(app, host='localhost', port=PORT)

