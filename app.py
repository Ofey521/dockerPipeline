from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.wykop.pl/cdn/c3201142/comment_VSiOQHuNcsiiNMQBBFppopIqcrXSx7oJ.jpg",
    "https://d-tm.ppstatic.pl/kadry/74/fb/c7a0d57fc87191ff3e91fb3a9dd9.1000.jpg",
    "https://i.ytimg.com/vi/Am3yN5ze0Mw/maxresdefault.jpg",
    "https://img.joemonster.org/mg/albums/082020/main_26boskie_kszta_ty.jpg",
    "https://www.wykop.pl/cdn/c3201142/comment_1601153376JXqV5AvIngw0wFhBMidHYR,w1200h627f.jpg"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")