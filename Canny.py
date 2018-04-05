#image resizer
import cv2
#import matplotlib.pyplot as plt
#import numpy as np
import glob
import os

product = []
counter = 0
images_list_input = glob.glob('Test_Data/*.jpg')
path = "~/PycharmProjects/CSV_Maker/Output_Data_non_Living"
for i in images_list_input:
    counter = counter + 1
    print(i)
    im = cv2.imread(i)
    resized_image = cv2.resize(im, (64, 64))
    edges = cv2.Canny(resized_image, 150, 250)
    print(edges)
    file_name = 'gray_list2_nonface' + str(counter) + '.jpg'
    cv2.imwrite(os.path.join(path, file_name), edges)
#print(np.shape(list(edges.flatten())))