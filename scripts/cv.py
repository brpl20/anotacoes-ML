import cv2
import json

with open('cv-aws.json', 'r') as f:
    data = json.load(f)

img = cv2.imread('cnh_bruno.jpg')
dimensions = img.shape
height, width, _ = img.shape
box = data["CustomLabels"][1]["Geometry"]["BoundingBox"]
box4 = data["CustomLabels"][4]["Geometry"]["BoundingBox"]

color = (0, 0, 255) # red color in BGR
thickness = 2

#print(data["CustomLabels"][1]) # Filiacao
#print(data["CustomLabels"][1]["Geometry"]["BoundingBox"]) # Filiacao
#print(data["CustomLabels"][1]["Geometry"]["BoundingBox"]["Width"]) # Filiacao


x1 = int(box['Left'] * width)
y1 = int(box['Top'] * height)
x2 = int((box['Left'] + box['Width']) * width)
y2 = int((box['Top'] + box['Height']) * height)


x14 = int(box4['Left'] * width)
y14 = int(box4['Top'] * height)
x24 = int((box4['Left'] + box4['Width']) * width)
y24 = int((box4['Top'] + box4['Height']) * height)


#x = int(points['x'])
#y = int(points['y'])
#w = int(points['width'])
#h = int(points['height'])
#retangle = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) # 3x4 (online)
retangle = cv2.rectangle(img, (x14, y14), (x24, y24), color, thickness)

cv2.imshow('imagem_com_retant', retangle)
cv2.waitKey(0)
cv2.destroyAllWindows()








# print(dimensions)
# print(dimensions[0]) # Heigh
# print(dimensions[1]) # Width
# height = img.shape[0]
# width = img.shape[1]
#retangle = cv2.rectangle(img, (int(points['x']), points['y']), (points['x']+points['width'], points['y']+points['height']), (0, 255, 0), 2) # 3x4 (online)

#retangle = cv2.rectangle(img, (159, 216), (159+161, 216+175), (0, 255, 0), 2) # 3x4 (curl)
#retangle = cv2.rectangle(img, (247, 341), (247+494, 341+682), (0, 255, 0), 2) # CNH


# "x":247.0,"y":341.0,"width":494.0,"height":682.0,"confidence":0.9660571813583374,"class":"CNH"},{"x":353.0,"y":232.0,"width":228.0,"height":82.0,"confidence":0.9155141115188599,"class":"Filiacao"},{"x":159.5,"y":216.5,"width":161.0,"height":175.0,"confidence":0.9126549959182739,"class":"3x4"},{"x":206.5,"y":512.5,"width":255.0,"height":41.0,"confidence":0.8657625913619995,"class":"Assinatura"},{"x":422.0,"y":170.5,"width":96.0,"height":35.0,"confidence":0.8649376630783081,"class":"Nascimento"},{"x":356.0,"y":137.5,"width":224.0,"height":29.0,"confidence":0.8633474111557007,"class":"Identidade"},{"x":310.0,"y":171.0,"width":124.0,"height":32.0,"confidence":0.858777642250061,"class":"CPF"},{"x":268.0,"y":104.5,"width":386.0,"height":29.0,"confidence":0.7378206849098206,"class":"Nome"}]}%                         ➜  PNGs


#where pt1 is starting point-->(x,y) and pt2 is end point-->(x+w,y+h).


      # "x": 118.5,
      # "y": 160,
      # "width": 119,
      # "height": 130,
      # "confidence": 0.913,
      # "class": "3x4"
# {"x":159.5,"y":216.5,"width":161.0,"height":175.0,"confidence":0.9126549959182739,"class":"3x4"}



# {"time":0.07140130199968553,"image":{"width":494,"height":690},"predictions":[{"x":247.0,"y":341.0,"width":494.0,"height":682.0,"confidence":0.9660571813583374,"class":"CNH"},{"x":353.0,"y":232.0,"width":228.0,"height":82.0,"confidence":0.9155141115188599,"class":"Filiacao"},,{"x":206.5,"y":512.5,"width":255.0,"height":41.0,"confidence":0.8657625913619995,"class":"Assinatura"},{"x":422.0,"y":170.5,"width":96.0,"height":35.0,"confidence":0.8649376630783081,"class":"Nascimento"},{"x":356.0,"y":137.5,"width":224.0,"height":29.0,"confidence":0.8633474111557007,"class":"Identidade"},{"x":310.0,"y":171.0,"width":124.0,"height":32.0,"confidence":0.858777642250061,"class":"CPF"},{"x":268.0,"y":104.5,"width":386.0,"height":29.0,"confidence":0.7378206849098206,"class":"Nome"}]}%                                                                                                                                                                                    ➜  PNGs





