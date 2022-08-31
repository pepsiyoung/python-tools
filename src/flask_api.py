import io

from flask import Flask, request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/im", methods=["POST"])
def image():
    im_file = request.files["image"]
    im_bytes = im_file.read()
    im = Image.open(io.BytesIO(im_bytes))
    im.show()
    im.save('/Users/pepsiyoung/Downloads/source/sss.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
