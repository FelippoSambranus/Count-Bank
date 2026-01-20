import pyfiglet

def ASCII_WITH_COLOR(color: str, text: str, type=str):
    text_ascii = pyfiglet.figlet_format(text=text, font=type)
    result = color + text_ascii + '\033[0m'
    print(result)


class Interface:
    def __init__(self):
        self.__colors = {'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
        }
    def interface_menu_principal(self):
        print("\n")
        ASCII_WITH_COLOR(color= self.__colors['green'], text="Count Bank", type="alligator")
        print("#############################################################################")
        print('\n')
        print("     BEM VINDO AO COUNT BANK, POR FAVOR ESCOLHA UMA DAS OPÇÕES PARA COMEÇAR      ")
        print("\n")
        print("  [1] - ADCIONAR RECEITA/RECIBO AS CONTAS DESSE MỄS")
        print("  [2] - ADCIONAR DESPEZA AS CONTAS DESSE MỄS")
        print("  [3] - CRIAR PLANILHA PARA NOVO MÊS")
        print("  [4] - VIZUALIZAR SALDO LIVRE DISPONIVEL")
        print("  [5] - SAIR")
        print('\n')
        print("#############################################################################")

    def interface_add_receita(self):
        print('\n')
        ASCII_WITH_COLOR(color= self.__colors['green'], text="Count Bank", type="alligator")
        print("#############################################################################")
        ASCII_WITH_COLOR(color=self.__colors['yellow'], text="Add Receita", type="slant")
        print("#############################################################################")

    def interface_add_despeza(self):
        print('\n')
        ASCII_WITH_COLOR(color= self.__colors['green'], text="Count Bank", type="alligator")
        print("#############################################################################")
        ASCII_WITH_COLOR(color=self.__colors['red'], text="Add Despeza", type="slant")
        print("#############################################################################")

    def interface_criar_planilha(self):
        print('\n')
        ASCII_WITH_COLOR(color= self.__colors['green'], text="Count Bank", type="alligator")
        print("#####################################################################")
        ASCII_WITH_COLOR(color=self.__colors['blue'], text="Criar Planilha", type="slant")
        print("#####################################################################")

    def interface_vizu_cash_livre(self):
        print('\n')
        ASCII_WITH_COLOR(color= self.__colors['green'], text="Count Bank", type="alligator")
        print("#############################################################################")
        ASCII_WITH_COLOR(color=self.__colors['green'], text="Cash Livre", type="slant")
        print("#############################################################################")