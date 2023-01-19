from flask import Flask, make_response
from io import BytesIO
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return "<h4 style='font-family: Verdana'>Example URL: /api/www.example.com </h1>"

@app.route("/api/<string:url>")
def convert(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Create the response object with the appropriate headers
    response = make_response(img_io.getvalue())
    response.content_type = 'image/png'
    return response

if __name__ == "__main__":
    app.run()