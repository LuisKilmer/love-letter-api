import requests
import csv
import os

class SEADParaibaCSV:
    def __init__(self):
        self.base_url = "https://api.dadosabertos.codata.pb.gov.br/api/v1/remuneracao"
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def buscar_pagina(self, ano, mes, pagina):
        """Busca uma página específica da API."""
        url = f"{self.base_url}/servidor"
        params = {
            "ano": str(ano),
            "mes": str(mes).zfill(2),
            "page": pagina
        }
        
        response = self.session.get(url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro ao buscar página {pagina}. Status: {response.status_code}")
            return None

    def localizar_lista(self, dados_json):
        """Descobre dinamicamente em qual chave a API guardou a lista de servidores."""
        if isinstance(dados_json, list):
            return dados_json
            
        if isinstance(dados_json, dict):
            for chave, valor in dados_json.items():
                if isinstance(valor, list):
                    return valor
        return []

    def exportar_para_csv(self, ano, mes):
        """
        Busca os dados de todas as páginas e salva em um arquivo CSV.
        """
        nome_arquivo = f"servidores_pb_{ano}_{str(mes).zfill(2)}.csv"
        
        print(f"Iniciando extração. Os dados serão salvos em: {nome_arquivo}\n")

        # Variáveis de controle
        arquivo_csv = None
        escritor = None
        cabecalhos = []
        pagina = 1 # Inicializa a contagem de páginas

        while True:
            print(f"Baixando página {pagina}...")
            dados = self.buscar_pagina(ano, mes, pagina)
            
            if not dados:
                print("Falha na requisição. Encerrando busca.")
                break
                
            lista_servidores = self.localizar_lista(dados)
            
            # Condição de parada: Se a lista vier vazia, chegamos ao fim dos dados
            if not lista_servidores:
                print(f"A lista de servidores na página {pagina} veio vazia. Fim da extração.")
                break
                
            # Processa cada servidor da página atual
            for servidor in lista_servidores:
                # Se for o primeiro registro encontrado, extraímos os cabeçalhos
                if not cabecalhos:
                    cabecalhos = list(servidor.keys())
                    
                    # Abre o arquivo CSV para escrita
                    arquivo_csv = open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig")
                    escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos, delimiter=";")
                    escritor.writeheader()

                # Escreve a linha no CSV
                escritor.writerow(servidor)
            
            # Avança para a próxima página
            pagina += 1

        # Garante o fechamento do arquivo no final
        if arquivo_csv:
            arquivo_csv.close()

        # O total de páginas baixadas com sucesso será (pagina - 1)
        total_paginas = pagina - 1
        print(f"\nExtração concluída com sucesso! Total de páginas processadas: {total_paginas}")
        print(f"Arquivo salvo no caminho: {os.path.abspath(nome_arquivo)}")


# --- Execução do Código ---
if __name__ == "__main__":
    extrator = SEADParaibaCSV()
    
    # Extraindo dados de Outubro de 2025 de forma dinâmica (todas as páginas)
    extrator.exportar_para_csv(ano=2025, mes=10)