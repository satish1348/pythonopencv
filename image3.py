from PIL import Image
im=Image.open("pxfuel.jpg")
im.thumbnail((100,100))
im.show()