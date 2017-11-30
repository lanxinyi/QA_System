# -*- coding: utf-8 -*-
import os
import uuid

class IO_Date(object):
    def __init__(self, fi_name):
        self.filename = fi_name

    @staticmethod
    def file_exist(fi_name):
        if not os.path.exists(fi_name):
            print('file %s does not exist' % fi_name)
            raise Exception

    @staticmethod
    def get_temp_file_name():
        return "temp_%s" % str(uuid.uuid4().hex)

    def read_file(self):
        self.file_exist(self.filename)

        with open(self.filename, 'r', encoding='utf-8') as in_f:
            lines = in_f.readlines()
            lines = [line.strip() for line in lines]

        return lines

    def write_file(self, data):
        with open(self.filename, 'w', encoding='utf-8') as out_f:
            for line in data:
                out_f.write(line + '\n')
