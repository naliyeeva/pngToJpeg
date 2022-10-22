from PIL import Image
import os

directory = '/Users/nazrinaliyeva/Desktop/archive/images'
counter = 0
os.chdir(directory)

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        img = Image.open(filename)
        name = 'img' + str(counter) + '.jpeg'
        rgb_im = img.convert('RGB')
        rgb_im.save('/Users/nazrinaliyeva/Desktop/dataset/' + name)
        counter += 1
        print(os.path.join(directory, filename))
        continue
    else:
        continue
