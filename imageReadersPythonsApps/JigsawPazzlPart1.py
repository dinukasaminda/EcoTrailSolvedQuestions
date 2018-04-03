from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

'''
c at dinuka saminda bandra gunarthna
'''
im = Image.open("download.jpg") #Can be many different formats.
pix = im.load()
wdith,height =im.size #Get the width and hight of the image for iterating over
print ("w",wdith,"h",height)
bw=153
bh=200
row = 0

c=1
for j in range(0,4):
    for i in range(0,8):
        cropped_example = im.crop((i*bw, j*bh, (i+1)*bw, ((j+1)*bh)))
        #draw = ImageDraw.Draw(cropped_example)
        #draw.text((10, 10),str(c),(255,255,255))
        path1 = "./parts/part"+str(c)+".jpg"
        print(path1)
        cropped_example.save(path1)
        c +=1