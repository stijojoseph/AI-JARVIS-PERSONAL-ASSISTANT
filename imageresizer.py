# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os


# Any results you write to the current directory are saved as output.

#import os
import cv2
W=256
path = "cats/validation/cats/"
for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        print(filename)
        oriimg = cv2.imread(path+'/'+filename)
       # height, width, depth = oriimg.shape
       # imgScale = W/width
      #  newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
        newimg = cv2.resize(oriimg,(227,227))
        cv2.imwrite(str(path+'/'+filename),newimg)        
        print('Image saved')