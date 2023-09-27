#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img,array_to_img, img_to_array
import os
import random
import seaborn as sns
import cv2
import pytesseract


# In[6]:


# Path to your Tesseract executable (adjust the path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[7]:


# Load the image using OpenCV
image_path = 'Sunny.png'  # Replace with the path to your image
image = cv2.imread(image_path)


# In[8]:


x = load_img(image_path)
x


# In[9]:


# Check if the image was loaded successfully
if image is not None:
    # Convert the image to grayscale (optional but can improve OCR accuracy)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the image using Pytesseract
    text = pytesseract.image_to_string(gray_image)

    # Print the extracted text
    print("Extracted Text:")
    print(text)
else:
    print("Failed to load the image. Please check the file path.")


# In[ ]:




