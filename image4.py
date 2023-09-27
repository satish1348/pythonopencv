from PIL import Image
im=Image.open("pxfuel.jpg").convert('L')
#im.thumbnail((100,100))
im.show()