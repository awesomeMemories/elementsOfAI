#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# generate a 30-by-50 array of random numbers
x = np.random.rand(30,50)
# The following code that will plot the numbers as colors would normally
# be hidden from you, so again, you won't have to worry about it.

plt.figure(figsize=(3,5))
plt.axis('off')

#The 'imshow' method is used to display images in a plot.
#Data is represented as a 2D array.
#First argument: Array of image data
#Then a numbers of optional argumetns that control the appearance of the plot

#Second argument:
#The cmap argument in Matplotlib's imshow method is used to specify the colormap that should be
#used to map the pixel values in the image to colors. A colormap is a mapping of data values to
#colors, where each color represents a specific range of values.
#
#The cmap argument in imshow is a powerful tool for customizing the appearance of your images, 
#and can be used to create a wide range of visualizations.

plt.imshow(x, cmap='Set3')

#The next code is to see the plot 
plt.show()
