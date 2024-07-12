!mkdir insta-posted

%%writefile mkimag.py
#import Image and ImageEnhance modules
from PIL import Image, ImageEnhance, ImageChops
from random import randint
import random
import os
import time
import shutil
def mkimag():
    #PatH=["publish/"]
    #num2 = randint(0,len(PatH)-1)
    path = "publish/"
    base_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
        ])
    file=(path+base_image)

    im = Image.open(file)# Open an Image file
    
    src_path = file
    dst_path = "insta-posted/"
    shutil.move(file, dst_path)
    print(file)
    im = im.resize((960,960), Image.ANTIALIAS)
    #print(im.size)
    Brighten = ImageEnhance.Brightness(im) # Create a Brightness class
    brightimage = Brighten.enhance(1.1)
    brightimage.save("junk/temp-brightened.jpg") # Save results
 
    im = Image.open("junk/temp-brightened.jpg") # Open the Image
    sharpened = ImageEnhance.Sharpness(im) # Create an object using Sharpness
    sharpenedimage = sharpened.enhance(1.1)
    sharpenedimage.save("junk/temp-sharpenedimage.jpg") # Save results
 
    im = Image.open('junk/temp-sharpenedimage.jpg') # Open the Image
    contrast = ImageEnhance.Contrast(im) # Create an object using Sharpness
    contrastedimage = contrast.enhance(1.1)
    contrastedimage.save('junk/temp-contrastedimage.jpg') # Save results
 
    im = Image.open("junk/temp-contrastedimage.jpg")
    width, height = im.size   # Get dimensions
    #im = im.resize((2*width,2*height), "Image.NEAREST" (0))
    #im = im.resize((2*width,2*height), Image.ANTIALIAS)
    Choose = ["insta-usa-perferations.png", "insta-philippines-perferations.png","insta-perferations.png"]
    num = randint(0,2)
    border = (Choose[num])
    mask=Image.open(border).convert('RGBA') 
    im.paste(mask, (0,0), mask=mask)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "junk/insta"+timestr+"_.jpg"
    im.save(filename)
    im.save('junk/temp1.jpg')
    return im    


mkimag()

#%%writefile use-post-to-instagram.py
#!/home/jack/miniconda3/envs/cloned_base/bin/python
from instabot import Bot
import os
import shutil
import markovify
from PIL import Image, ImageEnhance, ImageChops
from mkimag import mkimag
im = mkimag()


with open("sart.txt") as f:
    data = f.read()
data_model = markovify.Text(data)
STR = "#computerart #computergraphic #Bots #Python "+data_model.make_sentence()+"""path = "publish/"
base_image = random.choice([
x for x in os.listdir(path)
if os.path.isfile(os.path.join(path, x))
        ])
file=(path+base_image)
im = Image.open(file)# Open an Image file"""



def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("junk/{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):
    bot = Bot()

    bot.login(username="jacklnorthrup", password="Pxyackjs22")
    bot.upload_photo("junk/{}".format(i), caption=STR)


#if __name__ == '__main__':
# enter name of your image bellow
image_name = "temp1.jpg"
clean_up(image_name)
upload_post(image_name)
print(image_name)



!ls publish/274_20220925170825.jpg

from PIL import Image
im = Image.open("insta-posted/274_20220925170825.jpg")
im

randint(2000, 5000)*.01



