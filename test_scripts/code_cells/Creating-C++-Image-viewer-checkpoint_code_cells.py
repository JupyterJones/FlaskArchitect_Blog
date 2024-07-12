!locate opencv2/core.hpp

/usr/include/opencv4/opencv2/highgui.hpp

#include "opencv2/highgui/highgui.hpp"

%%writefile showme.cpp
#include </usr/lib/x86_64-linux-gnu/perl/5.30.0/CORE/cv.h>
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

!locate CORE/cv.h

%%writefile showme.cpp
#include </usr/lib/x86_64-linux-gnu/perl/5.30.0/CORE/cv.h>
#include <opencv4/opencv2/highgui.hpp>
#include </usr/local/include/opencv4/opencv2/core.hpp>
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

!g++ `pkg-config --cflags opencv4` showme.cpp -o showme

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

# Here is a nice Image Blending program written in C++

%%writefile controlBlend.cpp
#include <cv.h>
#include <highgui.h>

using namespace cv;

/// Global Variables
const int alpha_slider_max = 100;
int alpha_slider;
double alpha;
double beta;

/// Matrices to store images
Mat src1;
Mat src2;
Mat dst;

/**
 * @function on_trackbar
 * @brief Callback for trackbar
 */
void on_trackbar( int, void* )
{
 alpha = (double) alpha_slider/alpha_slider_max ;
 beta = ( 1.0 - alpha );

 addWeighted( src1, alpha, src2, beta, 0.0, dst);

 imshow( "Linear Blend", dst );
}

int main( int argc, char** argv )
{
 /// Read image ( same size, same type )
 src1 = imread("images/hicks01.jpg");
 src2 = imread("images/hicks02.jpg");

 if( !src1.data ) { printf("Error loading src1 \n"); return -1; }
 if( !src2.data ) { printf("Error loading src2 \n"); return -1; }

 /// Initialize values
 alpha_slider = 0;

 /// Create Windows
 namedWindow("Linear Blend", 1);

 /// Create Trackbars
 char TrackbarName[50];
 sprintf( TrackbarName, "Alpha x %d", alpha_slider_max );

 createTrackbar( TrackbarName, "Linear Blend", &alpha_slider, alpha_slider_max, on_trackbar );

 /// Show some stuff
 on_trackbar( alpha_slider, 0 );

 /// Wait until user press some key
 waitKey(0);
 return 0;
}

!g++ controlBlend.cpp -o controlBlend `pkg-config opencv --cflags --libs`

# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip
# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
unzip opencv.zip
# Create build directory
mkdir -p build && cd build
# Configure
cmake  ../opencv-4.x
# Build
cmake --build .
Build with opencv_contrib
# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip
# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
unzip opencv.zip
unzip opencv_contrib.zip
# Create build directory and switch into it
mkdir -p build && cd build
# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x
# Build
cmake --build .
Detailed process

This section provides more details of the build process and describes alternative methods and tools. Please refer to the OpenCV installation overview tutorial for general installation details and to the OpenCV configuration options reference for configuration options documentation.
Install compiler and build tools

    To compile OpenCV you will need a C++ compiler. Usually it is G++/GCC or Clang/LLVM:
        Install GCC...
        sudo apt install -y g++
        ... or Clang:
        sudo apt install -y clang
    OpenCV uses CMake build configuration tool:
    sudo apt install -y cmake
    CMake can generate scripts for different build systems, e.g. make, ninja:
        Install Make...
        sudo apt install -y make
        ... or Ninja:
        sudo apt install -y ninja-build
    Install tool for getting and unpacking sources:
        wget and unzip...
        sudo apt install -y wget unzip
        ... or git:
        sudo apt install -y git

Download sources

There are two methods of getting OpenCV sources:

    Download snapshot of repository using web browser or any download tool (~80-90Mb) and unpack it...
    wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
    unzip opencv.zip
    mv opencv-4.x opencv
    ... or clone repository to local machine using git to get full change history (>470Mb):
    git clone https://github.com/opencv/opencv.git
    git -C opencv checkout 4.x

Note
    Snapshots of other branches, releases or commits can be found on the GitHub and the official download page.

Configure and build

    Create build directory:
    mkdir -p build && cd build
    Configure - generate build scripts for the preferred build system:
        For make...
        cmake ../opencv
        ... or for ninja:
        cmake -GNinja ../opencv
    Build - run actual compilation process:
        Using make...
        make -j4
        ... or ninja:
        ninja

Note
    Configure process can download some files from the internet to satisfy library dependencies, connection failures can cause some of modules or functionalities to be turned off or behave differently. Refer to the OpenCV installation overview and OpenCV configuration options reference tutorials for details and full configuration options reference.
    If you experience problems with the build process, try to clean or recreate the build directory. Changes in the configuration like disabling a dependency, modifying build scripts or switching sources to another branch are not handled very well and can result in broken workspace.
    Make can run multiple compilation processes in parallel, -j<NUM> option means "run <NUM> jobs simultaneously". Ninja will automatically detect number of available processor cores and does not need -j option.

Check build results

After successful build you will find libraries in the build/lib directory and executables (test, samples, apps) in the build/bin directory:
ls bin
ls lib

CMake package files will be located in the build root:
ls OpenCVConfig*.cmake
ls OpenCVModules.cmake
Install

Warning
    The installation process only copies files to predefined locations and does minor patching. Installing using this method does not integrate opencv into the system package registry and thus, for example, opencv can not be uninstalled automatically. We do not recommend system-wide installation to regular users due to possible conflicts with system packages.

By default OpenCV will be installed to the /usr/local directory, all files will be copied to following locations:

    /usr/local/bin - executable files
    /usr/local/lib - libraries (.so)
    /usr/local/cmake/opencv4 - cmake package
    /usr/local/include/opencv4 - headers
    /usr/local/share/opencv4 - other files (e.g. trained cascades in XML format)

Since /usr/local is owned by the root user, the installation should be performed with elevated privileges (sudo):
sudo make install

or
sudo ninja install

Installation root directory can be changed with CMAKE_INSTALL_PREFIX configuration parameter, e.g. -DCMAKE_INSTALL_PREFIX=$HOME/.local to install to current user's local directory. Installation layout can be changed with OPENCV_*_INSTALL_PATH parameters. See OpenCV configuration options reference for details.
Generated on Sun Sep 18 2022 01:05:06 for OpenCV by   doxygen 1.8.13 

