import argparse
from bs4 import BeautifulSoup
import random
from urllib.request import Request, urlopen
from config import headers
import re

encode_choices = ['none', 'cpu', 'nv-gpu', ]

def get_parser():
    parser = argparse.ArgumentParser(description="Jable TV Downloader")
    parser.add_argument("--random", type=bool, default=False,
                        help="Enter True for download random ")
    parser.add_argument("--url", type=str, default="", nargs='+',
                        help="Jable TV URL to download")
    parser.add_argument("--all-urls", type=str, default="",
                        help="Jable URL contains multiple avs")
    
    parser.add_argument("--encode", type=str, choices=encode_choices,
                        default='none', help="Choose encode accelerator (default: %(default)s): "
                                           "none: no re-encoding; "
                                           "cpu: use CPU to encode; "
                                           "nv-gpu: use nvidia GPU to encode")

    return parser


def av_recommand():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://jable.tv/'
    request = Request(url, headers=headers)
    web_content = urlopen(request).read()
    # 得到繞過轉址後的 html
    soup = BeautifulSoup(web_content, 'html.parser')
    h6_tags = soup.find_all('h6', class_='title')
    av_list = re.findall(r'https[^"]+', str(h6_tags))
    return random.choice(av_list)


# print(av_recommand())
