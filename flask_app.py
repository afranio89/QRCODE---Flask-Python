from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html', titulo='Gerador de QrCode')


@app.route('/qr_code', methods=['POST'])
def generate_qr_code():

    data = request.form['link']

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    qr_img_bytes = base64.b64encode(buf.getvalue())


    return render_template('qr_code.html', titulo='Gerador de QrCode', qr_image=qr_img_bytes.decode('utf-8'), link=data)
  
if __name__ == '__main__':
    app.run(debug=True)
