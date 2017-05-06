#!/usr/bin/python

import sys
import getopt
import os
#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#from xml.etree import ElementTree
#from xml.dom import minidom
from xmlinstrument import getxmlinstrument

def main(argv):
    help_text = 'generate_kit.py -p <sample dir path> -e <sample file extension>'
    sample_path = ''
    sample_ext = ''
    try:
        opts, args = getopt.getopt(argv, "hp:e:", ["path=", "extension="])
        #print args
        #print opts
    except getopt.GetoptError:
        print help_text
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_text
            sys.exit()
        elif opt in ("-p", "--path"):
            sample_path = arg
        elif opt in ("-e", "--extension"):
            sample_ext = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile

    if not sample_path.endswith('/'):
        sample_path = sample_path + "/"

    #print 'Create drumkit from ' + samplePath + sampleExt
    #print len(args)
    #print len(opts)

    file_list = []

    #TODO: check directory existence
    for sample_file in sorted(os.listdir(sample_path)):
        if sample_file.endswith(sample_ext):
            #print samplePath+  sampleFile
            file_list.append(sample_file)

    print getxmlinstrument(sample_path.split('/')[-2], file_list)

if __name__ == "__main__":
    main(sys.argv[1:])
