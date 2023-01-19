from flask import Flask, request, jsonify
import qrcode

app = Flask(__name__)

@app.route('/qrcode', methods=['POST'])
def generate_qrcode():
    text = request.json['text']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

if __name__ == '__main__':
    app.run()