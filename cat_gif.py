#simple gif with python
import imageio.v3 as iio

filenames = ['foto_1_final.jpg', 'foto_2_final.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 500, loop = 0)

#write python cat_gif.py to create the gif
