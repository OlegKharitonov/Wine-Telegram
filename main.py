import requests
from bs4 import BeautifulSoup as BS


MAX_PAGE = 1
# 19

def get_soup(url, **kwargs):
    response = requests.get(url, **kwargs)
    if response.status_code == 200:
        soup = BS(response.text, features='html.parser')
    else:
        soup = None

    return soup


def crawl_products(max_page):
    urls = []
    fmt = 'https://www.bcfw.co.uk/buy-wine/red-wine?page={page}'
    for page_n in range(1, max_page+1):
        print('page: {}'.format(page_n))
        page_url = fmt.format(page=page_n)
        soup = get_soup(page_url)
        if soup is None:
            break

        for tag in soup.select('.product-head-main a'):
            href = tag.attrs['href']
            url = format(href)
            urls.append(url)

    return urls

def parse_products(urls):
    data = []
    for url in urls:
        soup=get_soup(url)
        if soup is None:
            break

    return data


def main():
    urls = crawl_products(MAX_PAGE)
    print('\n'.join(urls))
    data = parse_products(urls)


if __name__ == '__main__':
    main()
