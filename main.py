import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from image_utils import load_image, edge_detection

flower = load_image('/content/flower.jpg')
plt.imshow(flower)
plt.axis('off')
plt.show()

from skimage.filters import median
from skimage.morphology import ball

clean_image = median(flower, ball(3))

edge_test = edge_detection(clean_image)
edge_binary = edge_test > 100
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')


plt.imshow(edge_binary, cmap='gray')
