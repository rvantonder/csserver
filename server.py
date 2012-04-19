"""
The most basic (working) CherryPy application possible.
"""

import time
# Import CherryPy global namespace
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

    def index(self, *args, **kwargs):
        print "?1",args
        print "?2?",kwargs

#        return """
#        <html><body>
#            <h2>Upload a file</h2>
#            <form action="upload" method="post" enctype="multipart/form-data">
#            filename: <input type=file name=myFile /><br />
#            <input type=submit name=press value="OK"/>
#            </form>
#            <h2>Download a file</h2>
#            <a href='download'>This one</a>
#        </body></html>
#        """
#
        return """
        <html>
		<head><title>Test</title></head>
		<body>
		<div style="text-align: center;">
		<img src="pics/new.jpg">
		</div>
        </body></html>
        """


    # Expose the index method through the web. CherryPy will never
    # publish methods that don't have the exposed attribute set to True.
    index.exposed = True 

    def upload(self, myFile, imname=None):
        print "HELLO"

        out = """<html>
        <body>
            myFile length: %s<br />
            myFile filename: %s<br />
            myFile mime-type: %s
        </body>
        </html>"""

        # Although this just counts the file length, it demonstrates
        # how to read large files in chunks instead of all at once.
        # CherryPy reads the uploaded file into a temporary file;
        # myFile.file.read reads from that.

        f = open("pics/new.jpg", "w") #imname

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

