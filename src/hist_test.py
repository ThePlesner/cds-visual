# We need to include the home directory in our path, so we can read in our own module.
import os
import sys
sys.path.append(os.path.join(".."))
import cv2
import numpy as np
from utils.imutils import jimshow
from utils.imutils import jimshow_channel
import matplotlib.pyplot as plt
from pathlib import Path

# point to image dir
image_dir = os.path.join("..", "data", "img")

def plot_histogram(image, title, mask=None):
    # split channels
    channels = cv2.split(image)
    # names of colours
    colors = ("b", "g", "r")
    # create plot
    plt.figure()
    # add title
    plt.title(title)
    # Add xlabel
    plt.xlabel("Bins")
    # Add ylabel
    plt.ylabel("# of Pixels")

    # for every tuple of channel, colour
    for (channel, color) in zip(channels, colors):
        # Create a histogram
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        # Plot histogram
        plt.plot(hist, color=color)
        # Set limits of x-axis
        plt.xlim([0, 256])
    # Show plot
    plt.show()

# Iterate over files
for image in Path(image_dir).glob("*.png"):
    #cv2 and pathlib don't play nicely
    image_path = str(image)
    # read image
    image = cv2.imread(image_path)
    # Get image name from image_path
    _, image_name = os.path.split(image_path)
    # output plot
    plot_histogram(image, image_name)