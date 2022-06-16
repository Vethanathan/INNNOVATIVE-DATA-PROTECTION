# Python program to demonstrate
# image steganography using OpenCV


import cv2
import numpy as np
import random
import tkinter
import tkinter.messagebox
import customtkinter


# Encryption function
def encrypt(image1,image2):
	# image1="pic1.jpg"
	# image2="pic2.jpg"
	
	# img1 and img2 are the
	# two input images
	img1 = cv2.imread(image1)
	img2 = cv2.imread(image2)
	
	for i in range(img2.shape[0]):
		for j in range(img2.shape[1]):
			for l in range(3):
				
				# v1 and v2 are 8-bit pixel values
				# of img1 and img2 respectively
				v1 = format(img1[i][j][l], '08b')
				v2 = format(img2[i][j][l], '08b')
				
				# Taking 4 MSBs of each image
				v3 = v1[:4] + v2[:4]
				
				img1[i][j][l]= int(v3, 2)
				
	cv2.imwrite('final.png', img1)
	tkinter.messagebox.showinfo("Successfull" "sucess")

	
# Decryption function
def decrypt(final):
	# final = "final.png"
	# Encrypted image
	img = cv2.imread(final)
	width = img.shape[0]
	height = img.shape[1]
	
	# img1 and img2 are two blank images
	img1 = np.zeros((width, height, 3), np.uint8)
	img2 = np.zeros((width, height, 3), np.uint8)
	
	for i in range(width):
		for j in range(height):
			for l in range(3):
				v1 = format(img[i][j][l], '08b')
				v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
				v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
				
				# Appending data to img1 and img2
				img1[i][j][l]= int(v2, 2)
				img2[i][j][l]= int(v3, 2)
	
	# These are two images produced from
	# the encrypted image
	cv2.imwrite('pic2_re.png', img1)
	cv2.imwrite('pic3_re.png', img2)
	
	
# Driver's code

