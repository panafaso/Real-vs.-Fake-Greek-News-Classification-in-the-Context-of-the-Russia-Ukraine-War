
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen 
import re

def web_crawling(file_path):

    raw_texts = [] 

    with open(file_path, 'r', encoding='utf-8') as f:
        urls = f.readlines() 

    for url in urls:
        url = url.strip()
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
            raw = urlopen(req).read() 
            clean = BeautifulSoup(raw, features='html.parser') 

            paragraphs = clean.find_all('p') 
            raw_text = ' '.join([p.get_text() for p in paragraphs]) #to keep only text and not headers etc
            raw_text = re.sub('\n', ' ', raw_text)
            if raw_text.strip():
                raw_texts.append(raw_text) 
        
        except:
            continue #if error occurs with security etc, just skip this url 

    df = pd.DataFrame({'text': raw_texts}) 
    return df

try_df = web_crawling('fake_urls.txt') 
print(try_df.head()) 



    

