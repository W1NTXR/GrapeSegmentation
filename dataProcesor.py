import os
import shutil

dir_path = './Dataset'  # replace with the path to your directory
npz_files = []
for file in os.listdir(dir_path):
    if file.endswith('.npz'):
        npz_files.append(file)
dest=dir_path+'3'
os.makedirs(os.path.join(dest, 'image'), exist_ok=True)
os.makedirs(os.path.join(dir_path, 'annotation'), exist_ok=True)
os.makedirs(os.path.join(dest, 'mask'), exist_ok=True)

for file in npz_files:
    base_name = os.path.splitext(file)[0]
    image_file = base_name + '.jpg'
    annotation_file = base_name + '.txt'
    image_path = os.path.join(dir_path, image_file)
    annotation_path = os.path.join(dir_path, annotation_file)
    mask_path = os.path.join(dir_path, file)
    
    if os.path.isfile(image_path):
        shutil.move(image_path, os.path.join(dest, 'image'))
    if os.path.isfile(annotation_path):
        shutil.move(annotation_path, os.path.join(dir_path, 'annotation'))
    if os.path.isfile(mask_path):
        shutil.move(mask_path, os.path.join(dest, 'mask'))
