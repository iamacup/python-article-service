from flask import Flask, request
from newspaper import Article
import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    req_data = request.get_json()
    html = ""

    try:
        html = req_data["html"]
    except:
        return '{"error": true, "message": "missing input: html"}'

    article = Article("")
    article.download(html)

    article.parse()
    article.nlp()

    output = {
        "text": article.text,
        "authors": article.authors,
        "publish_date": article.publish_date,
        "top_image": article.top_image,
        "movies": article.movies,
        "keywords": article.keywords,
        "summary": article.summary,
    }

    out = json.dumps(output, default = myconverter)
    return out

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

app.run(debug=True, port=5000, host='0.0.0.0')
