import json
import requests

# Armazena o json em um dicionario
with open('base_tdspy.json') as file:
    dicionario = json.load(file)

# Solicita o RM do usuário
rm = input("Digite o seu RM: ")

# Verifica se o RM informado existe no dicionário
if rm not in dicionario:
    print(f"RM {rm} não encontrado.")
else:

    for url in dicionario[rm]:
        try:
            response = requests.get(f"http://{url}")
            arquivo_html = response.content

            # Salva o HTML em um arquivo com nome baseado na URL
            with open(f"{url}.html", "wb") as arquivo_site:
                arquivo_site.write(arquivo_html)
            print(f"Arquivo {url}.html salvo com sucesso.")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
