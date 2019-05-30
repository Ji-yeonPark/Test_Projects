#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import sys
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')

errors = []
rootDir = ''
exts = ['.mov', '.avi', '.wmv']

for (root, dirs, files) in os.walk(unicode(rootDir)):

    print '--root : %s' % root

    os.chdir(root)
    for filename in files:
        ext = os.path.splitext(filename)[-1].lower()

        name = os.path.splitext(filename)[0]
        if ext in exts:
            path = '%s/%s' % (root, filename)

            # change extension to mp4
            new_filename = name + '.mp4'
            new_path = '%s/%s' % (root, new_filename)
            print '"%s" to "%s"' % (path, new_path)

            # Do ffmpeg
            p = subprocess.Popen([
                'ffmpeg',
                '-y',
                '-i',
                filename,
                '-qscale',
                '0',
                new_filename,
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, msg = p.communicate()

            # Add full path of file if Occured `ffmpeg Error`
            if msg.find('Error') > -1:
                errors.append(path)

if errors:
    print '-' * 100 + 'ERROR' + '-' * 100

    for file in errors:
        print file
