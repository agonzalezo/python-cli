import io
import qrcode
import os

def gen_image(data):
    # img = qrcode.make('Some data here')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(60, 255, 51), back_color=(255, 255, 255))
    img.save("qr.png")
    os.system('ls qr.png|| dir qr.png')

def gen_ascii(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())