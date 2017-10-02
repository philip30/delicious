#!/usr/bin/env python3

import os
import sys
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--inp_directory", type=str, nargs="+")
parser.add_argument("--output_directory", type=str)
args = parser.parse_args()

if not os.path.exists(args.output_directory):
  os.makedirs(args.output_directory)

for i, directory in enumerate(args.inp_directory):
  for j, inp_file in enumerate(os.listdir(directory)):
    orig_file = os.path.join(directory, inp_file)
    extension = inp_file.split(".")[-1]
    dest_name = "%d_%s-%d.%s" % (i, os.path.basename(directory), j, extension)
    dest_file = os.path.join(args.output_directory, dest_name)
    print("Copying %s to %s" % (orig_file, dest_file))
    shutil.copyfile(orig_file, dest_file)

