#!/usr/bin/env python3

import sys
import os

# libディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from lib.slack_webhook import SlackWebhook

def main():
    # Your code goes here
    pass

if __name__ == "__main__":
    main()
