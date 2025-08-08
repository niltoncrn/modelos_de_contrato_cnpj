import requests
from tkinter import *
import tkinter as tk
import re

def gerar_escopo():
    cnpj = entrada_cnpj.get()  
    remover = [".","/","-"]
    for caracteres  in remover:
        cnpj = cnpj.replace(caracteres,"")

    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    response = requests.get(url)

    if response.status_code==200:
        dados = response.json()

    dados_empresarial = {
        'nome_empresarial': dados.get('nome', ''),
            'logradouro': dados.get('logradouro', ''),
            'numero': dados.get('numero', ''),
            'bairro': dados.get('bairro', ''),
            'cep': dados.get('cep', ''),
            'cidade': dados.get('municipio', ''),
            'uf': dados.get('uf', ''),
            'cnpj': dados.get('cnpj', '')
        }
    
    escopo = entrada_escopo.get("1.0",tk.END).strip()
    chaves = re.findall(r"{(.*?)}",escopo)

    for chave in chaves:
        valor = dados_empresarial.get(chave,f"[{chave}, não encontrada]")
        escopo = escopo.replace(f"{{{chave}}}", valor)

    escopo_final.delete("1.0",tk.END)
    escopo_final.insert(tk.END,escopo)

janela = Tk()
janela.title("Montador de escopo para contratos com CNPJ")
janela.geometry("600x600")

dados_empresa = tk.Frame(janela)
dados_empresa.pack(anchor="center")
tk.Label(dados_empresa, text="CNPJ: ", font=("Arial", 12)).grid(row=0, column=0, padx=0, pady=10, sticky="W") 
entrada_cnpj = tk.Entry(dados_empresa, width=60, font=("Arial", 12))
entrada_cnpj.grid(row=1, column=0, padx=0, pady=0)

dados_escopo = tk.Frame(janela)
dados_escopo.pack(anchor="center")
tk.Label(dados_escopo, text="Formato do escopo: ", font=("Arial", 12)).grid(row=0, column=0, padx=0, pady=10, sticky="W")
entrada_escopo = tk.Text(dados_escopo, width=60, height=10, font=("Arial", 12))
entrada_escopo.grid(row=1, column=0, columnspan=2, padx=0, pady=0)

escopo_feito = tk.Frame(janela)
escopo_feito.pack(anchor="center")
tk.Label(escopo_feito, text="Escopo completo com as informações: ", font=("Arial", 12)).grid(row=0, column=0, padx=0, pady=10, sticky="W")
escopo_final = tk.Text(escopo_feito, width=60, height=10, font=("Arial", 12))
escopo_final.grid(row=1, column=0, columnspan=2, padx=0, pady=0)



btns = tk.Frame(janela)
btns.pack(anchor="center", pady=10)
btn_gerar = tk.Button(btns, text="Gerar Escopo", command=gerar_escopo)
btn_gerar.pack(side="left", padx=5)



janela.mainloop()


