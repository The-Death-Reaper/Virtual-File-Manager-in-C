import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# f = open('temp_img.txt', 'w')
image = list(image)
for i in image:
    for j in i:
        print(j)