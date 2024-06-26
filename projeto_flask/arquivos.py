#ler

file=open("dados.txt")
print(file)
#print(file.read())
#conteudo=file.read()
#print(conteudo)
print(file.readlines())
file.close()

with open("dados.txt") as file:
    print(file.readlines())

with open("dados.txt", "w") as file:
    file.write("Banana verde")

with open("dados.txt", "a") as file:
    file.write("\nuvinha")

#lista_produtos => lista de dict (nome,decricao,preco,imagem)
#ler produtos.csv --->lista_produtos

def obter_produtos():
    with open("produtos.csv", "r") as file:
        lista_produtos = []
        for linha in file:
            nome, descricao, preco, imagem = linha.strip().split(",")
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "imagem": imagem
            }
            lista_produtos.append(produto)
        
        return lista_produtos

obter_produtos()

def adicionar_produto(p):
    with open("produtos.csv", "a") as file:
        linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
        file.write(linha)

p1 = {
    "nome": "Teclado Mecânico",
    "descricao":"Joga fora  acorda todos",
    "preco":250.00,
    "imagem":"teclado.jpg"
}

adicionar_produto(p1)

