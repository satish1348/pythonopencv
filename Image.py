from PIL import Image
im=Image.open("pxfuel.jpg")
print(im)
print(im.size)
print(im.format)
im.show()
im.rotate(25).show()