import cv2
import numpy as np
import glob
import os
import csv

product = []
counter = 0
images_list_input = glob.glob('Output_Data/*.jpg')
path = "/home/darkdragon/PycharmProjects/CSV_Maker/"
file_name = "Output_images.csv"

with open(file_name, 'a') as file_open:
    for images in images_list_input:
        im = cv2.imread(images)
        b = im.flatten()
        list_4096 = list(b)
        for n, i in enumerate(list_4096):
            if i >= 10:
                list_4096[n] = 1
            else:
                list_4096[n] = 0
        list_4096.append('0')
        print(list_4096)

        wr = csv.writer(file_open, quoting = csv.QUOTE_ALL)
        wr.writerow(list_4096)



