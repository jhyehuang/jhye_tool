#coding:utf-8

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time
import datetime
import requests

ALL_COUNT=5
ERR_PR_LINE=0.5
import json

def time_to_p(end_date):
    timeArray = time.strptime(end_date, "%Y%m%d")
    now_utc = time.mktime(timeArray)
    begin_utc=now_utc-24*60*60
    begin_utc=datetime.datetime.utcfromtimestamp(begin_utc)
    yea_mon_day=begin_utc.strftime("%Y.%m.%d")
    begin_date =begin_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    now_utc=datetime.datetime.utcfromtimestamp(now_utc)
    now_date =now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    return yea_mon_day,begin_date,now_date

class ES(object):

    class_flag = "es"
    
    def __init__(self, end_date='20181109',es_hosts=['172.18.52.196']):
        self.es = Elasticsearch(hosts=es_hosts,timeout=30)
        self.yea_mon_day,self.begin_date,self.now_date=time_to_p(end_date)
        self.indexes = ['logstash-crs_report-'+self.yea_mon_day]
        self.doc_type = 'doc'
        self.body = { "query":{
            "bool":{ 
                "must":[{
                    "range":{
                        "@timestamp":{
                            "gte": self.begin_date,    #最小日期
                            "lte": self.now_date
                        }
                    }
                }],
                "should":[],
                "minimum_should_match" : 1,
                "boost" : 1.0
        }}}

    def get_all_ret(self,sid, scroll='5m', timeout="3m"):
        es_search_options=self.body
        must_flag=[{
                "match_phrase":{
                    "MSG.sid":sid
                    }
                }]
        should_flag=[{
                    "match_phrase": {
                        "MODELNAME":"/home/data/crs-crawler.dianhua.cn/venv/lib/python2.7/site-packages/requests/sessions.py"
                    }

                },{
                    "match_phrase": {
                        "MODELNAME":"/home/crs-crawler.dianhua.cn/venv/lib/python2.7/site-packages/requests/sessions.py"
                    }

                }
                ]
        es_search_options['query']['bool']['must'].extend(must_flag)
        es_search_options['query']['bool']['should'].extend(should_flag)
        # print(es_search_options)
        es_result = helpers.scan( client=self.es, 
                                 query=es_search_options,
                                #  scroll=scroll, index=self.indexes
                                 doc_type=self.doc_type, timeout=timeout )
        ret=list(es_result)
        # for line in ret:
        #     print line['_source']['MODELNAME']
        return ret

    def get_proxy_ret(self,proxy, scroll='5m', timeout="3m"):
        es_search_options=self.body
        must_flag=[{
                "match_phrase":{
                    "MSG.proxies.http":proxy
                    }
                }]
        should_flag=[{
                    "match_phrase": {
                        "MODELNAME":"/home/data/crs-crawler.dianhua.cn/venv/lib/python2.7/site-packages/requests/sessions.py"
                    }

                },{
                    "match_phrase": {
                        "MODELNAME":"/home/crs-crawler.dianhua.cn/venv/lib/python2.7/site-packages/requests/sessions.py"
                    }

                }
                ]
        es_search_options['query']['bool']['must'].extend(must_flag)
        es_search_options['query']['bool']['should'].extend(should_flag)
        # print(es_search_options)
        es_result = helpers.scan( client=self.es, 
                                 query=es_search_options,
                                #  scroll=scroll, index=self.indexes
                                 doc_type=self.doc_type, timeout=timeout )
        ret=list(es_result)
        # for line in ret:
        #     print line['_source']['MODELNAME']
        return ret

    def get_err(self,sid,scroll='5m', timeout="3m"):
        es_search_options=self.body
        err_flag=[{
                "match_phrase":{
                    "MSG.sid":sid 
                    }
                },{
                "match_phrase":{
                    "MSG.state_log.execute_status":5017
                    }
                }]
        es_search_options['query']['bool']['must'].extend(err_flag)
        es_result = helpers.scan( client=self.es, 
                                 query=es_search_options,
                                #  scroll=scroll, index=self.indexes ,
                                 doc_type=self.doc_type, timeout=timeout )
        return list(es_result)



# print es
# print (es.get_all_ret('SID55b3f743f96a427da56cad04bd3bee8c'))



