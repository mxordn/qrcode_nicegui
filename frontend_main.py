from nicegui import ui
from fastapi import FastAPI
from qr_code_helpers import QrCodeData, QRParams
from impressum import Impressum
from header import QRHeader

def init(app: FastAPI) -> None:
    @ui.page('/qrcode')
    def qrcode_frontend():
        qr_data = QRParams(content='')
        qcd = QrCodeData(qr_data)

        def gen_qc_img():
            img_b64 = qcd.generate_qrcode()
            img_string = f'''<img src="data:image/png;base64,{img_b64}" style=""></img>'''
            image_html.set_content(img_string)

        def set_color(e):
            qcd.set_color(e)
            color_chooser.style(f'background-color:{e}!important')

        def set_bg_color(e):
            qcd.set_bg_color(e)
            bg_color_chooser.style(f'background-color:{e}!important')

        header = QRHeader()
        with ui.grid(columns=2).style('height:460px'):
            with ui.column().style('width:350px'):
                with ui.card().tight():
                    with ui.card_section():
                        ui.label('Einstellungen').classes('text-xl')

                    with ui.card_section():
                        with ui.column():
                            ui.label('URL oder Inhalt des QR-Codes:')
                            ui.input(label='Text für den QR Code', placeholder='URL eingeben',
                                    on_change=lambda e: qcd.set_url(e.value),
                                    validation={'Input too long': lambda value: len(value) < 200},
                                    ).style('width:100%')

                    with ui.card_section():
                        with ui.column():
                            ui.markdown('**Größen und Rand:**')
                            with ui.row():
                                ui.number(label='Größe des Codes', value=3, format='%.0f', min=1, max=40,
                                                    on_change=lambda e: qcd.set_version(e.value)).style('width:30%')
                                ui.number(label='Kästchengröße', value=10, format='%.0f', min=1,
                                            on_change=lambda e: qcd.set_box(e.value)).style('width:30%')
                                ui.number(label='Rand', value=2, format='%.0f', min=0,
                                            on_change=lambda e: qcd.set_border(e.value)).style('width:20%')
                            ui.markdown('**Farben wählen:**')
                            with ui.row():
                                with ui.column():
                                    ui.label('QR Code')
                                    picker = ui.color_picker(on_pick=lambda e: set_color(e.color))
                                    color_chooser = ui.button(on_click=picker.open).props('icon=palette')
                                with ui.column():
                                    ui.label('Hintergrund')
                                    picker_bg = ui.color_picker(on_pick=lambda e: set_bg_color(e.color))
                                    bg_color_chooser = ui.button(on_click=picker_bg.open).props('icon=colorize')

                            with ui.label('Wie viel Fehlertoleranz soll der Code haben:'):
                                ui.tooltip("Beispiel: Bis zu 15% des Codes sind unlesbar, trotzdem funktioniert der Code noch.").classes('bg-green')
                            ui.radio(['10%', '15%', '25%', '30%'], value='15%').props('inline')
                    with ui.card_actions():
                        ui.button('QR-Code erstellen!', on_click=lambda: gen_qc_img())

            with ui.column().style('width:100%-350px'):
                with ui.card().tight():
                    with ui.card_section():
                        image_html = ui.html('')
        with ui.footer():
            di = Impressum()
            ui.button('Impressum', on_click=di.open).classes('flat')

    ui.run_with(app, title='QR Code Generator')
