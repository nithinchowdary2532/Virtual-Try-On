# -*- coding: utf-8 -*-
"""Hackathon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17smfp1ePHT3TS62v6ubj_L5caepmTU9w
"""

# Commented out IPython magic to ensure Python compatibility.
# Clone the repository
!git clone https://github.com/shadow2496/VITON-HD.git

# Change directory to the project folder
# %cd VITON-HD/

!wget https://repo.continuum.io/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh && bash Miniconda3-py38_4.10.3-Linux-x86_64.sh -bfp /usr/local

!conda update conda -y -q
!source /usr/local/etc/profile.d/conda.sh
!conda init bash

import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
!conda --version

!conda create -y -n viton python=3.8
!conda activate viton
!conda install -y pytorch torchvision cudatoolkit -c pytorch
!pip install opencv-python torchgeometry

from google.colab import files

uploaded_dataset = files.upload()
!unzip -q -d datasets/ datasets.zip
!rm dataset.zip

# Manually upload the checkpoints file to the 'checkpoints' folder
from google.colab import drive

# Mount Google Drive to access files
drive.mount('/content/drive')

# Specify the path to the checkpoints file on Google Drive
drive_path = "/content/drive/MyDrive/checkpoints/checkpoints.zip"

# Copy the file from Google Drive to the 'checkpoints' folder in Colab
!cp "$drive_path" checkpoints/

# Unzip the checkpoints file
!unzip -q -d checkpoints/ checkpoints/checkpoints.zip

import zipfile
import os

# Specify the path to the zip file
zip_file_path = '/content/VITON-HD/datasets/test.zip'

# Specify the directory to extract the contents
extract_path = '/content/VITON-HD/datasets/'

# Open the zip file and extract its contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

from PIL import Image
import matplotlib.pyplot as plt

def imageMaskPreprocess(imageName) :
  image_path  = "/content/VITON-HD/datasets/test/cloth-mask/" + imageName + ".png"
  image = Image.open(image_path)
  import numpy as np
  image_resized = image.resize((768, 1024))
  image_array = np.array(image_resized)
  print(image_array.shape)
#reshape = np.reshape(image_array , (1024 , 768))
  plt.imshow(image_array)
  plt.show()

  updated_image_path = "/content/VITON-HD/datasets/test/cloth-mask/" + imageName + ".jpg"
  updated_image = Image.fromarray(image_array.astype(np.uint8))
  updated_image.save(updated_image_path)

def imagePreprocess(imageName) :
  image_path  = "/content/VITON-HD/datasets/test/cloth/" + imageName + ".jpg"
  image = Image.open(image_path)
  import numpy as np

  image_resized = image.resize((768, 1024))
  image_array = np.array(image_resized)

  print(image_array.shape)
  #reshape = np.reshape(image_array , (1024 , 768))
  plt.imshow(image_array)
  plt.show()


  updated_image_path = "/content/VITON-HD/datasets/test/cloth/" + imageName + ".jpg"
  updated_image = Image.fromarray(image_array.astype(np.uint8))
  updated_image.save(updated_image_path)

from google.colab import files

uploaded = files.upload()

def addImages(imageName):
  imageMaskPreprocess(imageName)
  imagePreprocess(imageName)

imagePreprocess("shirt3")

def imageMaskPreprocess2(imageName) :
  image_path  = "/content/VITON-HD/datasets/test/cloth-mask/" + imageName
  image = Image.open(image_path)
  import numpy as np
  image_resized = image.resize((768, 1024))
  image_array = np.array(image_resized)
  grayscale_image = np.mean(image_array, axis=-1, dtype=int)
  print(grayscale_image.shape)
#reshape = np.reshape(image_array , (1024 , 768))
  plt.imshow(grayscale_image)
  plt.show()

  updated_image_path = "/content/VITON-HD/datasets/test/cloth-mask/" + imageName
  updated_image = Image.fromarray(grayscale_image.astype(np.uint8))
  updated_image.save(updated_image_path)
imageMaskPreprocess2("pineapple.jpg")

addImages("pineapple")

# Commented out IPython magic to ensure Python compatibility.
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# %run test.py --name my_test_run





!jupyter nbconvert --to script Hackathon.ipynb
