import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import mhi

if __name__ == "__main__":
	mhi.get_data(decay=int(255/30))
	
	#Use this to generate csv training files.
	mhi.save_images_as_csv(include_overlays=True);
	mhi.save_images_as_csv(include_overlays=False);
