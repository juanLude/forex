from bs4 import BeautifulSoup
import pandas as pd
import requests
import cloudscraper
def investing_com():

    session = cloudscraper.create_scraper()

    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    params = dict(
        action = "get_studies",
        pair_ID = 7,
        time_frame = 3600
    )

    resp = session.get("https://www.investing.com/common/technical_studies/technical_studies_data.php", params = params, headers=headers) 

    # print(resp.content)
    # print(resp.status_code)

    text = resp.content.decode("utf-8")

    

    print(text)