from nicegui import ui
from qr_code_helpers import QrCodeData

qr_data = QrCodeData('')

def set_color(e):
    qr_data.color = e
    color_chooser.style(f'background-color:{e}!important')

def set_size(e):
    qr_data.set_box(e.value)
    if rand.value >= size.value:
        rand.value = size.value - 1

def gen_qc_img():
    img_b64 = qr_data.generate_qrcode()
    img_string = f'''<img src="data:image/png;base64,{img_b64}" style=""></img>'''
    image_html.set_content(img_string)

with ui.row():
    with ui.column().style('width:350px'):
        with ui.card().tight() as container:
            #container.classes("divide-y")
            with ui.card_section():
                with ui.column():
                    ui.label('URL oder Inhalt des QR-Codes:')
                    content_input = ui.input(label='Text', placeholder='URL eingeben',
                            on_change=lambda e: qr_data.set_url(e.value),
                            validation={'Input too long': lambda value: len(value) < 200},
                            ).style('width:100%')

            with ui.card_section():
                with ui.column():
                    with ui.row():
                        with ui.column().style('width:60%'):
                            ui.label('Größe und Rand:')
                            with ui.row():
                                size = ui.number(label='Größe', value=10, format='%.0f', min=1,
                                            on_change=lambda e: set_size(e)).style('width:40%')
                                rand = ui.number(label='Rand', value=4, format='%.0f', min=0,
                                            on_change=lambda e: qr_data.set_border(e.value)).style('width:40%')
                        with ui.column():
                            ui.label('Farbe wählen:')
                            picker = ui.color_picker(on_pick=lambda e: set_color(e.color))
                            color_chooser = ui.button(on_click=picker.open).props('icon=palette')
                    with ui.column():
                        with ui.label('Wie viel Fehlertoleranz soll der Code haben:'):
                            ui.tooltip("Beispiel: Bis zu 15% des Codes sind unlesbar, trotzdem funktioniert der Code noch.").classes('bg-green')
                        robustness = ui.radio(['10%', '15%', '25%', '30%'], value='15%').props('inline')
            with ui.card_section():
                #async def gen_qc():button_geng = 
                ui.button('QR-Code erstellen!', on_click=lambda: gen_qc_img())

    with ui.column():
        with ui.card().tight() as result:
            with ui.row():
                image_html = ui.html()

ui.run(title='QR Code Generator')