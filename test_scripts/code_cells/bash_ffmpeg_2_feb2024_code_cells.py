ffmpeg -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1*t,1)':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4



Path=sin(2*PI*t

ffmpeg -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1*.02),1':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4


ffmpeg -hide_banner -i leo-livebak/00025.jpg -filter_complex "[0:v]zoompan=z='if(eq(on,0),1.5+0.1*sin(2*PI*t),1)':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0[outv]" -map "[outv]" -c:v libx264 -y output4333.mp4


ffmpeg -i leo-livebak/00025.jpg -vf "zoompan=z='if(eq(on,0),1.5+0.1*sin(2*PI*t),1)':x='if(eq(on,0),100*t,100)':y='if(eq(on,0),50*t,50)':s=640x640,unsharp=5:5:1.5:5:5:0.0" -c:a copy -y output4333.mp4



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

FFMPEG -hide_banner -i leo-livebak/00017.jpg -vf " scale=8000:-1,zoompan=z='min(zoom+0.0015,2.5)':d=700:x='if(gte(zoom,1.5),x,x+1/a--5)':y='if(gte(zoom,2.5),y,y-15)':s=560x560" -y live_bak001a2.mp4
vlc live_bak001a2.mp4



