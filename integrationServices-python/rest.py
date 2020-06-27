import requests

def consulta():
    response = requests.get('uri')
    print(response.status_code)
    print(response.json)
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'], pessoa['idade'])

def insere():
    nome = 'Paulo'
    idade = 44
    pessoa = {"nome": nome, "idade": idade}
    response = requests.post('uri', json=pessoa)
    print(response.status_code)
    print(response.json())


insere()
consulta()