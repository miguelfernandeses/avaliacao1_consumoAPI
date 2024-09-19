import requests


def obter_dados_usuario_github(username):
    url = f'https://api.github.com/users/{username}'
    

    try:
        response = requests.get(url)
        response.raise_for_status() # Levanta um erro para códigos de status 4xx/5xx
        data = response.json()


        if"message" in data and data["message"] == "Not Found":
            print("Usuário não encontrado!")
            return None
        
        return data
    

    except requests.exceptions.RequestException as e:
        print(f'Erro ao acessar a API: {e}')
        return None
    

def exibir_dados_usuario(data):
    if data:
        print(f'\n Nome completo: {data.get("name", "Não disponível")}')
        
        print(f'Bio: {data.get("bio", "Não disponível")}')
        print(f'Localização: {data.get("location", "Não disponível")}')
        print(f'Seguidores: {data.get("followers", 0)}')
        print(f'Seguindo: {data.get("following", 0)}')
    else:
        print('Não foi possível encontrar o usuario!')

def main():
    print('GitHub Users\n')
    username = input('Qual é o nome do usuário?').strip()


    if not username:
        print('Nome de usuário inválido!')
        return
    
    dados_usuario = obter_dados_usuario_github(username)
    exibir_dados_usuario(dados_usuario)


if __name__ == "__main__":
    main()