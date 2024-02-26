#!/usr/bin/python3
from datetime import datetime
import sys, os

if len(sys.argv) < 2:
    print('Usage: python3 new.py <evfolyam> <cmd>')
    print('Example: python3 new.py 10 fn')
    sys.exit(1)
elif len(sys.argv) == 3:
  evfolyam = int(sys.argv[1])
  cmd = sys.argv[2]
else:
  cmd = sys.argv[1]
  evfolyam = int(datetime.now().year) - 2022 + 8

if cmd.startswith('fn'):
  path = os.path.dirname(os.path.realpath(__file__))
  dirs = [d for d in os.listdir(path) if d.startswith(str(evfolyam)) and os.path.isdir(os.path.join(path, d, 'py'))]
  if len(dirs) == 1:
    dir = dirs[0]
  dirs = os.listdir(os.path.join(path, dir, 'py', 'feladatsor'))
  new_dir = max([int(d) for d in dirs]) + 1
  os.makedirs(os.path.join(path, dir, 'py', 'feladatsor', str(new_dir)))
  os.makedirs(os.path.join(path, dir, 'py', 'feladatsor', str(new_dir), 'alap'))

  # create main.py
  with open(os.path.join(path, dir, 'py', 'feladatsor', str(new_dir), 'alap', 'main.py'), 'w') as f:
    f.write(f'# Path: prog/{dir}/py/feladatsor/{new_dir}/main.py')

  if "i" in cmd:
    # create input.txt
    with open(os.path.join(path, dir, 'py', 'feladatsor', str(new_dir), 'alap', 'input.txt'), 'w') as f:
      f.close()

  # open it in code
  os.system("code " + os.path.join(path, dir, 'py', 'feladatsor', str(new_dir), 'alap', 'main.py'))