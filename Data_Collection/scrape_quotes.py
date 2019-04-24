import requests
from bs4 import BeautifulSoup
import lxml
import _pickle as pickle

def get_formatted_quotes(quote_list):
    formatted_quotes = []

    for quote in quotes:
        soup_quote = BeautifulSoup(quote.get_text(), "lxml")
        try:
            ex1 = soup_quote.find('span')
            _ = ex1.extract()
        except:
            pass
        try:
            ex2 = soup_quote.find('a')
            _ = ex2.extract()
        except:
            pass
        quote_html = soup_quote.get_text()
        quote_text = quote_html.split("    ―\n")[0]
        formatted_quotes.append(quote_text)
    return formatted_quotes

all_quotes = []
for i in range(1, 25):
    page = requests.get('https://www.goodreads.com/quotes/tag/knowledge?page='+str(i))
    main_soup = BeautifulSoup(page.content, 'html.parser')
    quotes = main_soup.find_all("div", class_="quoteText")
    curr_formatted_quotes = get_formatted_quotes(quotes)
    all_quotes.extend(curr_formatted_quotes)

f = open("goodreads_knowledge.pickle", mode="wb")
pickle.dump(all_quotes, f)
f.close()
