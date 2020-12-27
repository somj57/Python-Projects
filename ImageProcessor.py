import sys
import os
from PIL import Image

DIRECTORY = r"DIRECTORY_NAME"
if not os.path.exists("output_folder"):
	os.makedirs("output_folder")
output_folder = "output_folder/"

i = 1

for subfolder in os.listdir(DIRECTORY):
	path = os.path.join(DIRECTORY, subfolder)
	print(path)
	for img in os.listdir(path):
		img_path = os.path.join(path, img)
		image  = Image.open(f'{img_path}')
		clean_name = os.path.splitext(img)[0]
		image.save(f'{output_folder}{i}.png','png')
		i = i+1
		print(i)