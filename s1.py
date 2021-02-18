#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author : coffe
# Time   : 2021-02-15 16:00
# File   : s1.py
import optparse
import os
import time

def daemonize():
    if os.fork()==0:
        os.setsid()
        if os.fork()==0:
            return
    os._exit(0)


def main():
    usage = """
    1. read docs: https://github.com/mdipierro/workflow
    2. create a file workflow.config
    3. run workflow.py
    """
    version = "0.1"
    parser = optparse.OptionParser(usage, None, optparse.Option, version)
    parser.add_option("-s", "--sleep", dest="sleep", default=1,
                      help="sleep interval")
    parser.add_option("-c", "--clear", dest="clear", default=None,
                      help="clear rule")
    parser.add_option("-n", "--name", dest="name", default='$0',
                      help="name")
    parser.add_option("-f", "--folder", dest="folder", default='./',
                      help="folder for workflow")
    parser.add_option("-d", "--daemonize", dest="daemonize", default=False,
                      action="store_true", help="runs as daemon")
    parser.add_option("-x", "--config", dest="config", default=None,
                      help="path of the config filename "\
                          +"(default=workflow.config)")
    parser.add_option("-y", "--cache", dest="cache", default=None,
                      help="path of the cache filename "\
                          +"(default=workflow.cache)")
    parser.add_option("-l", "--logfile", dest="logfile", default=None,
                      help="path of the logfile "\
                          +"(default=/var/tmp/workflow.log when daemonized)")
    (options, args) = parser.parse_args()
    print(options)
    print(args)
    if options.clear:
        # open('.workflow.%s.clear' % options.clear,'wb').write(time.ctime())
        return
    if options.daemonize:
        options.logfile = options.logfile or '/var/tmp/workflow.log'
        print('daemonize')
    try:
        time.sleep(10)
        print('11')
    except KeyboardInterrupt:
        return


data = {
    'OWS': [
            {'service_name':'GDE_ADC','current_package_size':20,'target_package_size': 21},
            {'service_name':'GDE_ADC','current_package_size':201,'target_package_size': 21},
            {'service_name':'GDE_FS','current_package_size':22,'target_package_size': 11},
            {'service_name':'GDE_Manas','current_package_size':120,'target_package_size': 10},
            {'service_name':'GDE_DSP','current_package_size':220,'target_package_size': 9},
        ],
    'NAWA': [
                {'service_name':'GDE_ADC','current_package_size':120,'target_package_size': 210},
                {'service_name':'GDE_ADC','current_package_size':320,'target_package_size': 210},
                {'service_name':'GDE_FS','current_package_size':22,'target_package_size': 11},
                {'service_name':'GDE_Manas','current_package_size':120,'target_package_size': 10},
                {'service_name':'GDE_DSP','current_package_size':220,'target_package_size': 9},
            ]
}
b_list = []
for k,v_list in data.items():
    small_list = []
    b = {}
    for item in v_list:
        b.setdefault(item['service_name'], {**item})
    ret = list(b.values())
    for i in ret:

        b_list.append(list(i.values()))
    # for i in ret:
    #     service_name = i.get('service_name').split('GDE_')[1]
    #     current_package_size = i.get('current_package_size')
    #     target_package_size = i.get('target_package_size')
print()
from pandas import DataFrame
import numpy as np
df = DataFrame(b_list)
df2 = DataFrame(df.values.T,index=['service_name','current_package_size','target_package_size'])
# df2.apply(lambda x:summary(x),axis=1)
df2['GDC'] = df2[0]+df2[4]
# 提取第0行
print(df2)
print('++++++++++++++++')
df3 = df2.iloc[2]
print(df3.values)
print('================')
df4 = df2.iloc[:,0]
df5 = df2.iloc[:,4]
x = df4.values.tolist()
y = df5.values.tolist()
x.extend(y)
print(x)

# print(df3.iloc[0:4])











# b=list(b.values())
# print(b)
xuyao_dict = [
    {'service_name': 'ADC','current_total_size':20,'target_total_size': 21,'ows_current_package_size':20,'ows_target_package_size': 21,'nawa_current_package_size':20,'nawa_target_package_size': 21}
]