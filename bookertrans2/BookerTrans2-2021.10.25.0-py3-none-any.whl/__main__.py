# coding: utf-8

import os
from os import path
from argparse import ArgumentParser
from . import trans_html, config, __version__

is_html = lambda f: f.endswith('.html') or \
                    f.endswith('.htm') or \
                    f.endswith('.xhtml')

def process_file(fname):
    if not is_html(fname):
        print(f'{fname} is not a html file')
        return
    
    print(fname)
    html = open(fname, encoding='utf-8').read()
    html = trans_html(html)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

def process_dir(dir):
    files = [f for f in os.listdir(dir) if is_html(f)]
    for f in files:
        f = path.join(dir, f)
        process_file(f)

def main():
    env_appid = os.environ.get('BAIDU_FANYI_APPID', '')
    env_appkey = os.environ.get('BAIDU_FANYI_APPKEY', '')
    parser = ArgumentParser(prog="BookerTrans2", description="HTML Translator with Baidu Api for iBooker/ApacheCN")
    parser.add_argument('fname', help="html file name or dir name")
    parser.add_argument('-v', '--version', action="version", version=__version__)
    parser.add_argument('-P', '--proxy', help=f'proxy with format \d+\.\d+\.\d+\.\d+:\d+ or empty')
    parser.add_argument('-t', '--timeout', type=float, default=8, help=f'timeout in second')
    parser.add_argument('-w', '--wait-sec', type=float, default=0.1, help='delay in second between two times of translation')
    parser.add_argument('-r', '--retry', type=int, default=10, help='count of retrying')
    parser.add_argument('-s', '--src', default='auto', help='src language')
    parser.add_argument('-d', '--dst', default='zh', help='dest language')
    parser.add_argument('-i', '--appid', default=env_appid, help='baidu api appid')
    parser.add_argument('-k', '--appkey', default=env_appkey, help='baidu api appkey')
    args = parser.parse_args()
    
    if args.proxy:
        p = args.proxy
        args.proxy = {'http': p, 'https': p}
    config.proxy = args.proxy
    config.timeout = args.timeout
    config.wait_sec = args.wait_sec
    config.retry = args.retry
    config.src = args.src
    config.dst = args.dst
    config.appid = args.appid
    config.appkey = args.appkey

    if path.isdir(args.fname):
        process_dir(args.fname)
    else:
        process_file(args.fname)
        
if __name__ == '__main__': main()
