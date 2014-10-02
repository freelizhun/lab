from PIL import Image
 
im = Image.new("RGB", (255,100))
#for x in range(im.size[0]):
#    for y in range(im.size[1]):
#        im.putpixel((x,y), (x,x,x))

im.save('pix.jpg')
