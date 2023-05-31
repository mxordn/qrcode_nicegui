from nicegui import ui
from qr_code_helpers import generate_qrcode

container = ui.card().tight()
content = ui.column()
params = {'url': '', 'chosen_color': '#000000', 'img': ''}

def set_url(e):
    params['url'] = e

def set_color(e):
    params['chosen_color'] = e
    color_chooser.style(f'background-color:{e}!important')

def gen_qc_img():
    img_b64 = generate_qrcode(params['url'], params['chosen_color'], robustness.value)
    params['img'] = f'''<img src="data:image/png;base64,{img_b64}" style="width:50%"></img>'''
    image_html.set_content(params['img'])

    #params['img'] = img

with ui.row():
    with ui.card().tight() as container:
        container.classes("divide-y")
        with ui.card_section():
            with ui.column():
                ui.label('URL oder Inhalt des QR-Codes:')
                content_input = ui.input(label='Text', placeholder='URL eingeben',
                        on_change=lambda e: set_url(e),
                        validation={'Input too long': lambda value: len(value) < 200},
                        ).style('width:100%')

        with ui.card_section():
            with ui.column():
                with ui.column():
                    with ui.label('Wie viel Fehlertoleranz soll der Code haben:'):
                        ui.tooltip("Beispiel: Bis zu 15% des Codes sind unlesbar, trotzdem funktioniert der Code noch.").classes('bg-green')
                    robustness = ui.radio(['10%', '15%', '25%', '30%'], value='15%').props('inline')
                with ui.column():
                    ui.label('Farbe wählen:') 
                    picker = ui.color_picker(on_pick=lambda e: set_color(e.color))
                    color_chooser = ui.button(on_click=picker.open).props('icon=palette')
        
        with ui.card_section():
            #async def gen_qc():button_geng = 
            ui.button('QR-Code erstellen!', on_click=lambda: gen_qc_img())

    image_html = ui.html()
ui.run(title='QR Code Generator')