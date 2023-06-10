from dataclasses import dataclass
from pydantic import BaseModel

from qrcode import constants, QRCode
import io
import base64

err_const: dict = {
    '10%': constants.ERROR_CORRECT_L,
    '15%': constants.ERROR_CORRECT_M,
    '25%': constants.ERROR_CORRECT_Q,
    '30%': constants.ERROR_CORRECT_H
}

class QRParams(BaseModel):
    '''A class that contains the data for a qr code.'''
    content: str
    color: str = '#6698CF'
    bg_color: str = '#FFFFFF'
    version: int = 2
    error_const: str = '15%'
    box_size: int = 10
    border: int = 2
    image_string: str = ''

@dataclass
class QrCodeData:
    '''A class that contains the data for a qr code and the qr code object itself.qr_params.'''
    qr_params: QRParams
    qc: QRCode = QRCode()

    def set_border(self, border):
        '''set a border width'''
        self.qr_params.border = int(border)

    def set_version(self, version):
        '''set the size of the picture. Value has to be between 1 and 40'''
        if version > 40:
            self.qc.version = 40
        elif version < 1:
            self.qc.version = 1
        else:
            self.qc.version = version

    def set_box(self, size):
        '''set the size of the qr code'''
        self.qr_params.box_size = int(size)

    def set_url(self, content):
        '''set the content of the qr code'''
        self.qr_params.content = content

    def set_color(self, color):
        '''set a color, default is black'''
        self.qr_params.color = color

    def set_bg_color(self, color):
        '''set a background color, default is white'''
        self.qr_params.bg_color = color
        #print(self.qr_params.color)

    def generate_qrcode(self) -> str:
        '''puts the qr code together and returns it as a base64 string'''

        # set params
        self.qc.version = self.qr_params.version
        if self.qr_params.error_const in err_const.keys():
            self.qc.error_correction = err_const[self.qr_params.error_const]
        else:
            self.qc.error_correction = err_const['15%']
        self.qc.border = self.qr_params.border
        self.qc.box_size = self.qr_params.box_size

        self.qc.add_data(self.qr_params.content)

        self.qc.make(fit=True)
        img = self.qc.make_image(fill_color=self.qr_params.color, back_color=self.qr_params.bg_color)

        out = io.BytesIO()
        img.save(out, format='PNG')

        self.qr_params.image_string = base64.b64encode(out.getvalue()).decode()

        return self.qr_params.image_string
