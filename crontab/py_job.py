#!/usr/bin/python

import os
import datetime

# create the dir name
dtnow = datetime.datetime.now()
dir_name = str(dtnow).replace(' ', '-').replace(':', '-').replace('.', '-')

# change to the path of the python script - crontab runs elsewhere
abspath = os.path.abspath(__file__)
adname = os.path.dirname(abspath)
os.chdir(adname)

# create the dir
fin_dir = os.path.join(adname, dir_name)
os.mkdir(fin_dir)
