# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:12:21 2021

@author: Sach
"""

import os
import cv2
import requests
from imutils import paths

text_path = r"C:\Users\urls.txt"
# text_path = input("Enter_path : ")
rows = open(text_path).read().strip().split("\n")
total = 0
save_path = r"C:\Users\Dataset"

for url in rows:
	try:
		# try to download the image
		r = requests.get(url, timeout=60)
		# save the image to disk
		p = os.path.join(save_path, "Random_{}.jpg".format(str(total).zfill(5)))
		f = open(p, "wb")
		f.write(r.content)
		f.close()
		# update the counter
		print("[INFO] downloaded: {}".format(p))
		total += 1
	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(p))

for imagePath in paths.list_images(save_path):
	# initialize if the image should be deleted or not
	delete = False
	# try to load the image
	try:
		image = cv2.imread(imagePath)
		# if the image is `None` then we could not properly load it
		# from disk, so delete it
		if image is None:
			delete = True
	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Except")
		delete = True
	# check to see if the image should be deleted
	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)
