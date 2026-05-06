# -*- coding: utf-8 -*-
import re

def replace_proxy():
    file = "1.conf"
    # 读文件
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 全局精准替换 PROXY
    new_content = re.sub(r'PROXY', 'AUTO', content)

    # 写回
    with open(file, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(new_content)

    print("已完成 1.conf 中所有 PROXY 替换为 AUTO")

if __name__ == "__main__":
    replace_proxy()
