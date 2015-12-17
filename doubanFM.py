from client import Client

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

client = Client()
client.start()