import qrcode
import io
import base64

err_const: dict = {
    '10%': qrcode.constants.ERROR_CORRECT_L,
    '15%': qrcode.constants.ERROR_CORRECT_M,
    '25%': qrcode.constants.ERROR_CORRECT_Q,
    '30%': qrcode.constants.ERROR_CORRECT_H
}

def generate_qrcode(url, color, error_corr='15%'):
    qc = qrcode.QRCode(
        version=10,
        error_correction=err_const[error_corr],
        box_size=10,
        border=4)
    
    print(url.value, color, error_corr, err_const[error_corr])
    
    qc.add_data(url.value)
    qc.make(fit=True)

    img = qc.make_image(fill_color=(color))

    out = io.BytesIO()
    img.save(out, format='PNG')

    img_b64 = base64.b64encode(out.getvalue()).decode()

    return img_b64
