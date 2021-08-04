import cv2 #Requires opencv-contrib-python==4.1.2.30
import os
import random
import numpy as np

def add_overlay(foldername,filename,overlay_type, opacity=1, blur=0, write=False):
	#Load videos
	vidcap_sample = cv2.VideoCapture("serre/hmdb51_org/"+foldername+"/"+foldername+"/"+filename);
	vidcap_overlay = cv2.VideoCapture("overlays/overlay_"+overlay_type+".mp4")

	
	success_sample,image_sample = vidcap_sample.read()
	success_overlay,image_overlay = vidcap_overlay.read()
	
	#Save video if used for testing purposes.
	outshape = (image_sample.shape[1], image_sample.shape[0])
	if write: out_video = cv2.VideoWriter("hmdb_overlay/"+overlay_type+"/"+foldername+"/"+filename, cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), 30, outshape)
	
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
			
			if write: out_video.write(new_img)
			
			#Iterate to the next frame.
			success_sample,image_sample = vidcap_sample.read()
			success_overlay,image_overlay = vidcap_overlay.read()
		else: break;
		
	#Save the output video.
	if write: out_video.release();
	
#This creates a test video fore each of the six overlays and a 7th that creates a gaussian blur.
def test_overlays(show=False):
	folders = ['cartwheel', 'climb', 'dive', 'kick', 'pullup', 'run', 'sit', 'situp', 'somersault', 'stand']
	for f in range(len(folders)):
		print("FOLDER:",folders[f])
		files = os.listdir("serre/hmdb51_org/"+folders[f]+"/"+folders[f])
		overlays = ["lights","snow","fog","rain","fire","grunge"]
		
		opacity_multipliers = [0.25,0.5,0.5,0.5,4,0.4]#Some overlays are stronger than others.
		
		#Iterate every file
		for i in range(len(files)):
			if show: print(len(files)-i,"\t",files[i]);
			if ".avi" in files[i] or ".mp4" in files[i]:
				for j in range(len(overlays)):
					this_opacity = random.random() * opacity_multipliers[j]+0.25;
					add_overlay(folders[f],files[i],overlays[j],opacity=this_opacity,write=True);
test_overlays();			

