from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.wykop.pl/cdn/c3201142/comment_VSiOQHuNcsiiNMQBBFppopIqcrXSx7oJ.jpg",
    "https://d-tm.ppstatic.pl/kadry/74/fb/c7a0d57fc87191ff3e91fb3a9dd9.1000.jpg",
    "https://i.ytimg.com/vi/Am3yN5ze0Mw/maxresdefault.jpg",
    "http://ganjafarmer.com.pl/img/cms/TrailerParkBoys-1.jpg"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")