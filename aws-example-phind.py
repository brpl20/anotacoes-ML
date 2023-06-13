import boto3
import cv2

# define AWS credentials and region
aws_access_key_id = ''
aws_secret_access_key = ''
region_name = 'us-east-2'

# create Rekognition client
session = boto3.Session(profile_name='default')
client = session.client('rekognition')
rekognition = boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# read image
image_path = 'cnh_bruno.jpg'
with open(image_path, 'rb') as image_file:
    image_bytes = image_file.read()

# get image dimensions
image = cv2.imread(image_path)
height, width, _ = image.shape

# define bounding box coordinates
# box = {'Width': 0.44773998856544495, 'Height': 0.12381000071763992, 'Left': 0.49772998690605164, 'Top': 0.2612900137901306}
# x1 = int(box['Left'] * width)
# y1 = int(box['Top'] * height)
# x2 = int((box['Left'] + box['Width']) * width)
# y2 = int((box['Top'] + box['Height']) * height)

# detect text in image using Rekognition
#response = rekognition.detect_text(Image={'Bytes': image_bytes})

response = client.detect_text(Image={'S3Object': {'Bucket': 'cnhnew', 'Name': 'cnh_bruno.jpg', 'Geometry': {'BoundingBox': {'Width': 0.5978781580924988, 'Height': 0.019790904596447945, 'Left': 0.19031666219234467, 'Top': 0.03172283619642258} }}})


             #'Polygon': [{'X': 0.1904338151216507, 'Y': 0.03172283619642258}, {'X': 0.7881948351860046, 'Y': 0.03367360681295395}, {'X': 0.7880776524543762, 'Y': 0.05151373893022537}, {'X': 0.19031666219234467, 'Y': 0.049562968313694}]}}

print(response)
# display bounding boxes around text
# for text in response['TextDetections']:
#     if text['Type'] == 'LINE' and x1 < text['Geometry']['BoundingBox']['Left'] * width < x2 and y1 < text['Geometry']['BoundingBox']['Top'] * height < y2:
#         box_left = int(text['Geometry']['BoundingBox']['Left'] * width)
#         box_top = int(text['Geometry']['BoundingBox']['Top'] * height)
#         box_width = int(text['Geometry']['BoundingBox']['Width'] * width)
#         box_height = int(text['Geometry']['BoundingBox']['Height'] * height)
#         image = cv2.rectangle(image, (box_left, box_top), (box_left + box_width, box_top + box_height), (0, 255, 0), 2)

# display image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
