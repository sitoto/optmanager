# -*- coding: utf-8 -*-
from Public_lib import *
#同步业务文件模块#
class Modulehandle():
    def __init__(self,moduleid,hosts,sys_param_row):
        self.hosts = ""
        self.Runresult = ""
        self.moduleid = moduleid
        self.sys_param_array= sys_param_row
        self.hosts=target_host(hosts,"IP")

    def run(self):
        try:
            commonname=str(self.sys_param_array[0])
            if commonname=="falcon-agent":
                source="http://img1.gtimg.com/news/pics/hv1/220/249/2107/137071390.jpg"
                goal="/tmp/"
                hx="ls "+str(goal)
            ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="get_url", module_args="url="+source+" dest="+goal,).run()

            self.Runresult = ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="command", module_args=hx,).run()
            if len(self.Runresult['dark']) == 0 and len(self.Runresult['contacted']) == 0:
                return "No hosts found,请确认主机已经添加ansible环境！"

        except Exception,e:
            return str(e)
        return self.Runresult

