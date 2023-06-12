import boto3
import cv2

# define AWS credentials and region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# create Rekognition client
rekognition = boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# read image
image_path = 'example.jpg'
with open(image_path, 'rb') as image_file:
    image_bytes = image_file.read()

# get image dimensions
image = cv2.imread(image_path)
height, width, _ = image.shape

# define bounding box coordinates
box = {'Width': 0.44773998856544495, 'Height': 0.12381000071763992, 'Left': 0.49772998690605164, 'Top': 0.2612900137901306}
x1 = int(box['Left'] * width)
y1 = int(box['Top'] * height)
x2 = int((box['Left'] + box['Width']) * width)
y2 = int((box['Top'] + box['Height']) * height)

# detect text in image using Rekognition
response = rekognition.detect_text(Image={'Bytes': image_bytes})

# display bounding boxes around text
for text in response['TextDetections']:
    if text['Type'] == 'LINE' and x1 < text['Geometry']['BoundingBox']['Left'] * width < x2 and y1 < text['Geometry']['BoundingBox']['Top'] * height < y2:
        box_left = int(text['Geometry']['BoundingBox']['Left'] * width)
        box_top = int(text['Geometry']['BoundingBox']['Top'] * height)
        box_width = int(text['Geometry']['BoundingBox']['Width'] * width)
        box_height = int(text['Geometry']['BoundingBox']['Height'] * height)
        image = cv2.rectangle(image, (box_left, box_top), (box_left + box_width, box_top + box_height), (0, 255, 0), 2)

# display image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
