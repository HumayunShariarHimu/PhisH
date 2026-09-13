#!/usr/bin/env python3
"""
Localtunnel - creates secure tunnel to localhost
Author: HumayunShariarHimu
"""

import os

def run_localtunnel():
    """Execute localtunnel command"""
    os.system("lt --port 8080 > url.txt")

if __name__ == "__main__":
    run_localtunnel()
