# Author: Philip Arthur
# Sunday, October 1st 2017

import dynet
import argparse
import numpy

from delicious.reader import ImageReader

parser = argparse.ArgumentParser()
parser.add_argument("training")
parser.add_argument("--dynet-gpu", help="use GPU acceleration")
args = parser.parse_args()

# Reading in the data
reader = ImageReader()
data, num_imgs = reader.parse_data(args.training)

