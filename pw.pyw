#!/usr/bin/env python
import yaml, pyperclip, sys
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)
f = open(script_dir + '\pass_list.yml', 'r')
data = yaml.load(f, Loader=yaml.SafeLoader)
service = sys.argv[1]
account = sys.argv[2]
value = data[service][account]
pyperclip.copy(value)
