import os
import sys

direc_path = sys.argv[1]

for dirs,files in os.walk(direc_path):
  print files
  break
  print dirs
