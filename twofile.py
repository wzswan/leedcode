import os

file1 = raw_input('Enter file name 1')
file2 = raw_input('Enter file name 2')

os.system("cp %s %s" % (file1, file2))
