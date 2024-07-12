!CREATEimage

!ls -ant images
# The top file is the last image created

from PIL import Image
IM = Image.open('images/202002221501-final.png')
IM

!cp images/202002221501-final.png /var/www/lbry-toolbox.com/public/thumbnails/

from PIL import Image
IM1 = Image.open('/var/www/lbry-toolbox.com/public/thumbnails/202002221501-final.png')
IM1



