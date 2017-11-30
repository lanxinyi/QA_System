# -*- coding: utf-8 -*-
from data import *
from data_zh import *
import sys

def main(infilename, outfilename):
    IO_Date.file_exist(infilename)
    lastquery = ""  # delete the repeat query
    with open(infilename, 'r', encoding='utf-8') as infile:
        with open(outfilename, 'w', encoding='utf-8') as outfile:
            while True:
                line = infile.readline()
                if not line:
                    break

                line = line.strip()
                strlist = line.split('\t')
                if strlist[0] != lastquery:
                    outfile.write(Seg_Chinese_In_Sentence(strlist[0]) + '\n')
                    lastquery = strlist[0]

                outfile.write(Seg_Chinese_In_Sentence(strlist[1]) + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage : %s infilename outfilename ! " % sys.argv[0])
        exit(1)
    else:
        main(sys.argv[1], sys.argv[2])