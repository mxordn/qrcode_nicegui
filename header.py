#!/usr/bin/env python3

from nicegui import ui

class QRHeader(ui.header):

    def __init__(self, *, value: bool = True, fixed: bool = True, bordered: bool = False,
                 elevated: bool = False) -> None:
        super().__init__(value=value, fixed=fixed, bordered=bordered, elevated=elevated)

        with self:
            ui.label('QR Code Generator').classes('text-m')
            ui.icon('qr_code_2')
