from PIL import Image
im=Image.open("pxfuel.jpg")
#im.show()
im.rotate(25).show()
im.save("pxfuels.png")