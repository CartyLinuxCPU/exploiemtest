import os
import socket
import time
from tqdm import tqdm
from tabulate import tabulate

limpar_tela = "clear"
os.system(limpar_tela)

while True:
    time.sleep(1)
    enter = "enter"
    def loading():
        for _ in tqdm(range(100), desc="Carregando.. ", ascii=False, ncols= 80):
            os.system(enter)
            time.sleep(0.1)
        time.sleep(2)        
        print("\nFinalizado!!")
    
    if __name__ == "__main__":
        loading()
        break

time.sleep(5)
limpar = "clear"
os.system(limpar)


def banner_key(): 
    print("""
 ██████╗ █████╗ ██████╗ ████████╗██╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║     ███████║██████╔╝   ██║    ╚████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
██║     ██╔══██║██╔══██╗   ██║     ╚██╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
╚██████╗██║  ██║██║  ██║   ██║      ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                         
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
[Instagram]: [@cartyslackware]
[Facebook]: [Cxrty Slackware]
[GitHub]: [CartyLinuxCPU]                                                     
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=""")
banner_key()
menu = '\nMENU\n\n[1] = Port Scan\n[2] = Exploit\n[3] = SAIR\n' 
print(menu)

op = input("Selecione a opção >>> ")

portas = [20, 21, 22, 23, 25, 80, 110, 123, 156, 161, 179, 443, 1863, 3128, 3389, 8080]


try:
    if op == "1":
        def loading():
            for _ in tqdm(range(10000),desc="Carregando.. ", ascii=False, ncols= 80):
                time.sleep(0.1)
        time.sleep(0.1)        
        print("\nFinalizado!!")
    
    if __name__ == "__main__":
        loading()
        

        time.sleep(3)
        tempo_ok = 'clear'
        os.system(tempo_ok)
        def banner():
            print("""

██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║1
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
            
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
[Instagram]: [@cartyslackware]
[Facebook]: [Cxrty Slackware]
[GitHub]: [CartyLinuxCPU]                                                     
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=""")

        banner()
        while True:
            website = input("\nSelecione >>> ")

            for porta in portas:
                clientes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientes.settimeout(0.8)
                total = clientes.connect_ex((website, porta))
                if total == 0:
                    
                    print("\n||WebSites: ||", website, "||Protocolo IP: ||", porta, "||Aberto ||")

            
                else:
                    print("||WebSites: ||", website, "||Protocolo IP: ||", porta, "||Fechado ||")

    
    else:
        pass


except Exception as error:
    print("Tentativa de ERROR", error)                