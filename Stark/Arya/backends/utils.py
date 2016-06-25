#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import sys


import django
django.setup()

from Arya import models
from Arya import action_list


class ArgvManagement(object):
    '''
    接收用户指令并分配到相应模块
    '''
    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse()

    def help_msg(self):
        print("Available modules:")
        for registered_module in action_list.actions:
            print("  %s" % registered_module)
        exit()
    def argv_parse(self):
        #print(self.argvs)
        if len(self.argvs) <2:
            self.help_msg()
            #判断输入的参数是否合法,否则输出帮助
        module_name = self.argvs[1]
        #取出第一个值
        if '.' in module_name:
            #判断是否'.'是否存在module_name
            mod_name,mod_method = module_name.split('.')
            #分割
            module_instance  = action_list.actions.get(mod_name)
            #判断是否存在于字典
            if module_instance:#matched
                print('12312312')
                module_instance(self.argvs,models)

        else:
            exit("invalid module name argument")

