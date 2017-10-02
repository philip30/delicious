# Philip Arthur
# 1st October 2017

import os
import sys
import numpy
import imread

class DataPoint(object):
  def __init__(self, array, directory, label=None):
    self.array = array
    self.directory = directory
    self.label = label

class ImageReader(object):
  def parse_data(self, directory, is_train=True):
    data = []
    imgs = set()
    for inp_file in os.listdir(directory):
      full_path = os.path.join(directory, inp_file)
      label = int(inp_file.split("_")[0]) if is_train else None
      data.append(DataPoint(self.read_image(full_path),
                            full_path,
                            label))
      imgs.add(data[-1].label)
    return data, len(imgs)

  def read_image(self, path):
    print("Reading: %s" % (path), file=sys.stderr)
    rgb = imread.imread(path)
    rgb = numpy.swapaxes(rgb, 0, 2)
    rgb = rgb[0] * (256 ** 2) + rgb[1] * 256 + rgb[2]
    return numpy.swapaxes(rgb, 0, 1)

