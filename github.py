import requests

print('GitHub Users\n')

username = input('Qual é o nome do usuario?')

print(username)

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    #print(data)
    print(f'\n Nome completo: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'localização: {data["location"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
else:
    print('Não foi possível encontrar o usuario!')

