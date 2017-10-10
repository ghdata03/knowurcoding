import os,leancloud

from cloud import engine

APP_ID = os.environ['LEANCLOUD_APP_ID']                
APP_KEY = os.environ['LEANCLOUD_APP_KEY']              
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']    
PORT = int(os.environ['LEANCLOUD_APP_PORT'])

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

application = engine


