import PySimpleGUI as sg

class TelaRec:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout (lista)
        layout = [
            [sg.Text('Nome', size=(20,0)), sg.Input(size=(25,0), key='nome')],
            [sg.Text('Cargo', size=(20,0)), sg.Input(size=(25,0), key='cargo')],
            [sg.Text('Salário', size=(20,0)), sg.Input(size=(25,0), key='salario')],
            [sg.Button('Guardar')],
            [sg.Output((48,10))]
        ]

        # Janela
        self.janela = sg.Window('Dados do funcionário: ', layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            cargo = self.values['cargo']
            salario = self.values['salario']

            print(f'Nome: {nome}')
            print(f'Cargo: {cargo}')    
            print(f'Salário: {salario}')

tela = TelaRec()
tela.Iniciar()


