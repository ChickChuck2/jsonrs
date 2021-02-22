import json

with open('data.json', 'r+') as f:
    data = json.load(f)

    idr = input("Id: ")

    mensagem = input("Mensagem: ")
    data['id'] = idr
    data['usuario'] = mensagem
    f.seek(0)
    json.dump(data, f)
    print(data)
