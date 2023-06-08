#!/usr/bin/env python3
import json
from fastapi import FastAPI
import frontend_main
from qr_code_helpers import QrCodeData, QRParams


qrcode_app = FastAPI(title='QR Code API')

@qrcode_app.post('/qrcode/api')
def qrcode_api(qr_data: QRParams):
    qcd = QrCodeData(qr_data)
    return qcd.generate_qrcode()

@qrcode_app.get('/qrcode/info')
def info():
    return json.dumps({
        'Hello': 'World',
        'version': 0.1})

frontend_main.init(qrcode_app)
