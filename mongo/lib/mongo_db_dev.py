# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:36:29 2018

@author: admin
"""

import pymongo
import pandas as pd

mongo_conf= {
        'host': ['172.18.19.187:27017', '172.18.19.188:27017'],
        'replicaset': 'rs0',
        'readPreference': 'secondaryPreferred',
        'authSource': 'admin',
        'user': 'readwrite',
        'password': 'yulore456',
        'db': 'crs'
    }
class MongodbConnection(object):
    """
    MongoDB连接类
    """
    def __init__(self):
        self.conn = None
        self.set_db_conn()

    def set_db_conn(self):
        safe_conn = pymongo.MongoClient(
            mongo_conf['host'], 
            authSource=mongo_conf['authSource'], username=mongo_conf['user'], password=mongo_conf['password'], connect=False)
        self.conn = safe_conn[mongo_conf['db']]

    def get_db_conn(self):
        db = self.conn
        return db

db_conn = MongodbConnection().get_db_conn()