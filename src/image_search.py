import os
import cv2
import csv
import argparse

from pathlib import Path

def validate_image(image_name, target_name):
    image

def create_histogram_color(image, normalize_func = cv2.NORM_MINMAX):
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0])
    plt.plot(histogram)


def main(target_path, collection_path, output_path):
    



    


if __name__ == '__main__':
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument('target_path', help='A path to the image you want compared to a collection')
    a_parser.add_argument('collection_path', help='A path to the collection of images to want compare to the target image')
    a_parser.add_argument('output_path', default='./',help='A path to the directory you want the output file placed in')
    args = a_parser.parse_args()

    main(args.target_path, args.collection_path, args.output_path)