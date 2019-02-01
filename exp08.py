import re
import os

logfile='/home/abual/exp/log.log'

def process_file(filename):
    f = open(filename)
    task_ctr = 0
    for line in f:
       if re.match('#task:', line):
        task_ctr = task_ctr + 1
    f.close()
    return task_ctr

def process_dir(mydir):
    directory = mydir
    for filename in os.listdir(directory):
       if filename.endswith(".txt"):
          ctr = 0
          print(os.path.join(directory, filename))
          ctr = process_file(os.path.join(directory, filename))
          print 'ctr: ', ctr
          write_to_logfile(filename+','+str(ctr))

def write_to_logfile(mystr):
    f = open(logfile,'a')
    try:
       f.write('\n')
       f.write(mystr)
       #f.write('\n')
    finally:
       f.close()
       #print 'problem happened writing to the file'
######################
#MAIN
#####################


#directory = '/home/abual/exp'
process_dir('/home/abual/exp')
#write_to_logfile('hehehehehehe')
