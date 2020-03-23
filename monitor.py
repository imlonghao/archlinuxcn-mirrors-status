#!/usr/bin/env python3

import json
import requests

mirrors = [
    ['浙江大学', 'https://mirrors.zju.edu.cn/archlinuxcn/'],
    ['中国科学技术大学', 'https://mirrors.ustc.edu.cn/archlinuxcn/'],
    ['清华大学', 'https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/'],
    ['Our main server', 'https://repo.archlinuxcn.org/'],
    ['xTom HK', 'https://mirror.xtom.com.hk/archlinuxcn/'],
    ['xTom US', 'https://mirror.xtom.com/archlinuxcn/'],
    ['xTom NL', 'https://mirror.xtom.nl/archlinuxcn/'],
    ['Open Computing Facility, UC Berkeley',
     'https://mirrors.ocf.berkeley.edu/archlinuxcn/'],
    ['上海科技大学', 'https://mirrors-wan.geekpie.club/archlinuxcn/'],
    ['网易', 'https://mirrors.163.com/archlinux-cn/'],
    ['重庆大学', 'https://mirrors.cqu.edu.cn/archlinuxcn/'],
    ['SJTUG 软件源镜像服务', 'https://mirrors.sjtug.sjtu.edu.cn/archlinux-cn/'],
    ['莞工 GNU/Linux 协会 开源软件镜像站', 'https://mirrors.dgut.edu.cn/archlinuxcn/'],
    ['腾讯云', 'https://mirrors.cloud.tencent.com/archlinuxcn/']
]

result = []

for mirror in mirrors:
    try:
        lastupdate = int(
            requests.get(
                mirror[1] +
                'lastupdate',
                timeout=5).text)
    except BaseException:
        lastupdate = 0
    result.append({
        'name': mirror[0],
        'url': mirror[1],
        'lastupdate': lastupdate
    })

newest = max([x['lastupdate'] for x in result])
for each in result:
    each['diff'] = newest - each['lastupdate']

with open('/home/imlonghao/public_html/status/status.json', 'w') as f:
    f.write(json.dumps(result))
