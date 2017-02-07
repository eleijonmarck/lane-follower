import os
import urllib.request
import pickle

import matplotlib
from matplotlib.pyplot import imshow

# Get driving data

print("Run this only once, and it might take some time..")
# download of driving data from wroscoe
data_url = 'https://s3.amazonaws.com/donkey_resources/indoor_lanes.pkl'
file_path, headers = urllib.request.urlretrieve(data_url)
