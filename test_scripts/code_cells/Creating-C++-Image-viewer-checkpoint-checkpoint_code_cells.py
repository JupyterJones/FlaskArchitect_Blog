%%writefile showme.cpp
#include <cv.h>
#include <highgui.h>
#include <iostream>
using namespace cv;
using namespace std;
int main(int argc,char **argv)
{
   Mat image;
   image = imread(argv[1],1);

   if(argc != 2 || !image.data)
   {
       cout << "No image data\n";
       return -1;
   }

   namedWindow("Image Viewer",CV_WINDOW_AUTOSIZE);
   imshow("Image Viewer",image);
   waitKey(0);
   return 0;
}

# Compile the Image Viewer below  showme.cpp
!g++ showme.cpp -o showme `pkg-config opencv --cflags --libs`

#The showme file was made executable "  chmod a+x showme "

!chmod a+x showme

# I wantedto use it from all directories
# this copies the showme file to ' /usr/local/bin '

!cp showme /usr/local/bin

!mkdir images

#retrieve a public domainimage from Wiki and name it face.jpg
!wget -O images/face.jpg https://upload.wikimedia.org/wikipedia/commons/3/33/Arnold_Schwarzenegger_edit%28ws%29.jpg

!showme images/face.jpg



