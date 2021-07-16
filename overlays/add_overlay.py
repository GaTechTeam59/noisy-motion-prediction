import cv2 #Requires opencv-contrib-python==4.1.2.30
import os
import random

def add_overlay(filename,overlay_type, opacity=1, blur=0, write=False):
	#Load videos
	vidcap_sample = cv2.VideoCapture("samples/"+filename)
	vidcap_overlay = cv2.VideoCapture("overlays/overlay_"+overlay_type+".mp4")
	
	success_sample,image_sample = vidcap_sample.read()
	success_overlay,image_overlay = vidcap_overlay.read()
	
	#Save video if used for testing purposes.
	outshape = (image_sample.shape[1], image_sample.shape[0])
	if write: out_video = cv2.VideoWriter("output_videos/output_"+filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, outshape)
	
	#This selects a random overlay frame to start with.
	skip_frames = random.randint(0,30);
	for i in range(skip_frames):
		success_overlay,image_overlay = vidcap_overlay.read()
	
	#Iterate through every frame and apply the overlay to the current frame.
	while True:
		if success_overlay and success_sample:
	
			#Resize the overlay image to fit the sample.
			this_shape = (image_sample.shape[1], image_sample.shape[0])
			image_overlay = cv2.resize(image_overlay, this_shape, interpolation = cv2.INTER_AREA)

			#Adds the overlay with an opacity to the sample image.
			#Opacity of 0 means the overlay is invisible.
			#Opacity over 1 amplifies the overlay.
			new_img = cv2.addWeighted(image_sample,1,image_overlay,opacity,0)
			
			#Example of how gaussian blur is applied.  the blur size must be an odd integer.
			if blur > 0: new_img = cv2.GaussianBlur(new_img,(blur,blur),cv2.BORDER_DEFAULT)

			if write: out_video.write(new_img)
			
			#Iterate to the next frame.
			success_sample,image_sample = vidcap_sample.read()
			success_overlay,image_overlay = vidcap_overlay.read()
		else: break;
		
	#Save the output video.
	if write: out_video.release();
	
#This creates a test video fore each of the six overlays and a 7th that creates a gaussian blur.
def test_overlays(show=False):
	files = os.listdir("samples");
	overlays = ["lights","snow","snow","fog","rain","fire","grunge"]
	opacities = [0.5,0,1,1,1,5,1]
	blurs = [0,15,0,0,0,0,0]
	
	for i in range(len(files)):
		if show: print(files[i]);
		add_overlay(files[i],overlays[i],opacity=opacities[i],blur=blurs[i],write=True);
	
	
test_overlays(show=True);

	
