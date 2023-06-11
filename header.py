#!/usr/bin/env python3

from nicegui import ui

from impressum import Impressum
from frontend_main import QRParams

class QRHeader(ui.header):
    '''THe Header class for the frontend'''
    def __init__(self, *, value: bool = True, fixed: bool = True, bordered: bool = False,
                 elevated: bool = False, qrdata: QRParams | None = None) -> None:
        super().__init__(value=value, fixed=fixed, bordered=bordered, elevated=elevated)
        self.qrdata = qrdata

        with self:
            with ui.button(on_click=lambda: menu.open()).props('flat color=white icon=menu'):
                dimp = Impressum()
                with ui.menu() as menu:
                    ui.menu_item('Clear QR Code', lambda: self.reset_img_string())
                    ui.separator()
                    ui.menu_item('Impressum', lambda: dimp.open())
            ui.label('QR Code Generator').classes('text-xl')
            ui.icon('qr_code_2', size='36px').classes('content-center')
        
    def reset_img_string(self):
        '''reset the qr code image '''
        if isinstance(self.qrdata, QRParams):
            self.qrdata.image_string = ''
