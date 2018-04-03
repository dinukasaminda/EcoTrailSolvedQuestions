from PIL import Image
im = Image.open("download.jpg")
pix = im.load()
wdith,height =im.size
print ("w",wdith,"h",height)

row = 0

for j in range(0,height):
    marks = 0
    for i in range(0,wdit h):
        value = pix[i,j]
        if(i<100):
            if (value[0]==0 and value[1]==0 and value[2]==0):
                marks +=1
        else :
            if marks > 90 :
                pix[i,row] = value 
    if marks > 90 :
        row +=1
im.save("alive_parrot.png") 