from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [ 
    {"nome": "Coca-cola", "descricao": "veneno", "preco": "10,00", "imagem": "https://choppmaisfacil.com.br/image/cache/catalog/produtos/Refrigerantes/1648036735_1SZ-1000x1000.jpg"},
    {"nome": "Doritos", "descricao": "suja mão", "preco": "6,00", "imagem": "https://images-americanas.b2w.io/produtos/01/00/img3/33584764/9/3358476409_1GG.jpg"},
    {"nome": "Água", "descricao": "mata sede", "preco": "2,00", "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYF7-2U3rCX7CXaDcc9A0YtSpl7ngJbm0PqQ&s"}
]

app = Flask("minha app")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)

    return "produto não existe"

@app.route ("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

#POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome=request.form['nome']
    descricao=request.form['descricao']
    preco=request.form['preco']
    imagem=request.form['imagem']
    produto= {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))


#app.run(port=5001)

