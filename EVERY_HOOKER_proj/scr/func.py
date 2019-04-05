#coding:utf-8
import urllib.request
import re
import sys
import struct
import win32api,win32con

from bs4 import BeautifulSoup

def html2mjo(url):
    """连接检查"""
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError:
        win32api.MessageBox(
            0,"连接超时！请检查你的网络是否流畅，或你的网址是否有效"
            ,"BAIKE_HOOKER-error",win32con.MB_OK)
        sys.exit(0)
    except ValueError:
        win32api.MessageBox(
            0,"无效的网址\n或缺少http://的标志\n或程序不支持的域名"
            ,"BAIKE_HOOKER-error",win32con.MB_OK)
        sys.exit(0)
    else:
        """文件写入"""
        html = page.read()#Try to hook HTML
        win32api.MessageBox(0,"成功链接到指定网页！","BAIKE_HOOKER-message",
                            win32con.MB_OK)
        soup = BeautifulSoup(html.strip(), 'html.parser')
        n = soup.text
        write = n.strip()
        file = open('html_hook.mjo','w',encoding = 'utf8',errors='ignore')
        file.write(write)
        win32api.MessageBox(
            0,"导出mjo文件成功！","BAIKE_HOOKER-success",win32con.MB_OK)
        file.close()
        sys.exit(0)
