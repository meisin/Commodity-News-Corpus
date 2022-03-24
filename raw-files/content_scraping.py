from os import listdir
from os.path import isfile, join
from urllib.request import Request, urlopen

import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup as soup
from bs4 import Tag, NavigableString

OUTPUT_DIRECTORY = 'data/'

def reuters(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    text = ''
    title = page_soup.find("h1")
    text = title.text + '.\n'
    text += url + '.\n\n'
    
    mydivs = page_soup.find("div", {"class": "StandardArticleBody_body"}).findAll('p')
    for p in mydivs:
        text += p.text + '\n'
    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt') , 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()

def investing(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    
    text = ''
    title = page_soup.find("h1")
    text = title.text + '.\n'
    text += url + '.\n\n'
    
    ## ## 1. Contains <p>
    mydivs = page_soup.find("div", {"class": "WYSIWYG articlePage"}).findAll('p')
    for p in mydivs:
        text += p.text + '\n'

    ### 2. Contains <ul> list
    if len(mydivs) == 0:
        mydivs = page_soup.find("div", {"class": "WYSIWYG articlePage"}).findAll('li')
        for li in mydivs:
            text += li.text + '\n'

    ## ## 2. Does not contain <p>
    if len(mydivs) == 0:
        mydivs = page_soup.find("div", {"class": "WYSIWYG articlePage"})
        #print(mydivs)
        for c in mydivs.contents:
            if isinstance(c, NavigableString):
                text += c.string

            elif isinstance(c, Tag):
                if c.name == "br":
                    text += '\n'

    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()

def marketwatch(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    text = ''

    title = page_soup.find("h1", {"class": "article__headline"})
    text = title.text.strip() + '.\n'
    text += url + '.\n\n'
    
    mydivs = page_soup.find("div", {"class": "article__body article-wrap at16-col16 barrons-article-wrap"}).findAll('p')
    
    for p in mydivs:
        text += p.text
    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()
    
    
def hellenicshippingnews(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    text = ''

    title = page_soup.find("h1")
    text = title.text.strip() + '.\n'
    text += url + '.\n\n'
    
    mydivs = page_soup.find("div", {"class": "post-inner"}).findAll('p', class_="")

    for p in mydivs:    
        text += p.text + '\n'
     
    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()
    
def cnbc(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    text = ''

    title = page_soup.find("h1")
    text = title.text + '.\n'
    text += url + '.\n\n'
    mydivs = page_soup.find("div", {"class": "group"}).findAll('p')
    for p in mydivs:
        text += p.text + '\n'
         
    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()
    
def oilprice(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    
    text = ''
    title = page_soup.find("h1")
    text = title.text.strip() + '.\n'
    text += url + '.\n\n'
    
    mydivs = page_soup.find("div", {"class": "wysiwyg clear"}).findAll('p')

    for p in mydivs:    
        text += p.text + '\n'
     
    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()
    
def marketpulse(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    
    text = ''
    title = page_soup.find("h1")
    text = title.text.strip() + '.\n'
    text += url + '.\n\n'
    mydivs = page_soup.find("div", {"class": "contents"}).findAll('p')

    for p in mydivs:  
        text += p.text + '\n'

    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()
    
def fxempire(url, file_name):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    text = ''
    title = page_soup.find("h1")
    text = title.text.strip() + '.\n'
    text += url + '.\n\n'
    
    header_p = page_soup.find("span", {"class": "Span-sc-1abytr7-0 yXFco"})
    text += header_p.text + '\n'
    mydivs = page_soup.find("article", {"class": "Post__PostArticle-sc-1czihrw-0 lDuIo"}).findAll('p')

    for p in mydivs:    
        text += p.text + '\n'

    f = open(join(OUTPUT_DIRECTORY, file_name+ '.txt'), 'w', encoding='utf8', newline='\n')    ### this saves the file in Unix 'End of line' format
    f.write(text)
    f.close()


if __name__ == '__main__':
    
    data_source = pd.read_csv ('data_source.csv')
    for index, row in tqdm(data_source.iterrows(), total=len(data_source)):
        if row['Source'] == 'reuters':
            reuters(row['URL'],row['FileName'])
        elif row['Source'] == 'investing':
            investing(row['URL'],row['FileName'])
        elif row['Source'] == 'marketwatch':
            marketwatch(row['URL'],row['FileName'])
        elif row['Source'] == 'hellenicshippingnews':
            hellenicshippingnews(row['URL'],row['FileName'])
        elif row['Source'] == 'cnbc':
            cnbc(row['URL'],row['FileName'])
        elif row['Source'] == 'oilprice':
            oilprice(row['URL'],row['FileName'])
        elif row['Source'] == 'marketpulse':
            marketpulse(row['URL'],row['FileName'])
        elif row['Source'] == 'fxempire':
            fxempire(row['URL'],row['FileName'])
        
        
        
        
        
        