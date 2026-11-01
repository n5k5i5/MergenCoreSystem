#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.shell import MergenShell

def init_workspace():
    if not os.path.exists('licence.json'):
        with open('licence.json', 'w') as f:
            json.dump({"licence": True}, f)

def main():
    init_workspace()
    shell = MergenShell()
    shell.start_loop()

if __name__ == '__main__':
    main()
