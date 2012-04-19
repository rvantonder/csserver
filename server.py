"""
The most basic (working) CherryPy application possible.
"""

import time
import cherrypy
import random
import ocrparser
import util

#time, so that its unique
#phone number, just cuz
#random shift cuz want things to be sufficiently mixed up

class Server:
    """ Sample request handler class. """

    def __init__(self):
      self.db = {}
      self.balances = {}
      self.img = "pics/new.jpg"
      self.result = ""

    def index(self, *args, **kwargs):
        #image line: <img src="%s">
        return  """
               <html>
		           <head><title>Test</title></head>
		           <body>
		           <div style="text-align: center;">
		           <img src="%s">
               <p>%s</p>
		           </div>
               </body></html>
               """  % (self.img, self.result)

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


        ocr_file = process_ocr(self.img) #critical method, must be allowed to run on multiple threads in future

        d = ocrparser.parse(ocr_file)

        print 'dict: '
        print d

        self.result = ""

        for k in d.keys():
          self.result += k+" "+str(d[k])+'<br />' #TODO this does not work for me!

        self.result += str(ocrparser.sum_prices(d))
        print 'Processing complete'

        return out % (size, myFile.filename, myFile.content_type)

    upload.exposed = True


def process_ocr(img_filename):
    
  tiffile = util.jpg_to_tif(img_filename,img_filename[:-4]+".tif",rotate=True)
  print 'tiffile: '+tiffile
  outfile = util.tif_to_ocr(tiffile,tiffile[:-4]+"out")
  print 'outfile: '+outfile
  
  return outfile
    

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

