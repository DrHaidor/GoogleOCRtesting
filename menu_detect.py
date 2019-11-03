from google.cloud import vision
import os

os.environ['GRPC_DNS_RESOLVER'] = 'native'

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'gs://gag_image_bucket/menu.jpg'

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))
