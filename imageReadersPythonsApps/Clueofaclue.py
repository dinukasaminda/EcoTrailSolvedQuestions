from PIL import Image
im = Image.open("download.png") #Can be many different formats.
import math
import sys
colorsRow = [
    [
    {'key':"A",'color':[]},
    {'key':"B",'color':[]},
    {'key':"C",'color':[]},
    {'key':"D",'color':[]},
    {'key':"E",'color':[]},
    {'key':"F",'color':[]},
    {'key':"G",'color':[]},
    {'key':"H",'color':[]}],
[
    {'key':"I",'color':[]},
    {'key':"J",'color':[]},
    {'key':"K",'color':[]},
    {'key':"L",'color':[]},
    {'key':"M",'color':[]},
    {'key':"N",'color':[]},
    {'key':"O",'color':[]},
    {'key':"P",'color':[]}],[
    {'key':"Q",'color':[]},
    {'key':"R",'color':[]},
    {'key':"S",'color':[]},
    {'key':"T",'color':[]},
    {'key':"U",'color':[]},
    {'key':"V",'color':[]},
    {'key':"W",'color':[]},
    {'key':"X",'color':[]}],[
    {'key':"Y",'color':[]},
    {'key':"Z",'color':[]},
    {'key':"a",'color':[]},
    {'key':"b",'color':[]},
    {'key':"c",'color':[]},
    {'key':"d",'color':[]},
    {'key':"e",'color':[]},
    {'key':"f",'color':[]}],[
    {'key':"g",'color':[]},
    {'key':"h",'color':[]},
    {'key':"i",'color':[]},
    {'key':"j",'color':[]},
    {'key':"k",'color':[]},
    {'key':"l",'color':[]},
    {'key':"m",'color':[]},
    {'key':"n",'color':[]}],[
    {'key':"o",'color':[]},
    {'key':"p",'color':[]},
    {'key':"q",'color':[]},
    {'key':"r",'color':[]},
    {'key':"s",'color':[]},
    {'key':"t",'color':[]},
    {'key':"u",'color':[]},
    {'key':"v",'color':[]}],[
    {'key':"w",'color':[]},
    {'key':"x",'color':[]},
    {'key':"y",'color':[]},
    {'key':"z",'color':[]},
    {'key':"0",'color':[]},
    {'key':"1",'color':[]},
    {'key':"2",'color':[]},
    {'key':"3",'color':[]}],[
    {'key':"4",'color':[]},
    {'key':"5",'color':[]},
    {'key':"6",'color':[]},
    {'key':"7",'color':[]},
    {'key':"8",'color':[]},
    {'key':"9",'color':[]},
    {'key':"+",'color':[]},
    {'key':"/",'color':[]}]
    ]

colors = [[0,0,0],[255,0,0],[0,0,255],[100,126,130],[255,0,255],[60,127,0],[128,60,60],[255,125,0]]

def VecDistance(v1,v2):
    res1 = math.pow(v1[0]-v2[0],2) + math.pow(v1[1]-v2[1],2)+ math.pow(v1[2]-v2[2],2)
    return res1
def getColorIndx(v1):
    distList = []
    for i in range(0,len(colors)):
        distList.append({'key':i,'v1':VecDistance(v1,colors[i]) })
    distList.sort(key=lambda x: x['v1'], reverse=False) 
    return distList[0]['key']


mWidth = 17
boxW = 40

offset1 = 5
offset2 = 20

print("mWidth:",mWidth," , boxW:",boxW)

pix = im.load()

str1 = ""
for j  in range (0,17):
   
    for i in range (0,17):
        vp1 = pix[boxW*i +offset1,j*boxW +offset1]
        v1Px = [vp1[0],vp1[1],vp1[2]]
        colorIndex1 = getColorIndx(v1Px)

        vp2 = pix[boxW*i +offset2,j*boxW +offset2]
        v2Px = [vp2[0],vp2[1],vp2[2]]
        colorIndex2 = getColorIndx(v2Px)
        str1 += colorsRow[colorIndex1][colorIndex2]['key']

print(str1) #plz ignore the last colors for white space 
        

'''

index = mWidth*jVl + xVl
getColorIndx([255,0,255])
'''

'''
print("len:",len(colorsRow))
pix = im.load()
wdith,height =im.size #Get the width and hight of the image for iterating over
print ("w",wdith,"h",height)

row = 0

for j in range(0,height):
    marks = 0
    for i in range(0,wdith):
        value = pix[i,j]
        if(i<100):
            if (value[0]==0 and value[1]==0 and value[2]==0):
                marks +=1
        else :
            if marks > 90 :
                pix[i,row] = value # Set the RGBA Value of the image (tuple)
    if marks > 90 :
        row +=1
im.save("alive_parrot.png") # Save the modified pixels as png
'''