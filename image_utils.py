from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(file_path):
    img = Image.open(file_path)
    img_array = np.array(img)
    return img_array
    
def edge_detection(image):
    gray_image = np.mean(image, axis=2)
    kernelY = np.array([[1, 1, 1], 
                    [0, 0, 0],
                    [-1, -1, -1]])
    kernelX = np.array([[1,  0,  -1],
                    [1,  0,  -1],
                    [1,  0,  -1]])
    filteredx = convolve2d(gray_image, kernelX, mode='same')
    filteredy = convolve2d(gray_image, kernelY, mode='same')
    
    edgeMAG = np.sqrt(filteredx**2 + filteredy**2)
    plt.axis('off')

    return edgeMAG
  
