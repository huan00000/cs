#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file_path = "1.conf"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("PROXY", "AUTO")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("替换完成：PROXY → AUTO")
