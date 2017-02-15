# -*- coding: utf-8 -*-
from Public_lib import *
#重启应用模块进程服务#
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
            if commonname=="resin":
                self.command="/etc/init.d/resin restart"
            elif commonname=="nginx":
                self.command="/etc/init.d/nginx restart"
            elif commonname=="haproxy":
                self.command="/etc/init.d/haproxy restart"
            elif commonname=="apache":
                self.command="/etc/init.d/httpd restart"
                self.command2="name=httpd state=started enabled=yes"
                #self.command="ifconfig"
                #self.command="name=vsftpd state=stopped enabled=yes"
            elif commonname=="mysql":
                self.command="/etc/init.d/mysql restart"
            elif commonname=="snmp":
                self.command="/etc/init.d/snmpd restart"
            elif commonname=="lighttpd":
                self.command="/etc/init.d/lighttpd restart"
            elif commonname=="squid":
                self.command="/etc/init.d/squid restart"
            self.Runresult2 = ansible.runner.Runner(
            pattern=self.hosts, forks=forks,
            module_name="service", module_args=self.command2,).run()

#            self.Runresult = ansible.runner.Runner(
#            pattern=self.hosts, forks=forks,
            #module_name="command", module_args=self.command,).run()
            if len(self.Runresult2['dark']) == 0 and len(self.Runresult2['contacted']) == 0:
                #return "\""+'_'.join(self.hosts)+u"\"No hosts found,请确认主机已经添加ansible环境！"
                return "No hosts found,请确认主机已经添加ansible环境！"
        except Exception,e:
            return "Error: \""+str(e)+"\""
        return self.Runresult2
