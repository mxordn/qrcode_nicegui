#!/usr/bin/env python3

'''QR Code Api base module'''
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse

import frontend_main
from qr_code_helpers import QrCodeData, QRParams


qrcode_app = FastAPI(title='QR Code API')

@qrcode_app.get('/')
def index():
    '''root path with redirect to /home'''
    return RedirectResponse('https://satzlehre-online.de/qrcode/home', status_code=307)
    #{'data': 'Hello, World'}

@qrcode_app.post('/api')
def qrcode_api(qr_data: QRParams) -> JSONResponse:
    '''POST method for the api. Takes QRParams as a JSON body'''
    qcd = QrCodeData(qr_data)
    return JSONResponse(content={'data': qcd.generate_qrcode()})

@qrcode_app.get('/api')
def qrcode_api_home() -> HTMLResponse:
    '''GET method for the api path. Shows a small html page with a link to the docs'''
    return HTMLResponse(content='''
        <html>
            <h1>QR Code API</h1>
            <div>
                <a href="https://satzlehre-online.de/qrcode/docs">Hier geht es zur API Dokumentation</a>
            </div>
        </html>
        ''')

@qrcode_app.get('/info')
def info():
    return JSONResponse(content={
        'app': 'QR Code Generator',
        'version': 0.2})

frontend_main.init(qrcode_app)
