INPUT="leo-livebak/00040.jpg"
ZOOM_SPEED=0.0015
MAX_ZOOM=2.5
DURATION=700
W=640
H=640
OUTPUT="variables.mp4"
FPS=24
XP=-1
YP=-5
ffmpeg -i "$INPUT" \
   -vf "scale=8000:-1,zoompan=z='min(zoom+${ZOOM_SPEED},${MAX_ZOOM})':x='iw/2-iw*(1/2-${XP}/100)*on/${DURATION}-iw/zoom/2':y='ih/2-ih*(1/2-${YP}/100)*on/${DURATION}-ih/zoom/2':d=${DURATION}:fps=${FPS}:s=${W}x${H},unsharp=5:5:1.5:5:5:0.0" \
   -c:v libx264 "$OUTPUT" -y
   
vlc variables.mp4   

vlc variables.mp4  

ffmpeg -hide_banner -i leo-livebak/00025.jpg -vf "scale=8000:-1,zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=640x640,unsharp=5:5:1.5:5:5:0.0" -c:v libx264 -y live_bak004.mp4
vlc live_bak004.mp4


ffmpeg -hide_banner -i leo-livebak/00025.jpg -vf "crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(n/10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(n/7)" -y live_bak004.mp4


ffmpeg -hide_banner -i leo-livebak/00025.jpg -vf crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(n/10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(n/7) -y live_bak004.mp4
vlc live_bak004.mp4

Path="sin(2*PI*t)"
ffmpeg -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1+${Path}):x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4


Path=sin(2*PI*t)
FFMPEG -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1+${Path})':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4

Path=sin(2*PI*t)

ffmpeg -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1*.02),1':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4

z='(exp(sin(t)))'

FFMPEG -hide_banner -i leo-livebak/00017.jpg -vf "zoompan=z='exp(0.001*(t/10)*0.5+1.5)':x='100*t':y='50*t':s=640x480" -c:v libx264 -y output.mp4


PATH=exp(sin(t/0.1)*0.5+1.5)

FFMPEG -hide_banner -i leo-livebak/00017.jpg -vf " scale=8000:-1,zoompan=z='min(zoom+0.0015,2.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a--5)':y='if(gte(zoom,2.5),y,y-15)':s=560x560,unsharp=5:5:1.5:5:5:0.0" -y live_bak001ah2.mp4
vlc live_bak001ah2.mp4

ffmpeg -hide_banner -i leo-livebak/00017.jpg -vf "zoompan=z='exp(sin(t/0.1)*0.5+1.5)':x='100*t':y='50*t':s=640x480" -c:v libx264 -y output.mp4


FFMPEG -hide_banner -i leo-livebak/00017.jpg -vf " scale=8000:-1,zoompan=z='min(zoom+0.0015,2.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a--5)':y='if(gte(zoom,2.5),y,y-15)':s=560x560,unsharp=5:5:1.5:5:5:0.0" -y live_bak001ah2.mp4
vlc live_bak001ah2.mp4

FFMPEG -hide_banner -i leo-livebak/00017.jpg -vf " scale=8000:-1,zoompan=z='min(zoom+0.0015,2.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a--5)':y='if(gte(zoom,2.5),y,y-15)':s=560x560,unsharp=5:5:1.5:5:5:0.0" -y live_bak001ah2.mp4
vlc live_bak001ah2.mp4

vlc live_bak001a.mp4

FFMPEG -hide_banner -i leo-livebak/00010.jpg -vf " scale=8000:-1,zoompan=z='min(zoom+0.0015,2.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a--5)':y='if(gte(zoom,2.5),y,y-15)':s=560x560" -y live_bak001a.mp4
vlc live_bak001a.mp4



FFMPEG -hide_banner -i leo-livebak/00010.jpg -vf " crop=560:560,zoompan=z='min(zoom+0.0015,1.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a)':y='if(gte(zoom,1.5),y,y+1)':s=560x560" -y live_bak001.mp4


#Zoom in up to 1.5x and pan at same time to some spot near center of picture:

    zoompan=z='min(zoom+0.0015,1.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a)':y='if(gte(zoom,1.5),y,y+1)':s=640x360




ls leo-livebak 

FFMPEG -i Videos/0bf7b3cb-cd74-4f4f-aada-606e74d46088+.mp4 -vf "hwupload, convolution_opencl=0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0:0 -1 0 -1 5 -1 0 -1 0, hwdownload" -y OUTPUT.mp4


ls Videos

Apply Zoom & Pan effect.

This filter accepts the following options:

zoom, z

    Set the zoom expression. Range is 1-10. Default is 1.
x
y

    Set the x and y expression. Default is 0.
d

    Set the duration expression in number of frames. This sets for how many number of frames effect will last for single input image. Default is 90.
s

    Set the output image size, default is ’hd720’.
fps

    Set the output frame rate, default is ’25’. 

Each expression can contain the following constants:

in_w, iw

    Input width.
in_h, ih

    Input height.
out_w, ow

    Output width.
out_h, oh

    Output height.
in

    Input frame count.
on

    Output frame count.
in_time, it

    The input timestamp expressed in seconds. It’s NAN if the input timestamp is unknown.
out_time, time, ot

    The output timestamp expressed in seconds.
x
y

    Last calculated ’x’ and ’y’ position from ’x’ and ’y’ expression for current input frame.
px
py

    ’x’ and ’y’ of last output frame of previous input frame or 0 when there was not yet such frame (first input frame).
zoom

    Last calculated zoom from ’z’ expression for current input frame.
pzoom

    Last calculated zoom of last output frame of previous input frame.
duration

    Number of output frames for current input frame. Calculated from ’d’ expression for each input frame.
pduration

    number of output frames created for previous input frame
a

    Rational number: input width / input height
sar

    sample aspect ratio
dar

    display aspect ratio

11.297.1 Examples

    Zoom in up to 1.5x and pan at same time to some spot near center of picture:

    zoompan=z='min(zoom+0.0015,1.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a)':y='if(gte(zoom,1.5),y,y+1)':s=640x360

    Zoom in up to 1.5x and pan always at center of picture:
11.50.1 Examples

    Crop area with size 100x100 at position (12,34).

    crop=100:100:12:34

    Using named options, the example above becomes:

    crop=w=100:h=100:x=12:y=34

    Crop the central input area with size 100x100:

    crop=100:100

    Crop the central input area with size 2/3 of the input video:

    crop=2/3*in_w:2/3*in_h

    Crop the input video central square:

    crop=out_w=in_h
    crop=in_h

    Delimit the rectangle with the top-left corner placed at position 100:100 and the right-bottom corner corresponding to the right-bottom corner of the input image.

    crop=in_w-100:in_h-100:100:100

    Crop 10 pixels from the left and right borders, and 20 pixels from the top and bottom borders

    crop=in_w-2*10:in_h-2*20

    Keep only the bottom right quarter of the input image:

    crop=in_w/2:in_h/2:in_w/2:in_h/2

    Crop height for getting Greek harmony:

    crop=in_w:1/PHI*in_w

    Apply trembling effect:

    crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(n/10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(n/7)

    Apply erratic camera effect depending on timestamp:

    crop=in_w/2:in_h/2:(in_w-out_w)/2+((in_w-out_w)/2)*sin(t*10):(in_h-out_h)/2 +((in_h-out_h)/2)*sin(t*13)

    Set x depending on the value of y:

    crop=in_w/2:in_h/2:y:10+10*sin(n/10)


    zoompan=z='min(zoom+0.0015,1.5)':d=700:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'

    Same as above but without pausing:

    zoompan=z='min(max(zoom,pzoom)+0.0015,1.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'

    Zoom in 2x into center of picture only for the first second of the input video:

    zoompan=z='if(between(in_time,0,1),2,1)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'



ffmpeg -i /home/jack/Desktop/EXP_notebooks/Videos/1c967f85-7d43-4b94-b2f8-0d592122f946++.mp4 -vf " scale=8000:-1,     crop=512:512,zoompan=z='min(max(zoom,pzoom)+0.0015,1.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)',scale=512x512,unsharp=5:5:1.5:5:5:0.0" -aspect 1:1 -y  tytghyf.mp4

ffmpeg -i /home/jack/Desktop/EXP_notebooks/Videos/1c967f85-7d43-4b94-b2f8-0d592122f946++.mp4 -vf " crop=in_w/2:in_h/2:y:10+10*sin(n/10),zoompan=z='min(max(zoom,pzoom)+0.0015,1.5)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'" -y ghyf.mp4



