import datetime
import sys

def info(*message, verbosity_level=0):
  print("[INFO]", datetime.datetime.now(), *message, file=sys.stderr)
  sys.stderr.flush()

def warning(*message, verbosity_level=0):
  print("[WARNING]", datetime.datetime.now(), *message, file=sys.stderr)
  sys.stderr.flush()

def fatal(*message, verbosity_level=0):
  print("[ERROR]", datetime.datetime.now(), *message, file=sys.stderr)
  sys.stderr.flush()
  sys.exit(1)

def fatal_if(condition, *message, verbosity_level=0):
  if condition:
    fatal(*message, verbosity_level=verbosity_level)

