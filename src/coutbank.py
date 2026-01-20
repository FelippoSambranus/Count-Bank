from src.interface import Interface
import csv
from datetime import datetime
from colorama import init, Fore, Style
import os
import sys

class Sistema:
    def __init__(self):
        self.__interface = Interface()

    def menu_principal(self):
        self.__interface.interface_menu_principal()

        descisao = input("DIGITE A OPÇÃO QUE DESEJA FAZER: ")

        if descisao == "1":
            os.system("clear")
            self.add_receita_atual()
        elif descisao == "2":
            os.system("clear")
            self.add_despeza_atual()
        elif descisao == "3":
            os.system("clear")
            self.criar_planilha_novo_mes()
        elif descisao == "4":
            os.system("clear")
            self.vizualizar_cash_livre()
        elif descisao == "5":
            os.system("clear")
            sys.exit()
        else:
            os.system("clear")
            self.menu_principal()
        
        
    def add_receita_atual(self):
        os.system("clear")
        today = datetime.now()
        month_now = today.month
        year_now = today.year
        archive_path = f'sheets/planilha_{month_now}_{year_now}.csv'
        nova_receita = {"Descricao": 0, "Valor": 0, "Tipo": 1}


        if (os.path.exists(archive_path)):
            with open(archive_path, "a") as file:
                writer = csv.writer(file)
                self.__interface.interface_add_receita()
                print("\n")
                Descricao = input("DIGITE A DESCRIÇÃO DO NOVO RECIBO DE DINHEIRO A SER ADCIONADO: ")
                Valor = float(input("DIGITE O VALOR DO DINHEIRO RECEBIDO: "))
                nova_receita ["Descricao"] = Descricao
                nova_receita["Valor"] = Valor

                writer.writerow(nova_receita.values())
            print("\n \n")
            print(f"RECEITA DE R${Valor} ADCIONADA COM SUCESSO!!")
            print("\n")
            desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            while (desc != "1"):
                os.system("clear")
                self.__interface.interface_add_receita()
                print("\n \n")
                print(f"RECEITA DE R${Valor} ADCIONADA COM SUCESSO!!")
                print("\n")
                desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
                

        else:
            with open(archive_path, "w") as file:
                colomns = ["Descricao", "Valor", "Tipo"]
                writer = csv.DictWriter(file, fieldnames=colomns)
                writer.writeheader()

                #....Somar o resto do mes passado...
                if (month_now == 1):
                    archive_path = f'sheets/planilha_12_{year_now - 1}.csv'
                else:
                    archive_path = f'sheets/planilha_{month_now - 1}_{year_now}.csv'

                if (os.path.exists(archive_path)):
                    ganho_total = 0
                    despezas_total = 0
                    with open(archive_path, "r") as file2:
                            reader = csv.DictReader(file2)

                            for row in reader:
                                if row["Tipo"] == "1":
                                    ganho_total += float(row["Valor"])
                                else:
                                    despezas_total += float(row["Valor"])
                    
                    add_row = {"Descricao": 0, "Valor": 0, "Tipo": 0}
                    if (ganho_total - despezas_total) >= 0:
                        add_row["Descricao"] = "SOBRA DE DINHEIRO MES PASSADO"
                        add_row["Valor"] = ganho_total - despezas_total
                        add_row["Tipo"] = 1
                        writer.writerow(add_row)
                    elif (ganho_total - despezas_total) < 0:
                        add_row["Descricao"] = "DESPEZAS DO MES PASSADO"
                        add_row["Valor"] = abs(ganho_total - despezas_total)
                        add_row["Tipo"] = 2
                        writer.writerow(add_row)       
                
                self.__interface.interface_add_receita()
                Descricao = input("DIGITE A DESCRIÇÃO DO NOVO RECIBO DE DINHEIRO: ")
                Valor = float(input("DIGITE O VALOR DO DINHEIRO RECEBIDO: "))
                nova_receita ["Descricao"] = Descricao
                nova_receita["Valor"] = Valor

                
                writer.writerow(nova_receita)
                
            print("\n \n")
            print(f"RECEITA DE R${Valor} ADCIONADA COM SUCESSO!!")
            print("\n")
            desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            while (desc != "1"):
                os.system("clear")
                self.__interface.interface_add_receita()
                print("\n \n")
                print(f"RECEITA DE R${Valor} ADCIONADA COM SUCESSO!!")
                print("\n")
                desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")

        os.system("clear")
        self.menu_principal()
                


    def add_despeza_atual(self):
        today = datetime.now()
        month_now = today.month
        year_now = today.year
        archive_path = f'sheets/planilha_{month_now}_{year_now}.csv'
        nova_despeza = {"Descricao": 0, "Valor": 0, "Tipo": 2}


        if (os.path.exists(archive_path)):
            with open(archive_path, "a") as file:
                writer = csv.writer(file)

                self.__interface.interface_add_despeza()

                Descricao = input("DIGITE A DESCRIÇÃO DA NOVA DESPEZA A SER ADCIONADA: ")
                Valor = float(input("DIGITE O VALOR DA DESPEZA: "))
                nova_despeza["Descricao"] = Descricao
                nova_despeza["Valor"] = Valor

                writer.writerow(nova_despeza.values())
            
            print("\n \n")
            print(f"DESPEZA DE R${Valor} ADCIONADA COM SUCESSO!!")
            print("\n")
            desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            while (desc != "1"):
                os.system("clear")
                self.__interface.interface_add_receita()
                print("\n \n")
                print(f"DESPEZA DE R${Valor} ADCIONADA COM SUCESSO!!")
                print("\n")
                desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
                
        else:
            with open(archive_path, "w") as file:
                colomns = ["Descricao", "Valor", "Tipo"]
                writer = csv.DictWriter(file, fieldnames=colomns)
                writer.writeheader()

                if (month_now == 1):
                    archive_path = f'sheets/planilha_12_{year_now - 1}.csv'
                else:
                    archive_path = f'sheets/planilha_{month_now - 1}_{year_now}.csv'

                if (os.path.exists(archive_path)):
                    ganho_total = 0
                    despezas_total = 0
                    with open(archive_path, "r") as file2:
                            reader = csv.DictReader(file2)

                            for row in reader:
                                if row["Tipo"] == "1":
                                    ganho_total += float(row["Valor"])
                                else:
                                    despezas_total += float(row["Valor"])
                    
                    add_row = {"Descricao": 0, "Valor": 0, "Tipo": 0}
                    if (ganho_total - despezas_total) >= 0:
                        add_row["Descricao"] = "SOBRA DE DINHEIRO MES PASSADO"
                        add_row["Valor"] = ganho_total - despezas_total
                        add_row["Tipo"] = 1
                        writer.writerow(add_row)
                    elif (ganho_total - despezas_total) < 0:
                        add_row["Descricao"] = "DESPEZAS DO MES PASSADO"
                        add_row["Valor"] = abs(ganho_total - despezas_total)
                        add_row["Tipo"] = 2
                        writer.writerow(add_row)

                self.__interface.interface_add_despeza()
                Descricao = input("DIGITE A DESCRIÇÃO DA NVOA DESPEZA: ")
                Valor = float(input("DIGITE O VALOR DA DESPEZA: "))
                nova_despeza["Descricao"] = Descricao
                nova_despeza["Valor"] = Valor

                writer.writerow(nova_despeza)

            print("\n \n")
            print(f"DESPEZA DE R${Valor} ADCIONADA COM SUCESSO!!")
            print("\n")
            desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            while (desc != "1"):
                os.system("clear")
                self.__interface.interface_add_receita()
                print("\n \n")
                print(f"DESPEZA DE R${Valor} ADCIONADA COM SUCESSO!!")
                print("\n")
                desc = input("DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")

        os.system("clear")
        self.menu_principal()

    def criar_planilha_novo_mes(self):
        os.system("clear")
        today = datetime.now()
        month_now = today.month
        year_now = today.year
        archive_path = f'sheets/planilha_{month_now}_{year_now}.csv'

        if (os.path.exists(archive_path)):
            self.__interface.interface_criar_planilha()
            print("----------------------------------------------------------------")
            print("PLANILHA JÁ CRIADA!")
            desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            print("----------------------------------------------------------------")
            while (desc != "1"):
                os.system("clear")
                self.__interface.interface_criar_planilha()
                print("----------------------------------------------------------------")
                print("PLANILHA JÁ CRIADA!")
                desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
                print("----------------------------------------------------------------")
            os.system("clear")
            self.menu_principal()
        else:
            columns = ["Descricao", "Valor", "Tipo"]
            with open(archive_path, "w") as file:
                writer = csv.DictWriter(file, fieldnames=columns)

                if (month_now == 1):
                    archive_path = f'../sheets/planilha_12_{year_now - 1}.csv'
                else:
                    archive_path = f'../sheets/planilha_{month_now - 1}_{year_now}.csv'

                if (os.path.exists(archive_path)):
                    ganho_total = 0
                    despezas_total = 0
                    with open(archive_path, "r") as file2:
                            reader = csv.DictReader(file2)

                            for row in reader:
                                if row["Tipo"] == "1":
                                    ganho_total += float(row["Valor"])
                                else:
                                    despezas_total += float(row["Valor"])
                    
                    add_row = {"Descricao": 0, "Valor": 0, "Tipo": 0}
                    if (ganho_total - despezas_total) >= 0:
                        add_row["Descricao"] = "SOBRA DE DINHEIRO MES PASSADO"
                        add_row["Valor"] = ganho_total - despezas_total
                        add_row["Tipo"] = 1
                        writer.writerow(add_row)
                    elif (ganho_total - despezas_total) < 0:
                        add_row["Descricao"] = "DESPEZAS DO MES PASSADO"
                        add_row["Valor"] = abs(ganho_total - despezas_total)
                        add_row["Tipo"] = 2
                        writer.writerow(add_row)
            
            self.__interface.interface_criar_planilha()
            print("----------------------------------------------------------------")
            print("PLANILHA JÁ CRIADA!")
            desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            print("----------------------------------------------------------------")

            while(desc != "1"):
                os.system("clear")
                self.__interface.interface_criar_planilha()
                print("----------------------------------------------------------------")
                print("PLANILHA JÁ CRIADA!")
                desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
                print("----------------------------------------------------------------")
            
        os.system("clear")
        self.menu_principal()


    def vizualizar_cash_livre(self):
        total_ganhos = 0
        total_despezas = 0
        today = datetime.now()
        month_now = today.month
        year_now = today.year
        archive_path = f'sheets/planilha_{month_now}_{year_now}.csv'

        with open(archive_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if (row["Tipo"] == "1"):
                    total_ganhos += float(row["Valor"])
                else:
                    total_despezas += float(row["Valor"])
        
        var_color = None
        if (total_ganhos - total_despezas > 0):
            var_color = Fore.GREEN
        else:
            var_color = Fore.RED

        self.__interface.interface_vizu_cash_livre()
        print("----------------------------------------------------------------")
        print("SEU SALDO LIVRE, CONTANDO RECIBOS E DESPEZAS É DE R$: " + var_color + f"{total_ganhos - total_despezas}" + '\033[0m')
        desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
        print("----------------------------------------------------------------")

        while (desc != "1"):
            os.system("clear")
            self.__interface.interface_vizu_cash_livre()
            print("----------------------------------------------------------------")
            print("SEU SALDO LIVRE, CONTANDO RECIBOS E DESPEZAS É DE R$: " + var_color + f"{total_ganhos - total_despezas}" + '\033[0m')
            desc = input("POR FAVOR, DIGITE (1) PARA RETORNAR AO MENU PRINCIPAL: ")
            print("----------------------------------------------------------------")
        
        os.system("clear")
        self.menu_principal()

