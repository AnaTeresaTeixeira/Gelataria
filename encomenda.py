import PySimpleGUI as sg
import pandas as pd

from datetime import datetime
from datetime import date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

today = date.today()
today = str(today)

# localizar ficheiro excel
exceldados = pd.read_excel("Gelados.xlsx", sheet_name='Folha1')
sabores = exceldados['Sabores']
precos = exceldados['Preços']

def iva(preco):
    preco_final= (preco*0.23) + preco
    return round(preco_final, 2)

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout (lista)
        layout = [
            [sg.Text(current_time + ' | ' + today)],
            [sg.Text('Nome', size=(20,0)), sg.Input(size=(25,0), key='nome')],
            [sg.Text('Sabor do gelado', size=(20,0)), sg.Combo(sabores.tolist(), size=(23,0), key='sabor')],
            [sg.Text('Preço', size=(20,0)), sg.Combo(precos.tolist(), size=(23,0), key='preco')],
            [sg.Text('Número de bolas', size=(20,0)), sg.Input(size=(25,0), key='numBolas')],
            [sg.Text('Adicionar topping')],
            [sg.Radio('Sim', 'topping', key='addTopping'), sg.Radio('Não', 'topping', key='notAddTopping')],
            [sg.Text('Tipo de casca')],
            [sg.Radio('Chocolate', 'casca', key='cascaChocolate'), sg.Radio('Sem lactose', 'casca', key='cascaSLactose'), sg.Radio('Tradicional', 'casca', key='cascaTradicional')], 
            [sg.Button('Ok', size=(10))],
            [sg.Output((48,10))]
        ]

        # Janela
        self.janela = sg.Window('Dados de compra: ', layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            sabor = self.values['sabor']
            preco = self.values['preco']
            numBolas = self.values['numBolas']
            addTopping = self.values['addTopping'] 
            notAddTopping = self.values['notAddTopping']
            cascaChocolate = self.values['cascaChocolate']
            cascaSLactose = self.values['cascaSLactose']
            cascaTradicional = self.values['cascaTradicional']

            print(f'Nome: {nome}')
            print(f'Sabor do gelado: {sabor}')       
            print(f'Número de bolas: {numBolas}')

            if(addTopping):
                print(f'Adicionar topping: Sim')
            else:
                print(f'Adicionar topping: Não')

            if(cascaChocolate):
                print(f'Casca de chocolate')
            elif(cascaSLactose):
                print(f'Casca sem lactose')
            else:
                print(f'Casca tradicional')

            print(f'Valor final: {iva(preco)}€\n\n')

tela = TelaPython()
tela.Iniciar()


