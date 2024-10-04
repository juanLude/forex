from bs4 import BeautifulSoup
import pandas as pd
import requests

def dailyfx_com():

    resp = requests.get('https://www.myfxbook.com/community/outlook')

    print(resp.content)
    print(resp.status_code)

    soup = BeautifulSoup(resp.content, 'html.parser')

    #print(soup)

    rows = soup.select(".")

    # 196 - check from there

    