import requests
from bs4 import BeautifulSoup

def trade_spyder(max_pages):
    page=1
    while page < max_pages:
        url = ""
