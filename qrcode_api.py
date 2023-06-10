#!/usr/bin/env python3
import json
from fastapi import FastAPI

import frontend_main
from qr_code_helpers import QrCodeData, QRParams


qrcode_app = FastAPI(title='QR Code API')

@qrcode_app.get('/')
def index():
    return {'data': 'Hello, World'}

@qrcode_app.post('/home/api')
def qrcode_api(qr_data: QRParams) -> str:
    qcd = QrCodeData(qr_data)
    return qcd.generate_qrcode()

@qrcode_app.get('/home/info')
def info():
    return json.dumps({
        'app': 'QR Code Generator',
        'version': 0.2})

frontend_main.init(qrcode_app)
