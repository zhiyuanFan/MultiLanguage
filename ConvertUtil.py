# -*- coding: utf-8 -*-

import xlrd
import xml.dom.minidom
import os
from shutil import copyfile


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


def copy_default_xml(src, des):
    try:
        copyfile(src, des)
    except Exception as e:
        print(e)


def translate_default_to_other(generate_path, excel_absolute_path, by_index=0):
    # 获取xml文档
    dom = xml.dom.minidom.parse(generate_path)
    # 根节点
    root = dom.documentElement
    # string 节点
    strings = root.getElementsByTagName('string')

    # 获取excel文档
    data = open_excel(excel_absolute_path)
    # 获取sheet页
    table = data.sheets()[by_index]
    # 获取行数
    rows = table.nrows

    for str_index in range(0, len(strings)):
        # <string name"translate_key">value</string>  获取key
        translate_key = strings[str_index].getAttribute('name')
        for row in range(0, rows):
            # 获取excel的 key
            value = table.cell(row, 0).value
            # 如果excel的key 和 string.xml文件的key一样， 则修改其value值
            if translate_key == value:
                strings[str_index].firstChild.data = table.cell(row, 1).value

    f = open(generate_path, 'w')
    dom.writexml(f, addindent='  ', encoding='utf-8')
    f.close()


def deal_with_excel_and_xml(excel_path, xml_path):
    paths = os.path.split(xml_path)
    currentPath = paths[0]
    destinationPath = os.path.join(currentPath, 'values-other')
    if not os.path.exists(destinationPath):
        os.mkdir(destinationPath)
    destinationPath = os.path.join(destinationPath, 'strings.xml')
    # 創建文件strings.xml
    f = open(destinationPath, 'w')
    f.close()
    copy_default_xml(xml_path, destinationPath)
    translate_default_to_other(destinationPath, excel_path)
    return destinationPath
