# machineSpec; figure out a machine's specification, what hardware is here?
# This might grow to include some diagnostics, like exercise the HDD, ...
__author__ = 'dalem'

# Many current machine specifications can be found with psutil from here https://github.com/giampaolo/psutil
#TODO; how much memory
#TODO; what kind of processor
#TODO; performance whetstones counter
#TODO; ImportError: No module named psutil
#TODO; Windows. psutils needs to be installed. Gets "error: Unable to find vcvarsall.bat" and this http://stackoverflow.com/questions/6551724/how-do-i-point-easy-install-to-vcvarsall-bat has a little insight. Sounds like lots of hassle. I'm wondering what a reasonable answer is...
#TODO; Perhaps on Windows machines we boot from a Linux LiveCD then run machineSpec.py?


import os
import psutil
print "cpu times: " + str(psutil.cpu_times())
print "memory: " + str(psutil.TOTAL_PHYMEM)
print "disk: " + str(psutil.disk_usage(os.getcwd()))