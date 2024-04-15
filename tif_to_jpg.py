import os
from PIL import Image

class tif_to_jpg:
    def tif_to_jpg(self,file_name):
        img = Image.open(file_name)
        count = img.n_frames
        for i in range(count):
            img.seek(i)
            img.save(str(i)+'.jpg')

if __name__ == '__main__':
    tif_to_jpg_object = tif_to_jpg()
    file_path = 'C:\\Users\\Patterns\\PycharmProjects\\pythonProject1\\Dexter'
    for file in os.listdir(file_path):
        if file.endswith('.tif'):
            tif_to_jpg_object.tif_to_jpg(file)


