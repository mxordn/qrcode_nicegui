from dataclasses import dataclass, field
import qrcode
import io
import base64

err_const: dict = {
    '10%': qrcode.constants.ERROR_CORRECT_L,
    '15%': qrcode.constants.ERROR_CORRECT_M,
    '25%': qrcode.constants.ERROR_CORRECT_Q,
    '30%': qrcode.constants.ERROR_CORRECT_H
}

@dataclass
class QrCodeData:
    '''A class that contains the data for a qr code and the qr code object itself.'''
    content: str
    color = '#000000'
    version = 10
    error_const = err_const['15%']
    box_size: int = 10
    border: int = 4
    qc = qrcode.QRCode()

    def set_border(self, border):
        '''set a border width'''
        self.border = int(border)

    def set_box(self, size):
        '''set the size of the qr code'''
        self.box_size = int(size)

    def set_url(self, content):
        '''set the content of the qr code'''
        self.content = content

    def set_color(self, color):
        '''set a color, default is black'''
        self.color = color
        print(self.color)

    def generate_qrcode(self) -> str:
        '''puts the qr code together and returns it as a base64 string'''
        self.qc.version = self.version
        self.qc.error_correction = self.error_const

        self.qc.border = self.border
        self.qc.box_size = self.box_size

        self.qc.add_data(self.content)
        #print(self)
        self.qc.make(fit=True)
        img = self.qc.make_image(fill_color=self.color)

        out = io.BytesIO()
        img.save(out, format='PNG')

        img_b64 = base64.b64encode(out.getvalue()).decode()

        return img_b64
