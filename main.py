from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

print(NEWS_API_KEY)

app = Flask(__name__)

@app.route('/') 
def index():
    query = request.args.get('query', 'latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])

    filtered_articles = [
        article for article in articles 
        if 'Yahoo' not in article['source']['name'] and 'removed' not in article['title'].lower()
    ]

    return render_template('base.html', articles=filtered_articles, query=query)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port = 5050)
