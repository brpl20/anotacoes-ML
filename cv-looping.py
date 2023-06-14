import cv2
import json
import pytesseract

with open('cv-aws.json', 'r') as f:
    data = json.load(f)

for customLabel in data['CustomLabels']:
    if 'Geometry' in customLabel:
        img = cv2.imread('cnh_bruno.jpg')
        dimensions = img.shape
        height, width, _ = img.shape
        box = customLabel['Geometry']['BoundingBox']
        color = (0, 0, 255)
        thickness = 2
        x = int(box['Left'] * width)
        y = int(box['Top'] * height)
        w = int((box['Left'] + box['Width']) * width)
        h = int((box['Top'] + box['Height']) * height)
        cv2.rectangle(img, (x, y), (w, h), color, thickness)
        cv2.putText(img, customLabel['Name'], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        ret_to_read = cv2.rectangle(img, (x, y), (w, h), color, thickness)
        text = pytesseract.image_to_string(ret_to_read)
        print(text)
        cv2.imshow('imagem_com_retant', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



