#!/usr/bin/env python3
"""
Localhost.run tunnel - creates reverse SSH tunnel
Author: HumayunShariarHimu
"""

import os

def run_localhost_run():
    """Execute localhost.run tunnel command"""
    os.system("ssh -R 80:localhost:8080 nokey@localhost.run | grep .lhr.life")

if __name__ == "__main__":
    run_localhost_run()
