import subprocess

def jpg_to_tif(jpgin, tifout, rotate=False):
  """
  In: filename or path to jpg, and tif output name
  Out: tif image in specified path
  """
  if rotate: # It may be necessary to rotate the image for OCR
    subprocess.call(["convert", jpgin, tifout])
    subprocess.call(["convert", "-rotate", "90", tifout, tifout])
  else:
    subprocess.call(["convert", jpgin, tifout])

def tif_to_ocr(tif, outfile):
  """
  In: tif image and output file name
  Out: tesseract ocr output
  Returns: name of output file
  """
  subprocess.call(["tesseract", tif, outfile])
  return outfile+".txt"
