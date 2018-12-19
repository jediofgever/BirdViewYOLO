"""
    Generate train.txt file which contains a list of training indices.
"""


from os import listdir
from os.path import isfile, join

# Grab all files and determine training size
path = '/home/atas/YOLO3D/data/training/calib/'
files = [f for f in listdir(path) if isfile(join(path, f))]
train_ratio = 0.85
train_size = min(6000, int(len(files) * train_ratio))

# Write to train.txt 
file = open('/home/atas/YOLO3D/data/training/train.txt', 'w') 
for i in range(train_size):
	file.write(str(i).zfill(6) + '\n')
file.close() 

