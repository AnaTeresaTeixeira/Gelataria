import PySimpleGUI as sg

class TelaRec:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout (lista)
        layout = [
            [sg.Text('Data', size=(20,0)), sg.Input(size=(25,0), key='data')],
            [sg.Text('Nome', size=(20,0)), sg.Input(size=(25,0), key='nome')],
            [sg.Text('Descrição')],
            [sg.Input(size=(25,0), key='des')],
            [sg.Button('Guardar')],
            [sg.Output((48,10))]
        ]

        # Janela
        self.janela = sg.Window('Dados de reclamação: ', layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            data = self.values['data']
            nome = self.values['nome']
            des = self.values['des']

            print(f'Data: {data}')
            print(f'Nome: {nome}')
            print(f'Descrição: {des}')       
      
tela = TelaRec()
tela.Iniciar()



