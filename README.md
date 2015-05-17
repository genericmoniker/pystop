pystop - A Python stop-motion animation application
===================================================

Being frustrated that is difficult to get Helium Frog running anymore, I 
thought I'd try to create something myself. This is the very simple and
*early* attempt. Use at your own peril.

Installation
------------

### Additional Components ###

1. Python 2.7
2. [pygame](http://www.pygame.org/download.shtml)
3. [VideoCapture](http://videocapture.sourceforge.net/)

### Setup ###

I had to fix some code in pygame.

C:\Python27\Lib\site-packages\pygame\_camera_vidcapture.py, line 111 needs to 
be indented so that the function doesn't always return None if there isn't
a destination surface.

From the VideoCapture zip file, copy the vidcap.pyd for the Python27 
interpreter to C:\Python27\DLLs.

Operation
---------

Run pystop.py

Pick video source?

A single window shows the video source. Push the spacebar to take a frame. 
Onion skinning is supported from the previous frame.

Still images are stored in your user directory under `pystop`.

To generate a video from the stills, use ffmpeg. In the images directory:

    ffmpeg -framerate 15 -i %04d.jpg -loglevel debug video_file_name


