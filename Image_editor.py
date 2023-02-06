#Python project 1
#Image editor
#Applies the same edit to all the images 

from PIL import Image, ImageEnhance, ImageFilter
import os

#path of image to be edited
path = './images'

#path of edited images to be placed
pathOut = '/editedImages'

#for image in the path
for filename in os.listdir(path):
    #opens the image
    img = Image.open(f"{path}/{filename}")

    #applies the following edits
    #L = Black and white
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    #code to enhance image by scale
    scale = 2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(scale)

    clean_name = os.path.splitext(filename) [0]

    #saves image in new folder
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')   

