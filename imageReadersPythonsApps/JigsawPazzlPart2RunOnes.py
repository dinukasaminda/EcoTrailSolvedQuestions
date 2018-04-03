
'''
dont change dits shufl array and anything 

'''

dictsShufl = [
    13,
  22,
  8,
  4,
  6,
  29,
  19,
  25,
  2,
  27,
  11,
  9,
  1,
  16,
  15,
  14,
  17,
  18,
  5,
  23,
  21,
  20,
  7,
  10,
  3,
  26,
  24,
  28,
  12,
  30,
  31,
  32
]



from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import math
import sys

'''
c at dinuka saminda bandra gunarthna
'''
images = []
imagesTest = []
imgW=1224
immgH=800
bw=153
bh=200
Parts =32

def VecDistance(v1,v2):
    res1 = math.pow(v1[0]-v2[0],2) + math.pow(v1[1]-v2[1],2)+ math.pow(v1[2]-v2[2],2)
    return res1

for c in range (1,Parts+1):
    im = Image.open("./realparts/part"+str(c)+".jpg") #Can be many different formats.
    images.append(im)

for c in range (1,Parts+1):
    im = Image.open("./parts/part"+str(c)+".jpg") #Can be many different formats.
    imagesTest.append(im)

sString1 = ""

background = Image.new('RGBA', (imgW, immgH), (255, 255, 255, 255))

ik=0
jk=0
for c in range (1,Parts+1):
    impix = images[dictsShufl[c-1]-1].load()
  
    
    marks = [] 
    
    for k in range (0,Parts):
        markcs = 0
        pix =imagesTest[k].load()
        for j in range(40,bh-1):
            for i in range(40,bw-1):
                if(VecDistance(impix[i,j],pix[i,j])<2 ):
                    markcs +=1
        marks.append({'key':k,'v1':markcs })
    marks.sort(key=lambda x: x['v1'], reverse=True) 
    sString1 += ","+str(marks[0]['key']+1)
    background.paste(imagesTest[marks[0]['key']],(ik,jk))
    if(ik<imgW-bw):
        ik+=bw
    else:
        ik=0
        jk+=bh
    
print(sString1)
background.save("HHH.png")