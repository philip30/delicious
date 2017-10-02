# Philip Arthur
# 1st October 2017

import os
import sys
import numpy
import imread

class ImageReader(object):
  def parse_data(self, directory):
    data = []
    imgs = set()
    for inp_file in os.listdir(directory):
      full_path = os.path.join(directory, inp_file)
      data.append(self.read_image(full_path))
      imgs.add(inp_file.split("_")[0])
    return data, len(imgs)

  def read_image(self, path):
    print("Reading: %s" % (path), file=sys.stderr)
    rgb = imread.imread(path)
    rgb = numpy.swapaxes(rgb, 0, 2)
    rgb = rgb[0] * (256 ** 2) + rgb[1] * 256 + rgb[2]
    return numpy.swapaxes(rgb, 0, 1)

