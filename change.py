#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

print("Find pair strings with \"DocumentRoot\" and change it")
print("1.nano")
print("2.micro")
print("3.joe")
a = int(input())

if a == 1:
    os.system("apt install nano && nano /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 2:
    os.system("apt install micro && clear && echo "Ctrl-S for save, Ctrl-Q for exit" && sleep 10s && micro /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
elif a == 3:
    os.system("apt install joe && clear && echo "Ctrl-K-Q for exit" && sleep 10s && joe /data/data/com.termux/files/usr/etc/apache2/httpd.conf")
