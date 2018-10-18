# -*- coding: utf-8 -*-

# db_config
env = {
    'redis': {
        'host': '172.18.18.165',
        'port': 6379,
        'db': [0, 1, 2, 3, 4, 5],
    },
    'mongo': {
        'host': ['172.18.19.187:27017', '172.18.19.188:27017'],
        # 'port': 27017,
        'replicaset': 'rs0',
        'readPreference': 'secondaryPreferred',
        'authSource': 'admin',
        'user': 'readwrite',
        'password': 'yulore456',
        'db': 'crs',
        'pwd_authSource': 'admin',
        'pwd_user': 'readwrite',
        'pwd_password': 'yulore456',
        'pwd_db': 'pwd'
    },
    # 'mysql':{
    #     'user': 'admin',
    #     'password': 'admin',
    #     'host': '172.18.19.155',
    #     'database': 'crawler'
    # },
    'proxies': {
        'launcher': True,
        'port': 8080,
        'timeout': 60,
        'redirects': True,
        'verify': False,
        'check_url': "https://www.baidu.com/duty/copyright.html",
        'try_times': 3,
        'cmcc_ip': [
            "squidsz01.dianhua.cn",
            "squidsz02.dianhua.cn",
        ],
        'cucc_ip': [
            "squidsz01.dianhua.cn",
            "squidsz02.dianhua.cn",
        ]
    },
    'mul_dama_url':"http://172.18.19.189:9081/crawl/calls/mul_dama",
    'mul_dama_report_url':"http://172.18.19.189:9081/crawl/calls/dama_report",
}
