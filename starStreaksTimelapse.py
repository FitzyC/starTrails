import os, numpy
from PIL import Image

inFiles = ""
outfiles = ""

for dirpath, dirnames, filenames in os.walk(inFiles):
    images = filenames

os.chdir(inFiles) 

width, height = Image.open(images[0]).size
stack = numpy.zeros((height, width, 3), numpy.float)

for imageMain in images:  
    print("Processing img " + imageMain)
    stacker = numpy.array(Image.open(imageMain), dtype = numpy.float)
    stack = numpy.maximum(stack, stacker)        
    
    print("Finishing image...")
    stack = numpy.array(numpy.round(stack), dtype = numpy.uint8)
    
    output = Image.fromarray(stack, "RGB")
    
    output.save(os.path.join(outfiles, os.path.splitext(imageMain)[0] + 's.jpg'), "JPEG")
    print("")
