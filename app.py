from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.wykop.pl/cdn/c3201142/comment_VSiOQHuNcsiiNMQBBFppopIqcrXSx7oJ.jpg",
    "https://d-tm.ppstatic.pl/kadry/74/fb/c7a0d57fc87191ff3e91fb3a9dd9.1000.jpg",
    "http://ganjafarmer.com.pl/img/cms/TrailerParkBoys-1.jpg",
    "https://i.pinimg.com/474x/5b/58/cb/5b58cb8194857810642a371a0abe691d.jpg",
    "https://data4.cupsell.pl/upload/generator/276575/640x420/4870607_print_1.png?resize=max_sizes&key=55f9a22768eed085006592c1174c0235"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")