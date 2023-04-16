import cv2
import numpy as np
import os
# Load the npz file
npzfile = np.load('Dataset/CDY_2015.npz')
ls=npzfile.files
temp=npzfile[ls[0]]
# Convert the contours to bounding boxes and normalize the coordinates
bounding_boxes = []
print(temp.shape)
for i in range(temp.shape[2]):
    class_index = 0

    # Load the numpy array with grape pixels
    grape_array = temp[:,:,i]

    # Convert the grape array to a binary image
    grape_image = (grape_array == 1).astype(np.uint8) * 255

    # Find the contours of the grape regions
    contours, hierarchy = cv2.findContours(grape_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        x_center = (x + w/2) / grape_image.shape[1]
        y_center = (y + h/2) / grape_image.shape[0]
        width = w / grape_image.shape[1]
        height = h / grape_image.shape[0]
        bounding_boxes.append((x_center, y_center, width, height))
# for arr in temp:
#     for i in arr:
#         if(i==0):
#             print('.',end="")
#         else:
#             print('-',end="")

#     print('|')   

# Define the class index for grape


# Write the bounding boxes to a YOLOv7 format text file
with open('grape_bounding_boxes.txt', 'w') as f:
    for bbox in bounding_boxes:
        bbox_str = ' '.join([str(class_index), str(bbox[0]), str(bbox[1]), str(bbox[2]), str(bbox[3])])
        f.write(bbox_str + '\n')
 
# print(npzfile.shape)
# # Extract the image array
# img_array = npzfile['arr_0']

# # Convert the array to an image
# img_cv2 = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

# # Save the image to disk
# cv2.imwrite('output.jpg', img_cv2)
