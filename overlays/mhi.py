import cv2;
import numpy as np;
import os;
import joblib
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,plot_confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import KFold
import math;
import matplotlib.pyplot as plt

def warn(*args, **kwargs):
	pass
import warnings
warnings.warn = warn


folders_pics = ['cartwheel_pics','climb_pics','dive_pics','kick_pics','pullup_pics', 'run_pics', 'sit_pics', 'situp_pics', 'somersault_pics', 'stand_pics','cartwheel_overlay_pics','climb_overlay_pics','dive_overlay_pics','kick_overlay_pics','pullup_overlay_pics', 'run_overlay_pics', 'sit_overlay_pics', 'situp_overlay_pics', 'somersault_overlay_pics', 'stand_overlay_pics']


folders = ['cartwheel', 'climb', 'dive', 'kick', 'pullup', 'run', 'sit', 'situp', 'somersault', 'stand', 'cartwheel_overlay', 'climb_overlay', 'dive_overlay', 'kick_overlay', 'pullup_overlay', 'run_overlay', 'sit_overlay', 'situp_overlay', 'somersault_overlay', 'stand_overlay']
	
	
def get_video_mhi(video,size,decay):
	threshold_min = 40;
	for i in range(3):
	
		vidcap = cv2.VideoCapture(video)
		success,image = vidcap.read()
		count = 0
		
		current_image = np.copy(image)
		current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY) * 0;
		current_image = cv2.GaussianBlur(current_image, (5, 5), 3)
		
		mhi_shader = np.ones(current_image.shape) / 3;
		all_mhi_images = [];
		mhi_image = np.copy(current_image)
		
		
		while success:
			temp_image = np.copy(image);
			temp_image = cv2.cvtColor(temp_image, cv2.COLOR_BGR2GRAY);

			#This reduces noise.
			temp_image = cv2.medianBlur(temp_image,7)

			if count > 1:
				this_img = cv2.absdiff(temp_image, current_image);
				ret,this_img = cv2.threshold(this_img,threshold_min,255,cv2.THRESH_BINARY)
				current_image = temp_image
				if count > 2: mhi_image = cv2.add(cv2.subtract(mhi_image,decay), this_img);

			success,image = vidcap.read()

			count += 1
			if count > 1: all_mhi_images.append(mhi_image)
		
		#For some videos, the subject exists the scene long before the video ends.  To prevent an empty MHI image,
		#find the local maximum from the end of this list.
		best_sum = 0;
		best_image = mhi_image;
		for i in range(10,len(all_mhi_images)):
			this_sum = np.mean(all_mhi_images[i])
			if this_sum > best_sum:
				#This fixes false motion from the camera switching scenes.
				if (i > len(all_mhi_images)/2 and this_sum > best_sum*1.5) == False:
					best_sum = this_sum;
					best_image = all_mhi_images[i];

		if best_sum < 130 and best_sum > 20:
			break;
		else:
			if best_sum > 130: threshold_min *= 1.1
			if best_sum < 20: threshold_min *= 0.9
			if best_sum < 15: threshold_min *= 0.75

	outfile = video.replace('.avi','.png')
	outfile = outfile.replace("/","_pics/")

	cv2.imwrite(outfile, best_image)
	return best_image;

	
def save_images_as_csv(include_overlays=False):
	outfile_train = "";
	outfile_test = "";
	outfile_val = "";
	
	divider = 1;
	added_filename = "_overlay"
	if include_overlays == False:
		divider = 2;
		added_filename = ""
	
	for i in range(len(folders_pics)//divider):
		
		print(folders_pics[i]);
		files = os.listdir(folders_pics[i])
		
		#Iterate every file, flatten the image, and add to an outfile;
		for j in range(len(files)):
			filename = folders_pics[i] + "/" + files[j];
			
			#Read in and modify image.
			image = cv2.imread(filename);
			image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
			image = cv2.resize(image, (40, 30), interpolation = cv2.INTER_AREA)

			#Flatten image
			flattened = str(list(np.array(image).flatten()));
			flattened = flattened.replace("[","")
			flattened = flattened.replace("]","")
			#print("FLAT:",flattened);
			
			if j == 0 and i == 0:#Add headers:
				lst = list(np.array(image).flatten())
				startline = "label"
				for k in range(len(lst)):
					startline = startline + ", pixel" + str(k);
				outfile_train = startline + "\n"
				outfile_test = startline + "\n"
				outfile_val = startline + "\n"
			
			this_line = str(i%10) + ", " + flattened + "\n"
			if j < len(files)*0.75:
				outfile_train += this_line;
			else:
				if j < len(files)*0.85:
					outfile_val += this_line;
				else:
					outfile_test += this_line;
	file = open("train"+added_filename+".csv","w");
	file.write(outfile_train);
	file.close();
	
	file = open("test"+added_filename+".csv","w");
	file.write(outfile_test);
	file.close();
	
	file = open("val"+added_filename+".csv","w");
	file.write(outfile_val);
	file.close();
	
	
def get_data(size=128,decay=int(255/12)):
	for i in range(len(folders)):
		print(folders[i]);
		files = os.listdir(folders[i])
		for j in range(len(files)):
			filename = folders[i] + "/" + files[j];
			print("FILE:",filename);
			if ".avi" in files[j]:
				image = get_video_mhi(filename,size,decay);
				
	
