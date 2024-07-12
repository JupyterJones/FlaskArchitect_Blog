# Create a database of ffmpeg commands

%%writefile FFMPEG
#!/usr/bin/python3
import sys
import sqlite3
conn = sqlite3.connect("/home/jack/Desktop/FFMPEG/mpeg.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
     print ("\n******* NOTE - Notes Editor **************")
     print ("Not enough options were passed.")     
     print ("NOTE requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period.")
     print ("If printing the database -T also add a filename of your choice ( no quotes required ):")
     print (" Example: NOTE -T Data2Text.txt")   
     print ("If wanting to read all entries use -R . (use the period)") 
     print ("even use the period with help.  -H .   must be entered.")
     print ("******************************************\n")
     sys.exit()
mod = sys.argv[1]
def create():

    import sqlite3
    conn = sqlite3.connect("/home/jack/Desktop/FFMPEG/mpeg.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text

def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    #for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
    #    print ("\nINFO Found Here:",row[0],row[1])
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        if data in row[1]:    
            print ("\nINFO Found Here:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/jack/Desktop/FFMPEG/mpeg.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/jack/Desktop/FFMPEG/mpeg.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')
    fn.close()    

def HELP():
    TXT = """
    USE: NOTE argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NOTE -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NOTE -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NOTE -S 3
    -S "current project"
    NOTE -R .
    -H help on options
    NOTE -H .
    """
    print (TXT)

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R" or mod == "-r":
    main()
if mod == "-I" or mod == "-i":
    data = sys.argv[2]
    insert(data)
if mod == "-D" or mod == "-d":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S" or mod == "-s":
    data = sys.argv[2]
    search(data)       
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-C" or mod == "-c":
    create()
    print (create)
else:
    print ("_________________\n")
    print (sys.argv[2],"Command Completed")
    


import string
#with open("ffmpeghistory.py", "r") as Data:
Data = open("ffmpeghistory.py", "r").read()    
nonalpha = string.digits + string.punctuation + string.whitespace
a = set()
cnt = 0 
lines = Data.split("\n")
for line in lines:
        data = line.lstrip(nonalpha)
        cnt=cnt+1
        if len(data)>30:
            print(data)
            a.add(data)


import sys
import sqlite3
conn = sqlite3.connect("/home/jack/Desktop/FFMPEG/mpeg.db")
conn.text_factory = str
c = conn.cursor()
def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
    return data

for data in a:
    insert(data,conn=conn, c=c)
    print(data)
conn.commit()
conn.close()    

!ls 

import numpy as np
arr = np.asarray(TEXT) 

print (len(arr))

print (arr[10])

np.save("saved-arr", arr)

!ls saved*.*

!ls /home/jack/hidden

finput = open("cleanhistory.txt", "w")
for line in a:
    finput.write(line+"\n")
    print (line,"\n")
finput.close()    

fout = open("cleanhistory.txt", "r")
search = input("search term: ")
print(" ")
for line in a:
    if search in line:
        print (line)
        print("-")
    

STRINGS="""FFMPEG -fflags +genpts -r 30 -i raw.h264 -c:v copy 30output.mp4
FFMPEG -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0  -y scene3.mp4
FFMPEG -i butteredlargslow.mp4 -c:v copy -bsf hevc_mp4toannexb -f hevc  out.h265
ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -i :0.0 -f alsa -ac 2 -i default output.mkv
full screen capture with audio mic and audio out terrible noise ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f alsa -ac 2 -i hw:0 output.mkv
FFMPEG -framerate 30 -pattern_type glob -i '/home/jack/Desktop/DOCKER/deepdream/deepdream/jack/*.jpg' -c:v libx264 -pix_fmt yuv420p deepdreamglob.mp4
cat images/*.jpg | FFMPEG -f image2pipe -i - catoutput.mp4
FFMPEG -i 'jack/tmp/%04d.jpg' -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -pattern_type glob -i /home/jack/Desktop/TEST/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/TEST/glob.mp4
ffmpeg -i input.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][0:a][r] [0:a]concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" output.mp4
ffmpeg -framerate 30 -pattern_type glob -i /home/jack/Desktop/frames4/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/frames4/frames4.mp4
FFMPEG -i butteredlargslow.mp4 -c:v copy -bsf hevc_mp4toannexb out.h265
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -qscale 3 -s 1366x768 -c:v wmv1 desktop.mp4
docker run -it --rm adilm7177/ffmpeg ash -c "ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4"
sudo ffmpeg -r 10 -f image2 -i _%04d.jpg  output1.mp4
FFMPEG -i out01.mkv -map 0:v -c:v copy -bsf:v h264_mp4toannexb -y raw.h264
FFMPEG -framerate 30 -pattern_type glob -i '/home/jack/Desktop/DOCKER/deepdream/deepdream/jack/*.jpg' -c:v libx264 -pix_fmt yuv420p deepdreamglob.mp4'
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharpen=lr=1.5:ls=-0.25:lt=-3.5:cr=0.75:cs=0.250:ct=0.5" -y Jasmine_Byrne-01S.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest
ffmpeg -r 10 -f image2 -i _%04d.jpg  output1.mp4
ffmpeg  -loop 1 -t 5 -i "test.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]"test.mp4
FFMPEG -i butteredlargslow.mp4 -c:v libx265 -c:a copy -x265-params crf=2 OUTPUT_h265.mp4
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharp=5:5:1.0:5:5:0.0" Jasmine_Byrne-01S.mp4
ffmpeg -framerate 30 -i images/%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" -y test.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i %04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -i adiiiDocker.mp4 -q:v 1 -vf reverse reversedadiiiDocker.mp4
docker run -i --rm -u $UID:$GROUPS -v '$PWD:$PWD' -w '$PWD' mwader/static-ffmpeg:5.0.1-3 -i $1 -vf 'scale=trunc(iw/4)*2:trunc(ih/4)*2' -c:v libx265 -preset slow -crf 20 -y preset$1
ffmpeg -framerate 10 -i _%04d.jpg -c:v libx264 -vf fps=20 -pix_fmt yuv420p -y out.mp4
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharped=lr=1.5:ls=-0.25:lt=-3.5:cr=0.75:cs=0.250:ct=0.5" -y Jasmine_Byrne-01S.mp4
sudo ffmpeg -i _0000.jpg -i _0120.jpg -filter_complex xfade=transition=distance:duration=5:offset=0 distanceVideo.mp4
ss : start time. If omitted, ffmpeg will start from the beginning
FFMPEG -fflags +genpts -r 20 -i raw.h264 -c:v copy 20output.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 25 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y longguide.mp4
sudo ffmpeg -r 10 -f image2 -i _%04d.jpg  -y output1.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i /home/jack/Desktop/TEST/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/TEST/glob.mp4
FFMPEG -framerate 30 -pattern_type glob -i /home/jack/Desktop/DOCKER/deepdream/deepdream/jack/*.jpg -c:v libx264 -pix_fmt yuv420p deepdreamglob.mp4
ffmpeg -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0  -y scene3.mp4
docker run -it -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y longguide.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i 'TEST/*.jpg' -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p TEST/glob.mp4
ffmpeg -ss 00:01:00 -i latina.mp4 -t 60 -acodec copy -vcodec copy 60.mp4
FFMPEG -i paper/%04d.jpg -framerate 18 -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 20 videolonger.mp4
ffmpeg /images/%04d.jpg -loop 1 -t 5 -i "test.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
ffmpeg -framerate 10 -i _%04d.jpg -c:v libx265 -vf fps=20 -pix_fmt yuv420p -y out.mp4
ffmpeg -i %03d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 test1.mp4
ffmpeg -i /images/%04d.jpg -loop 1 -t 5 -i "testout.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm7177/ffmpeg ash 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4'
ffmpeg -i images/%04d.jpg -loop 1 -t 5 -i "test.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i $(pwd)/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p frames4.mp4
cp /home/jack/Desktop/INFO/FFMPEG/images/rhino.jpg .
ffmpeg -i LOOP.mp4 -vf "scale=3840:2160,unsharp=1x=13:ly=13:la=2.0" LOOPout.mp4
FFMPEG -i fishvid/longguide.mp4 -vf "scale=1080:-1,unsharp=lx=13:ly=13:la=2.0" 720x480out.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i ./*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y frames4.mp4
ffmpeg -i LOOPout.mp4 -vf "scale=720:480,unsharp=lx=13:ly=13:la=2.0" LOOP720x480out.mp4
ffmpeg -i JaneWild-002.mkv -vf unsharp -y JaneWild-002-sharpen.mp4
ffmpeg -framerate 10 -i %04d.jpg -c:v libx265 -vf fps=20 -pix_fmt yuv420p -y out.mp4
ffmpeg -i 60.mp4 -i palette16.png -filter_complex "paletteuse" -c:a copy out16.mp4
FFMPEG -i /fishvid/longguide.mp4 -vf "scale=720:480,unsharp=lx=13:ly=13:la=2.0" 720x480out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i /home/jack/Desktop/TEST/%3d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/TEST/glob.mp4
docker run -it jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p guide.mp4
FFMPEG -i resultZ1.mp4 -c:v copy resultZ1.ogv
MPEG -i "FFMPEG -i paper/%04d.jpg -framerate 18 -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 20 videolonger.mp4"
cmake -D CMAKE_BUILD_TYPE=RELEASE >     -D CMAKE_INSTALL_PREFIX=/usr/local >     -D INSTALL_C_EXAMPLES=ON >     -D INSTALL_PYTHON_EXAMPLES=ON >     -D OPENCV_GENERATE_PKGCONFIG=ON >     -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules >     -D BUILD_EXAMPLES=ON -D WITH_FFMPEG=OFF ..
NOTE -i "docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %3d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p glob2.mp4
FFMPEG -i butteredlargslow.mp4 -map 0:v -c:v copy -bsf:v hevc_mp4toannexb raw.h265
ffmpeg -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB out-nodupes.mp4
ffmpeg -i output60.mp4 -vf mpdecimate -vsync vfr outdec.mp4 > out3.txt 2>&1
FFMPEG -fflags +genpts -r 10 -i raw.h264 -c:v copy 10output.mp4
ffmpeg -i output15.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][r] concat=n=2:v=1 [v]" -map "[v]" -y outputreverse.mp4
ffmpeg -framerate 1 -i _%04d.jpg -c:v libx264 -r 30 output.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i *.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p frames4.mp4
ffmpeg -i output15.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][r] [0:a]concat=n=2:v=1:[v] " -map "[v]" outputreverse.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm7177/ffmpeg ash -c 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker3.mp4'
history | grep ffmpeg  >>ffmpegcommands.list
ffmpeg -y -f x11grab -i :0.0  -pix_fmt yuv420p -c:v wmv1 desktop2.wmv -t 20 test.mp4
ffmpeg -i LOOPout.mp4 -vf "scale=720:480" LOOP-NS720x480out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -v
create a high quality video 1/2 the size of the original
ffmpeg -i out01.mkv -map 0:v -c:v copy -bsf:v h264_mp4toannexb raw.h264
ffmpeg -fflags +genpts -r 30 -i raw.h264 -c:v copy output.mp4
ffmpeg -fflags +genpts -r 60 -i raw.h264 -c:v copy output60.mp4
docker run -it --rm adilm7177/ffmpeg ash -c "ffmpeg -version"
FFMPEG -i BLEND-r30.mp4 -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=120'" ffplay
FFMPEG -i butteredlargslow.mp4 -map 0:v -c:v copy -bsf:v h264_mp4toannexb raw.h264
sudo ffmpeg -framerate 10 -i _%04d.jpg output.mp4
ffmpeg -i output15.mp4 -vf reverse:q:v=1 reversedVideo2.mp4
cat /usr/local/bin/mkvid >>ffmpeg.commands
nffmpeg: ffmpeg version N-106486-g451300d0e8 Copyright (c) 2000-2022 the FFmpeg developers
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch 
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y longguide.mp4
sudo ffmpeg -framerate 5 -i _%04d.jpg -vf "framerate=fps=30:interp_start=50:interp_end=200:scene=100" -y 50-200test.mp4
sudo ffmpeg -framerate 10 -i 0_%04d.jpg -vf fps=20 -pix_fmt yuv420p -y out.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p -y vid-from-images.mp4
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,smartblur=lr=1.5:ls=-0.25:lt=-3.5:cr=0.75:cs=0.250:ct=0.5" -y Jasmine_Byrne-01S.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg -i output60.mp4 -y scene3.mkv
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i 4%d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
docker run -v $(pwd):$(pwd) -w $(pwd)        jrottenberg/ffmpeg:3.2-scratch -stats         -i original.gif         original-converted.mp4
ffmpeg -r 5 -i %03d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 25 -y test1.mp4
FFMPEG -fflags +genpts -r 15 -i raw.h264 -c:v copy 15output.mp4
ffmpeg /images/%04d.jpg -loop 1 -t 5 -i "testout.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest --version
FFMPEG -i paper/%04d.jpg -framerate 20 -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 24 video.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -vf scale=1366:768,setdar=16:9 -c:v wmv1 desktop2.wmv
FFMPEG -i paper/%04d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 25 -i %3d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p glob25.mp4
FFMPEG -i ./butterflow/out.mp4 -vf "scale=1080:-1,unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5unsharp=1x=13:ly=13:la=2.0" ./butterflow/large.mp4
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
docker run -it --name ffmpeg adiii717/ffmpeg ash -c "node -v"
ffmpeg -ss 00:01:00 -i Latina.mp4 -t 60 -acodec copy -vcodec copy 60.mp4
FFMPEG -i ./butterflow/out.mp4 -vf "scale=1080:-1,unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5" -y ./butterflow/large.mp4
ffmpeg -v warning -f x11grab -video_size 1366x768 -r 30000/1001 -i :0.0  -vcodec libx264 -pix_fmt yuv420p -s 1280x720 -y output.mp4
ffmpeg -i output15.mp4 -q:v 1 -vf reverse reversedVideo2.mp4
ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i hw:0 output.mkv
ffmpeg -framerate 30 -pattern_type glob -i 'TEST/*.jpg' -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p TEST/glob.mp4
ffmpeg -framerate 10 -i 0_%04d.jpg -c:v libx264 -vf fps=20 -pix_fmt yuv420p -y out.mp4
NOTE -i "sudo ffmpeg -r 10 -f image2 -i _%04d.jpg  output1.mp4
ffmpeg -y -f x11grab -i :0.0 -codec:v libx265 -pix_fmt yuv420p -t 20 test.mp4
docker run adiii717/ffmpeg ffmpeg 
ffmpeg -i output15.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][0:a][r] [0:a]concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" outputreverse.mp4
ffmpeg -i 60.mp4 -vf palettegen16 palette.png
ffmpeg -r 1 -i tmp/000.jpg -vf untile=1x25 movie.mkv
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y ufadiiiDocker.mp4
sudo ffmpeg -r 10 -f image2 -i _%04d.jpg  -y output2.mp4
FFMPEG -i paper/%04d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS,pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -version
sudo ffmpeg -framerate 5 -i _%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" -y test.mp4
ffmpeg -i JaneWild-002.mkv -vf unsharp -y JaneWild-002-sharpen.mkv
ffmpeg -i output15.mp4 -vf reverse:-q:v 1 reversedVideo2.mp4
docker run -i --rm -u $UID:$GROUPS -v "$PWD:$PWD" -w "$PWD" mwader/static-ffmpeg:5.0.1-3 -i adiiiDocker.mp4 static.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) -framerate 30 adiii717/ffmpeg:latest -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -qscale 3 -vf scale=1366:768,setdar=4:3 -c:v wmv1 desktop.wmv
ffmpeg -framerate 10 -i frames/%04d.jpg -c:v libx264 -vf fps=20 -pix_fmt yuv420p -y out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i output60.mp4 -y scene3.mkv
ffmpeg -i %0d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 test1.mp4
ffmpeg -i 3%d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 test1.mp4
echo "ffmpeg -ss 00:05:00 -i $1 -acodec copy -vcodec copy new$1">>shorten
ffmpeg -i output15.mp4 -vf reverse reversedVideo.mp4
ffmpeg -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0  scene3.mp4
ffmpeg -r 1 -i 000.jpg -vf untile=1x25 movie.mkv
ffmpeg -i 60.mp4 -vf palettegen,colors=16 palette16.png
FFMPEG -i $(pwd)/butterflow/butteredlong.mp4 -vf "scale=740:-1,unsharp=5:5:2" $(pwd)/butterflow/butteredoutS740.mp4
ffmpeg -i images/%04d.jpg -loop 1 -t 5 -i "testout.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" test.mp4
ffmpeg -r 1 -i tmp/0000.jpg -vf untile=1x25 movie.mkv
ffmpeg:  ffmpeg version N-106927-ge6f0cec880 Copyright (c) 2000-2022 the FFmpeg developers
ffmpeg -ss 00:04:00 -i 19yo_petite_latina.mp4 -t 25 short.mp4
ffmpeg -i /images/0001.jpg -loop 1 -t 5 -i "testout.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -prese>
history |grep FFMPEG >> ffmpeg.history
FFMPEG -i 'images/*.jpg' -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -vf scale=1366:768,setdar=1:1 -c:v wmv1 desktop2.wmv
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i /home/jack/Desktop/DOCKER/deepdream/frames4/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/TEST/frames4.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm1177/ffmpeg ash 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4'
FFMPEG -i BLEND-r30.mp4 -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=120'" output-BLEND-r30.mkv
cat images/*.jpg | FFMPEG -f image2pipe -r 15 -c:v mjpeg -i - -c:v copy -f matroska - | ffplay -
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i /home/jack/Desktop/frames4/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/frames4/frames4.mp4
FFMPEG:  ffmpeg version 5.0.1 Copyright (c) 2000-2022 the FFmpeg developers
display /home/jack/Desktop/INFO/FFMPEG/images/rhino.jpg
FFMPEG -i 'paper/*.jpg' -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4
history | grep "ffmpeg" >>ffmpeg.commands
ffmpeg -i output15.mp4 -vf reverse:q:v 1 reversedVideo2.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
ffmpeg -i scene.mkv -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0  scene3.mp4
docker run -it --rm adilm7177/ffmpeg ash -c 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4'
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharp=3:3:1.5" -y Jasmine_Byrne-01S.mp4
docker run -it --rm adiii717/ffmpeg ash -c 
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
FFMPEG -i ./butterflow/out.mp4 -vf "scale=1080:980,unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5" -y ./butterflow/large.mp4
FFMPEG -i $(pwd)/butterflow/butteredlong.mp4 -vf "scale=740:-1,unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5" $(pwd)/butterflow/butteredoutS740.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v h264 -r 30 -y vid-from-images.mp4
FFMPEG -i fishvid/longguide.mp4 -vf "scale=-1:720,unsharp=lx=13:ly=13:la=2.0" xxx720.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2":reverse -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y RufadiiiDocker.mp4
ffmpeg -y -f x11grab -i :0.0  -pix_fmt yuv420p -c:v wmv1 -t 10 desktop5.wmv
ffmpeg -fflags +genpts -r 20 -i raw.h264 -c:v copy output.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch  -f x11grab -i :0.0  -framerate 25 -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p desktop.mp4
ffmpeg -video_size 1024x768 -framerate 25 -f x11grab -i :0.0+100,200 -f pulse -ac 2 -i default output.mkv
history |grep ffmpeg >> ffmpeg.history
FFMPEG -framerate 30 -pattern_type glob -i /home/jack/Desktop/DOCKER/deepdream/deepdream/jack/%d.jpg -c:v libx264 -pix_fmt yuv420p deepdreamglob.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p vid-from-images.mp4
SCRIPTS i `docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch  -f x11grab -i :0.0  -framerate 25 -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p desktop.mp4
FFMPEG -i butteredlargeslow.mp4 -map 0:v -c:v copy -bsf:v h264_mp4toannexb raw.h264
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://underpop.online.fr/f/ffmpeg/ffmpeg-all.html.gz
FFMPEG -i %04d.jpg -qscale:v 1 test.MOV 
ffmpeg -i test.mp4 -filter:v "setpts=40*PTS,minterpolate='fps=25:scd=none:me_mode=bidir:vsbmc=1:search_param=400'" -y output.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -qscale 3 -s 1366x768 -c:v wmv1 desktop.wmv
ffmpeg -i 60.mp4 -vf palettegen=max_colors=16 palette16.png
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i images/%4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
FFMPEG -i butteredlargslow.mp4 -c:v copy -bsf hevc_mp4toannexb-f hevc  out.h265
ffmpeg -framerate 10 -i _%04d.jpg output.mp4
ffmpeg -i longguide.mp4 -map 0:v -c:v copy -bsf:v h264_mp4toannexb raw.h264
ffmpeg LOOP.mp4 -vf "scale=3840:2160,unsharp=1x=13:ly=13:la=2.0" LOOPout.mp4
FFMPEG -i resultZ1.mp4 resultZ1.ogv
sudo ln -s /home/jack/Desktop/FFMPEG/gifblender /usr/local/bin/gifblender
ffmpeg -framerate 2 -i _%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" test.mp4
cat /home/jack/Desktop/DOCKER/deepdream/deepdream/jack/*.jpg | FFMPEG -f image2pipe -i - deepdream.mp4
FFMPEG -i fishvid/longguide.mp4 -vf "scale=720:480,unsharp=lx=13:ly=13:la=2.0" 720x480out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm7177/ffmpeg ash -c 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4'
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i *.png -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y frames4.mp4
FFMPEG -i $(pwd)/butterflow/butteredlong.mp4 -vf "scale=740:-1,pad=ceil(iw/2)*2:ceil(ih/2)*2,unsharp=5:5:2" $(pwd)/butterflow/butteredoutS740.mp4
ffmpeg -framerate 30 -pattern_type glob -i '*hybridCNN.jpg' -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p hybridCNN.mp4
FFMPEG -i FishDream.mp4 FishDreamout.mp4
sudo ffmpeg -framerate 5 -i _%04d.jpg -vf "framerate=fps=30:interp_start=0:interp_end=255:scene=100" -y 0-255test.mp4
ffmpeg -i 60.mp4 -vf "palettegen:colors=16" palette16.png
ffmpeg -i %04d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 test1.mp4
ffmpeg -i _%04d.jpg -filter_complex xfade=transition=distance:duration=5:offset=0 distanceVideo.mp4
FFMPEG butterflow/out.mp4 -vf "scale=1080:-1,unsharp=1x=13:ly=13"la=2.0" butterflow/large.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch ffmpeg -framerate 30 -pattern_type glob -i /home/jack/Desktop/TEST/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p /home/jack/Desktop/TEST/glob.mp4
ffmpeg -i JaneWild-002.mkv -vf unsharp=3:3:1.5 -y JaneWild-002-sharpen.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -vf scale=1366:768,setdar=4:3 -c:v wmv1 desktop2.wmv
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i TEST/*.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p TEST/glob.mp4
ffmpeg -r 1 -i 500.jpg -vf untile=1x25 movie.mkv
SCRIPTS i "docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch  -f x11grab -i :0.0  -framerate 25 -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p desktop.mp4"
ffmpeg -i %4d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 test1.mp4
ffmpeg -i LOOP.mp4 -vf "scale=3840:2160,unsharp=lx=13:ly=13:la=2.0" LOOPout.mp4
ffmpeg -i %03d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 10 -y test1.mp4
cat /home/jack/Desktop/DOCKER/deepdream/deepdream/jack/*.jpg | FFMPEG -f image2pipe -i - deepdreamcat.mp4
FFMPEG -i $(pwd)/butterflow/butteredlong.mp4 -vf "scale=740:-1,unsharp=1x=13:ly=13"la=2.0" $(pwd)/butterflow/butteredoutS740.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v h264 -r 30 -pix_fmt yuv420p -y vid-from-images.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v h.264 -r 30 -pix_fmt yuv420p -y vid-from-images.mp4
FFMPEG butterflow/out.mp4 -vf "scale=1080:-1,unsharp=1x=13:ly=13:la=2.0" butterflow/large.mp4
ffmpeg -framerate 2 -i images/%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" test.mp4
ffmpeg -ss 00:04:00 -i 10yo_petite_latina.mp4 -t 25 short.mp4
ffmpeg -i images/%04d.jpg -loop 1 -t 5 -i "testout.mp4" -filter_complex "[0:v]concat=n=1:v=1:a=0,format=yuv444p[v]" -map "[v]" testout.mp4
ffmpeg -framerate 30 -pattern_type glob -i *hybridCNN.jpg' -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p hybridCNN.mp4
FFMPEG -framerate 30 -pattern_type glob -i 'images/*.jpg' -c:v libx264 -pix_fmt yuv420p globout.mp4
FFMPEG -i 'jack/tmp/%04d.jpg' -vf "tblend=average,framestep=2,setpts=0.50*PTS" -r 30 -c:v libx264 -pix_fmt yuv420p BLEND-r30.mp4
FFMPEG -i ./butterflow/out.mp4 -vf "scale=1080:-1,unsharp=1x=13:ly=13:la=2.0" ./butterflow/large.mp4
ffmpeg -i _0000.jpg -i _0120.jpg -filter_complex xfade=transition=distance:duration=5:offset=0 distanceVideo.mp4
ffmpeg -i output15.mp4 -vf reverse:-q:v=1 reversedVideo2.mp4
ffmpeg -y -f x11grab -i :0.0 -codec:v libx264 -pix_fmt yuv420p -t 20 test.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm7177/ffmpeg ash -c ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker3.mp4
FFMPEG -i butteredlrgslow.mp4 -map 0:v -c:v copy -bsf:v hevc_mp4toannexb raw.h265
ffmpeg -framerate 10 -i 0_%04d.jpg -vf fps=20 -pix_fmt yuv420p -y out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adilm7177/ffmpeg ash -c 'ffmpeg -i images/%04d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker2.mp4'
ffmpeg -i JaneWild-002.mkv -vf unsharp=5:5:2 JaneWild-002-sharpen.mp4
ffmpeg -i output15.mp4 **-sameq**  -vf reverse reversedVideo2.mp4
FFMPEG -framerate 30 -pattern_type glob -i /home/jack/Desktop/DOCKER/deepdream/deepdream/jack/%0d.jpg -c:v libx264 -pix_fmt yuv420p deepdreamglob.mp4
ffmpeg -framerate 2 -i %03d.jpg -c:v libx265 -r 30 -pix_fmt yuv420p -y vid-from-images.mp4
ffmpeg -i 60.mp4 -i palette.png -filter_complex "paletteuse" -c:a copy out.mp4
docker run adiii717/ffmpeg ffmpeg -framerate 30 -pattern_type glob -i ./*.png -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y frames4.mp4
The basic format is: ffmpeg -i originalvideo.mp4 -ss 0:0:4 -t 0:1:10 -vcodec copy -acodec copy outputvideo.mp4
ffmpeg -ss 00:04:00 -i 19yo_petite_latina.mp4 -t 1500 -acodec copy -vcodec copy -t 25 25.mp4
ffmpeg -framerate 20 -i images/%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" -y test.mp4
ffmpeg -fflags +genpts -r 15 -i raw.h264 -c:v copy output15.mp4
NOTE -i "docker run -v \$(pwd):\$(pwd) -w \$(pwd) adiii717/ffmpeg:latest ffmpeg -i adiiiDocker.mp4 -q:v 1 -vf reverse reversedadiiiDocker.mp4"
FFMPEG -i fishvid/longguide.mp4 -vf "scale=1080:-1,unsharp=lx=13:ly=13:la=2.0" 1080out.mp4
FFMPEG -i ./butterflow/large.mp4 -filter:v "setpts=2.0*PTS" ./butterflow/largeslowed.mp4
ln -s /home/jack/Desktop/FFMPEG/gifblender /usr/local/bin/gifblender
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -framerate 30 -i images/%4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
docker run -it -d  -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y longguide.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %3d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p glob2.mp4
ffmpeg -i output15.mp4 -filter_complex "[0:v]reverse,fifo[r];[0:v][r] [0:a]concat=n=1:v=1:[v] " -map "[v]" outputreverse.mp4
ffmpeg -r 5 -i %03d.jpg -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4
sudo ffmpeg -r 9 -f image2 -i _%04d.jpg  -y output4.mp4
docker run -i --rm -u $UID:$GROUPS -v "$PWD:$PWD" -w "$PWD" mwader/static-ffmpeg:5.0.1-3 '-i adiiiDocker.mp4 static.mp4'
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0 scene3.mp4
ffmpeg -i paper/%04d.jpg -f 20 -vcodec libx264 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 24 video.mp4
ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f alsa -ac 2 -i hw:0 output.mkv
ffmpeg -framerate 10 -i %03d.jpg -c:v libx264 -vf fps=20 -pix_fmt yuv420p -y out.mp4
rm /home/jack/Desktop/lbry-react/FFMPEG/shotcut-linux-x86_64-220425.txz
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharp=3:3:1.5" -preset slow -y Jasmine_Byrne-01S.mp4
docker run -it -v $(pwd):$(pwd) -w $(pwd) jrottenberg/ffmpeg:3.2-scratch -framerate 30 -i %4d.jpg -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p guide.mp4
ffmpeg -f image2 -r 25 -pattern_type glob -i '*.png' -qscale 3 -s 1920x1080 -c:v wmv1 video.wmv
FFMPEG -i fishvid/longguide.mp4 -vf "scale=-1:720,unsharp=lx=13:ly=13:la=2.0" 720x480out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -i output60.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB -map:v 0 -y scene3.mp4
ffmpeg -f pulse -i alsa_input.pci-0000_00_1b.0.analog-stereo -ac 1 recording.m4a
sudo ffmpeg -framerate 5 -i _%04d.jpg -y output.mp4
ffmpeg -i Jasmine_Byrne-01.mp4 -filter:v "scale=720:-1:flags=lanczos,unsharp=lr=1.5:ls=-0.25:lt=-3.5:cr=0.75:cs=0.250:ct=0.5" -y Jasmine_Byrne-01S.mp4
ffmpeg -framerate 10 -i %04d.jpg -c:v libx264 -vf fps=20 -pix_fmt yuv420p -y out.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset slow -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDockerpresetslow.mp4
https://www.hellocatfood.com/misusing-ffmpegs-motion-interpolation-options/
ffmpeg -i Jasmine_Byrne-01.mp4 -vf unsharp=3:3:1.5 -codec:v libx264 -crf 18 -preset slow -filter_complex format=yuv420p -y Jasmine_Byrne-01S.mp4
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset ultrafast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDocker.mp4
ffmpeg -i 60.mp4 -vf palettegen colors=16 palette16.png
ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0 -f alsa -ac 2 -i hw:1 output.mkv
docker start ffmpeg ffmpeg -version
FFMPEG resultZ1.mp4 -c:v copy resultZ1.ogv
docker run -v $(pwd):$(pwd) -w $(pwd) adiii717/ffmpeg:latest ffmpeg -framerate 30 -i %4d.jpg -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -preset fast -qp 0 -r 30 -pix_fmt yuv420p -y adiiiDockerpresetslow.mp4
MPEG -i "FFMPEG -i paper/%04d.jpg -vf "tblend=average,framestep=2,setpts=0.50*PTS,pad=ceil(iw/2)*2:ceil(ih/2)*2" -r 15 -c:v libx264 -pix_fmt yuv420p BLEND.mp4 
ffmpeg -r 1 -i temp/000.jpg -vf untile=1x25 movie.mkv
ffmpeg -r 1 -i 0.jpg -vf untile=1x25 movie.mkv
sudo ffmpeg -framerate 2 -i _%04d.jpg -vf "framerate=fps=30:interp_start=64:interp_end=192:scene=100" test.mp4
"""

import ffmpeghistory
print(dir(ffmpeghistory))
data=ffmpeghistory()

nodups = set()
NODUPES = []
STRING = STRINGS.split("\n")
print(len(STRING))
for line in STRING:
    nodups.add(line)
    NODUPES.append(line)
print(len(nodups))
    

print(NODUPES[12])

term =input("Search Term: ")
for line in NODUPES:
    if term in line:
        print(line)

import numpy as np

with np.load('/home/jack/Desktop/HDD500/TARS/saved-arr.npy') as data:
     print(data[30:])

print (a[30:])

