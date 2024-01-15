import os

import configparser

config = configparser.ConfigParser()

if not os.path.isfile('storage.ini'):
  config['indul'] = {'c': '0'}
else:
  config.read('storage.ini')
  if 'indul' not in config:
    config['indul'] = {'c': '0'}
  else:
    config['indul']['c'] = str(int(config['indul']['c']) + 1)

with open('storage.ini', 'w') as configfile:
  config.write(configfile)

print(config['indul']['c'])