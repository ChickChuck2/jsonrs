id = input("NewID: ")

with open('data.json', 'r') as outfile:
    servers = json.load(outfile)
servers[str(id)] = id
with open('data.json', 'w') as outfile:
    json.dump(servers, outfile)
