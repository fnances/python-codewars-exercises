import time
import os
import sys
import getopt
import argparse

from threading import Timer

print(str(sys.argv))
old_content = ""


def script():
    parser = argparse.ArgumentParser(prog='watcher')
    parser.add_argument('--file', help='Provide path to file')
    file_path = parser.parse_args().file
    cwd = os.path.join(os.getcwd(), file_path)
    file = open(cwd, 'r')
    name = file.name

    def watch_and_rerun(file):
        global old_content
        # print('Reading {0} - {1}'.format(name, cwd))
        content = file.read()
        # print('Comparing {0}'.format(name))
        if old_content != content:
            old_content = content
            print('Running script {0}'.format(name))
            os.system('python {0}'.format(cwd))

    while 1:
        watch_and_rerun(file)
        time.sleep(0.5)


try:
    script()
except KeyboardInterrupt:
    print >> sys.stderr, '\nExiting by user request.\n'
    sys.exit(0)
except:
    print('error {0}'.format(sys.exc_info()[0]))
