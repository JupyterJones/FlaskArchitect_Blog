from PIL import Image
# Creating a image1 object
image1 = Image.open("image1.jpg").convert("RGBA")
# Creating a image2 object
image2 = Image.open("image2.jpg").convert("RGBA")
image2 = image2.resize(image1.size)
count = 0
for i in range(0,11):
   I = float(i*.1)
   count = count +1
   # As Alpha value is 0.0, Image1 would be returned
   image3 = Image.blend(image1,image2,I)
   print(I)
   image3.save(str(count)+"output1.png")
#image3.show()
# As Alpha value is 0.5, Blend of both would be returned
image4 = Image.blend(image1,image2,0.5)
image4.save("output2.png")
image4.show()

from PIL import Image
# creating image object
img10 = Image.open("image2.jpg").convert("RGBA")
# creating image2 object having alpha
img2 = Image.open("image1.jpg").convert("RGBA")
img2 = img2.resize(img10.size)
# using alpha_composite
image4 = Image.blend(img10,img2,0.5)
image4.show()

!pwd

color = (0, 0, 0,3)
formatted_color = tuple(f"{c:04}".replace(" ", "0") for c in color)
print(formatted_color)


 opacity = 150
 r, g, b, a = 0, 0, 0, opacity
color = (r, g, b, a)
formatted_color = tuple(f"{c:04}".replace(" ", "0") for c in color)
r,g,b,a = formatted_color
R,G,B,A = int(r),int(g),int(b),int(a)
print(R,G,B,A)

img10



