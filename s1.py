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
# df = DataFrame(b_list)
# df2 = DataFrame(df.values.T,index=['service_name','current_package_size','target_package_size'])
# # df2.apply(lambda x:summary(x),axis=1)
# df2['GDC'] = df2[0]+df2[4]
# # 提取第0行
# print(df2)
# print('++++++++++++++++')
# df3 = df2.iloc[2]
# print(df3.values)
# print('================')
# df4 = df2.iloc[:,0]
# df5 = df2.iloc[:,4]
# x = df4.values.tolist()
# y = df5.values.tolist()
# x.extend(y)
# print(x)

# print(df3.iloc[0:4])



s1 = [
    ['os',1,2,3,4,5,'Y'],
    ['GDE服务',1,2,3,4,5,'Y'],
    ['运维使能',1,2,3,4,5,'Y'],
    ['镜像服务',1,2,3,4,5,'Y'],
]

import numpy
df = DataFrame(s1)
# df0 = df[0] # 取0列
df1 = df.iloc[0]  # 取0行
df3 = df.iloc[3]
df4 = df1 + df3

def change_status(index_str):
    if isinstance(index_str, numpy.int64):
        return index_str
    if 'N' in index_str:
        index_str = 'N'
    elif 'YY' in index_str:
        index_str = 'Y'
    return index_str


df4 = df4.apply(lambda x:change_status(x))
df4_reverse = df4.values.T

# 删除os/镜像服务行，然后处理后合并
df = df[(df.index!=0)&(df.index!=3)]  # 删除os/镜像服务行
# 插入一行，随便设置索引，比如按照字符串作为索引
# df.loc['new'] = ['duck', 10]
# 此时需要把最后一行安排到第二行去，方法是新增一列指明他们的顺序
# df['order'] = [1, 3, 4, 2]  # 所以这个顺序列表很重要
# 按照order字段进行排序
# df = df.sort_values(by='order')
# 再接下来是重新设置索引
# df = df.reset_index()
# 最后删除多余的列
# df.drop(columns=['index','order'],inplace=True)

df.loc['new'] = df4_reverse
print(df)

