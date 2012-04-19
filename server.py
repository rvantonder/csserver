"""
The most basic (working) CherryPy application possible.
"""

import time
import cherrypy
import random

#time, so that its unique
#phone number, just cuz
#random shift cuz want things to be sufficiently mixed up

class Server:
    """ Sample request handler class. """

    def __init__(self):
      self.db = {}
      self.balances = {}
      self.img = "pics/new.jpg"

    def index(self, *args, **kwargs):
        return  """
               <html>
		           <head><title>Test</title></head>
		           <body>
		           <div style="text-align: center;">
		           <img src="%s">
		           </div>
               </body></html>
               """ % (self.img)

    index.exposed = True 

    def upload(self, myFile, imname=None):
        out = """
              <html>
              <body>
              myFile length: %s<br />
              myFile filename: %s<br />
              myFile mime-type: %s
              </body>
              </html>
              """ #TODO get rid of this

        self.img = "pics/"+str(int(time.time()))+".jpg"
        f = open(self.img, "w") 

        size = 0
        while True:
            data = myFile.file.read(8192)
            f.write(data)
            if not data:
                break
            size += len(data)

        return out % (size, myFile.filename, myFile.content_type)
    upload.exposed = True

import os.path
appconf = os.path.join(os.path.dirname(__file__), 'app.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    

    cherrypy.quickstart(Server(), config=appconf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(Server(), config=appconf)

