from bs4 import BeautifulSoup
import requests

# Extract data
def myscrap(tag):
    # URL to scrape
    url = f'https://quotes.toscrape.com/tag/{tag}/'
    
    # Get HTML content from URL
    r  = requests.get(url)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')

    # Parameters to extract specific info from HTML
    dct_post = {'class': 'quote'}
    dct_quote = {'class': 'text', 'itemprop': 'text'}
    dct_author = {'class': 'author', 'itemprop': 'author'}

    posts = soup.find_all('div', attrs=dct_post)

    # Write specific info in json
    out = []
    for post in posts:
        quote = post.find('span', attrs=dct_quote).text.strip('“"”')
        author = post.find('small', attrs=dct_author).text.strip()
        item = {
            'Quote': quote, 
            'Author': author
        }
        out.append(item)

    return out
