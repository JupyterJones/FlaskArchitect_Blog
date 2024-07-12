#!/home/jack/miniconda3/envs/cloned_base/bin/python
import sys
sys.path.append('/home/jack/hidden')
def gettext():
   from randtext import randTXT
   STR = randTXT()
   return STR
print(gettext())
