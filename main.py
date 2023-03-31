import PySimpleGUI as sg

def fencomenda():
    from encomenda import TelaPython
    tela = TelaPython()
    tela.Iniciar()

def ffuncionarios():
    from funcionario import TelaFun
    tela = TelaFun()
    tela.Iniciar()

def freclamacao():
    from reclamacao import TelaRec
    tela = TelaRec()
    tela.Iniciar()

class Menu:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue')
        # Layout (lista)
        layout = [
            [sg.Radio('Encomenda', 'menu', key='m_encomenda', size=(40))],
            [sg.Radio('Funcionários', 'menu', key='m_funcionarios')],
            [sg.Radio('Reclamação', 'menu', key='m_reclamacao')],
            [sg.Text()],
            [sg.Button('        Ok        ')],
        ]

        # Janela
        self.janela = sg.Window('Menu: ', layout)

    def IniciarM(self):
            
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            
            encomenda = self.values['m_encomenda']
            funcionarios = self.values['m_funcionarios']
            reclamacao = self.values['m_reclamacao']

            if(encomenda==True):
                fencomenda()
            elif(funcionarios==True):
                ffuncionarios()
            elif(reclamacao==True):
                freclamacao()
        
menu = Menu()
menu.IniciarM()

