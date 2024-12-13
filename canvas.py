import numpy as np
from PIL import Image

"""creating the canvas with user specified width and height and color"""
class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        #create 3d zeros numpy array
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        #fill the [0,0,0] np array with user given color
        self.data[:] = self.color
    #convert current array into and image
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
