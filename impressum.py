from nicegui import ui

class Impressum(ui.dialog):

    def __init__(self, *, value: bool = False) -> None:
        super().__init__(value=value)
        with self, ui.card():
            ui.markdown('### Impressum')
            ui.markdown('''
                #### Angaben gemäß § 5 TMG

                Moritz Heffter

                Zähringerstr. 13

                79331 Teningen
            ''')
            ui.markdown('''
                #### Kontakt

                Telefon: 0171 9386944

                E-Mail: [moritz_heffter@me.com](mailto:moritz_heffter@me.com)'''
            )
            ui.button('Schließen', on_click=self.close)
