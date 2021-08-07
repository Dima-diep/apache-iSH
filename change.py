#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

print("Find pair strings with \"DocumentRoot\" and change it")
print("1.nano")
print("2.micro")
print("3.joe")
a = int(input())

if a == 1:
    os.system("apk add nano && nano /usr/etc/apache2/httpd.conf")
elif a == 2:
    os.system("apk add micro && clear && echo "Ctrl-S for save, Ctrl-Q for exit" && sleep 10s && micro /usr/etc/apache2/httpd.conf")
elif a == 3:
    os.system("apk add joe && clear && echo "Ctrl-K-Q for exit" && sleep 10s && joe /usr/etc/apache2/httpd.conf")
