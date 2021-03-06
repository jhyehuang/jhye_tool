# -*- coding: utf-8 -*-

CHANNEL_MAPPING = {
# 联通统一渠道
u'10010': 'worker.crawler.unicom.main',
# 移动统一渠道
u'10086': 'worker.crawler.china_mobile.all_entry.main',
# 电信统一渠道
u'10000': '',
# 联通分渠道
u"10010-安徽": '',
u"10010-北京": '',
u"10010-广东": '',
u"10010-广东-深圳": '',
u"10010-河北": '',
u"10010-河南": '',
u"10010-湖北": '',
u"10010-湖南": '',
u"10010-吉林": '',
u"10010-江苏": '',
u"10010-江西": '',
u"10010-辽宁": '',
u"10010-内蒙古": '',
u"10010-山东": '',
u"10010-山西": '',
u"10010-陕西": '',
u"10010-上海": '',
u"10010-四川": '',
u"10010-天津": '',
u"10010-云南": '',
u"10010-浙江": '',
u"10010-重庆": '',
u"10010-福建": '',
u"10010-广西": '',
u"10010-黑龙江": '',
u"10010-贵州": '',
u"10010-海南": '',
u"10010-宁夏": '',
u"10010-青海": '',
u"10010-西藏": '',
u"10010-新疆": '',
u"10010-甘肃": '',
# 移动分渠道
u"10086-安徽": '',
u"10086-北京": 'worker.crawler.china_mobile.beijing.main',
#u"10086-安徽": 'worker.crawler.china_mobile.anhui.main', # 'worker.crawler.china_mobile.anhui.main'
u"10086-广东": '', # 'worker.crawler.china_mobile.guangdong.main'
u"10086-广东-深圳": '', # 'worker.crawler.china_mobile.SZ.main'
u"10086-河北": 'worker.crawler.china_mobile.hebei.main',
u"10086-河南": 'worker.crawler.china_mobile.henan.main',
u"10086-湖北": '', #  'worker.crawler.china_mobile.hubei.main'
u"10086-湖南": 'worker.crawler.china_mobile.wap.hunan.main', # 'worker.crawler.china_mobile.hunan.main'
u"10086-江苏": 'worker.crawler.china_mobile.wap.jiangsu.main',
u"10086-吉林": '',
#u"10086-江苏": 'worker.crawler.china_mobile.jiangsu.main',
u"10086-江西": '', # 'worker.crawler.china_mobile.jiangxi.main'
u"10086-辽宁": 'worker.crawler.china_mobile.liaoning.main',
u"10086-内蒙古": '',
u"10086-山东": '', # 'worker.crawler.china_mobile.shandong.main'
u"10086-山西": 'worker.crawler.china_mobile.shanxi.main',
u"10086-陕西": 'worker.crawler.china_mobile.shaanxi.main',
u"10086-上海": 'worker.crawler.china_mobile.shanghai.main',
u"10086-四川": 'worker.crawler.china_mobile.sichuan.main',
#u"10086-天津": 'worker.crawler.china_mobile.wap.tianjin.main',
u"10086-天津": 'worker.crawler.china_mobile.tianjin.main',
# u"10086-云南": '',
u"10086-云南": 'worker.crawler.china_mobile.yunnan.main',
u"10086-浙江": 'worker.crawler.china_mobile.zhejiang.main',
#u"10086-浙江": 'worker.crawler.china_mobile.wap.zhejiang.main',
u"10086-重庆": 'worker.crawler.china_mobile.chongqing.main',
u"10086-福建": '',
u"10086-广西": 'worker.crawler.china_mobile.guangxi.main',
u"10086-黑龙江": 'worker.crawler.china_mobile.heilongjiang.main', # 'worker.crawler.china_mobile.heilongjiang.main'
u"10086-贵州": '',
#u"10086-贵州": 'worker.crawler.china_mobile.guizhou.main',
u"10086-海南": '', # worker.crawler.china_mobile.hainan.main
u"10086-宁夏": '',
u"10086-青海": '',
u"10086-西藏": '',
u"10086-新疆": '',
u"10086-甘肃": '',
# 电信分渠道
u"10000-安徽": 'worker.crawler.china_telecom.wap.anhui.main',
u"10000-北京": 'worker.crawler.china_telecom.beijing.main',
u"10000-广东": 'worker.crawler.china_telecom.guangdong.main',
u"10000-广东-深圳": '',
u"10000-河北": 'worker.crawler.china_telecom.hebei.main',
u"10000-河南": 'worker.crawler.china_telecom.henan.main',
u"10000-湖北": 'worker.crawler.china_telecom.wap.hubei.main',
# u"10000-湖南": 'worker.crawler.china_telecom.hunan.main',
u"10000-湖南": 'worker.crawler.china_telecom.wap.hunan.main',
u"10000-吉林": 'worker.crawler.china_telecom.jilin.main',
u"10000-江苏": 'worker.crawler.china_telecom.wap.jiangsu.main', # 'worker.crawler.china_telecom.jiangsu.main'
u"10000-江西": 'worker.crawler.china_telecom.jiangxi.main',
u"10000-辽宁": 'worker.crawler.china_telecom.liaoning.main',
u"10000-内蒙古": 'worker.crawler.china_telecom.neimenggu.main',
u"10000-山东": 'worker.crawler.china_telecom.shandong.main',
u"10000-山西": '',
u"10000-陕西": 'worker.crawler.china_telecom.shaanxi.main',
u"10000-上海": 'worker.crawler.china_telecom.shanghai.main',
u"10000-四川": 'worker.crawler.china_telecom.sichuan.main',
u"10000-天津": 'worker.crawler.china_telecom.tianjin.main',
u"10000-云南": 'worker.crawler.china_telecom.yunnan.main',
# u"10000-云南": 'worker.crawler.china_telecom.wap.yunnan.main',
u"10000-浙江": 'worker.crawler.china_telecom.zhejiang.main',
u"10000-重庆": 'worker.crawler.china_telecom.chongqing.main',
u"10000-福建": 'worker.crawler.china_telecom.fujian.main',
u"10000-广西": 'worker.crawler.china_telecom.guangxi.main',
u"10000-黑龙江": 'worker.crawler.china_telecom.heilongjiang.main',
u"10000-贵州": '',
u"10000-海南": '',
u"10000-宁夏": 'worker.crawler.china_telecom.ningxia.main',
u"10000-青海": '',
u"10000-西藏": '',
u"10000-新疆": '',
u"10000-甘肃": '',
# no crawler supported case
u'none':  '',
}
