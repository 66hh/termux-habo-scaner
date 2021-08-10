#!/usr/bin/env python
#coding = utf - 8

import os;
import re;
import sys;
import hashlib;
import urllib.request;

def CheckFile(URL):
    try:
        req = urllib.request.Request(URL);
        data = urllib.request.urlopen(req).read().decode(encoding='utf-8');
    except:
        return CheckFile(URL);
    if "red color" in data and "\\u9ad8\\u5ea6\\u98ce\\u9669" in data:
        return "Trojan/Habo.Virus";
    elif "orange color" in data and "\\u8f7b\\u5ea6\\u98ce\\u9669" in data:
        return "Trojan/Habo.Suspicious";
    else :
        return "safe";
    
def GetFileMd5(strFile):
    file = None;
    strMd5 = "";
    try:
        file = open(strFile, "rb");
        md5 = hashlib.md5();
        strRead = "";
        while True:
            strRead = file.read(8096);
            if not strRead:
                break;
            md5.update(strRead);
        strMd5 = md5.hexdigest();
    except:
        return "-1";
    finally:
        if file:
            file.close();
    return strMd5;

def ScanFile(Path):
    URL = "https://habo.qq.com/file/detailcontent?md5=" + GetFileMd5(Path);
    CheckFile(URL);
    print(Path + " " + CheckFile(URL));

def ScanDir(Dir):
    for root, dirs, files in os.walk(Dir):
        for file in files:
            ScanFile(os.path.join(root, file));

def main():
    print("欲扫描目录:");
    Path = input();
    ScanDir(Path);
    main();

if __name__ == '__main__':
    main();
