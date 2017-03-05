#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from utils.string_utils import string_utils

class Utilsjson(object):
    def __repr__(self):
        return self.to_json()

    def __init__(self):
        pass

    def to_dict(self):
        items = [[k, v] for k, v in self.__dict__.items()]
        itemsdict = {}
        for item in items:
            if type(item[1]) is str or type(item[1]) is int or \
                            type(item[1]) is bool or type(item[1]) is float:
                itemsdict[item[0]] = item[1]
            if type(item[1]) is list:
                listdict=[]
                for i in item[1]:
                    if type(i) is str or type(i) is int or type(i) is bool or type(i) is float:
                        listdict.append(i)
                    else:
                        listdict.append(i.toDICT())
                itemsdict[item[0]] = listdict
        return itemsdict

    def to_json(self):
        itemsdict=self.to_dict()
        return string_utils.repair_text(json.dumps(itemsdict).decode('unicode-escape').encode('utf8'))

    def to_json_file(self,path):
        json=self.to_json
        text_file = open(path, "w")
        text_file.write(json)
        text_file.close()

    @staticmethod
    def read_json_file(path):
        try:
            with open(path) as data_file:
                data = json.load(data_file)
            return data
        except:
            return None