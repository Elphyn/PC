import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Set up the base URL and headers
url = 'https://habr.com/ru/all/page'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
pages = 3

def scrape_articles_data(url, headers, number):
    """Scrapes article data from a website and returns a list of lists, 3rd argument is number of pages"""
    articles = []
    for i in range(1, number):
        print(f"Page {i} is done")
        response = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_list = soup.find_all('article', class_='tm-articles-list__item')
        
        for article in article_list:
            time = article.find('time').get('title')
            title = article.find('h2').text.strip()
            content = article.find('div', class_=['article-formatted-body article-formatted-body article-formatted-body_version-2','article-formatted-body article-formatted-body article-formatted-body_version-1']).text.strip()
            tags = article.find('div', class_='tm-article-snippet__hubs').text.strip()
            articles.append([time, title, content, tags])
    return articles

def create_dataframe(articles):
    """Converts a list of lists to a pandas DataFrame"""
    df = pd.DataFrame(articles, columns=['Time','Title', 'Content', 'Tags'])
    return df

def clean_dataframe(df):
    """Removes leading and trailing whitespace from the title column of a DataFrame"""
    df['Title'] = df['Title'].str.strip()
    return df

def save_dataframe_csv(df):
    """Saves a pandas DataFrame to a CSV file with the current date as the filename"""
    date_string = datetime.now().strftime('%Y-%m-%d')
    filename = f'article_data_{date_string}.csv'
    df.to_csv(filename, index=False)

def save_dataframe_excel(df):
    """Saves a pandas DataFrame to a xlsx file with the current date as the filename"""
    date_string = datetime.now().strftime('%Y-%m-%d')
    filename = f'article_data_{date_string}.xlsx'
    df.to_excel(filename, index=False)

def main():
    # Call the functions to execute the program
    articles = scrape_articles_data(url, headers, pages)
    df = create_dataframe(articles)
    df = clean_dataframe(df)
    save_dataframe_csv(df)
    save_dataframe_excel(df)
    print(df)


if __name__ == '__main__':
    main()







