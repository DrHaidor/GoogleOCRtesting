"""Detects text in the file."""
from google.cloud import vision
import io

import argparse
import os

os.environ['GRPC_DNS_RESOLVER'] = 'native'
#path = '/home/gag/Dropbox/GCP/python-docs-samples/vision/cloud-client/detect/resources/TestText/7/MedText07.jpg'
path = '/home/gag/Dropbox/GCP/python-docs-samples/vision/cloud-client/detect/resources/test_data.tar/18.jpg'


client = vision.ImageAnnotatorClient()

# [START vision_python_migration_text_detection]
with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
#print('Texts:\n')
#print(texts)

#for text in texts:
#    print('\n"{}"'.format(text.description))

print(texts[0].description)

    #vertices = (['({},{})'.format(vertex.x, vertex.y)
    #    for vertex in text.bounding_poly.vertices])

    #print('bounds: {}'.format(','.join(vertices)))
# [END vision_python_migration_text_detection]

# [END vision_text_detection]