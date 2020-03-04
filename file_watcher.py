import time
from datetime import datetime
import os
import sys
import getopt
import argparse

from threading import Timer

print(str(sys.argv))

last_modified = 0


def script():
    parser = argparse.ArgumentParser(prog='watcher')
    parser.add_argument('-f', '--file', help='Provide path to file')
    file_path = parser.parse_args().file
    cwd = os.path.join(os.getcwd(), file_path)
    last_modified = os.stat(cwd).st_mtime
    file = open(cwd, 'r')
    name = file.name

    def watch_and_rerun(file):
        global last_modified
        actual_modified = os.stat(cwd).st_mtime
        if last_modified != actual_modified:
            try:
                os.system('python {0}'.format(cwd))
                print('After script {0} - {1}'.format(name, datetime.now()))
            except:
                print('Error in script {0} - {1}'.format(name, datetime.now()))
            print('Running script {0} - last_modified: {1} actual_modified: {2}'.format(
                name, last_modified, actual_modified))
            last_modified = actual_modified
    while 1:
        time.sleep(0.5)
        watch_and_rerun(file)


try:
    script()
except KeyboardInterrupt:
    print >> sys.stderr, '\nExiting by user request.\n'
    sys.exit(0)
