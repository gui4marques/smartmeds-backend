from flask import Flask, jsonify, request
from inserir import insert_cliente
from atualizar import update_cliente
from deletar import delete_cliente
from consultar import read_cliente
from validar import vailadar_cliente
from fornecedor import validar_fornecedor
from itens_de_entrada import validar_itens_entrada
from itens_de_saida import validar_itens_saida
from localização import validar_localizacao
from pedido_entrada import validar_pedido_entrada
from pedido_saida import validar_pedido_saida
from produto import validar_produto
from estoque import validar_estoque


app = Flask(__name__)

fornecedor = []

@app.route("/")
def home():
    return "Bem-vindo à API da smartmeds!"

@app.route("/pedido de especificacoes", methods=["GET"])
def listar_fornecedor():
    return jsonify(fornecedor)

@app.route("/fornecedor", methods=["POST"])
def adicionar_fornecedor():
    novo_fornecedor = request.get_json()
    ret = validar_fornecedor(novo_fornecedor)
    if ret == True:
        return({"valido":True, "mensagem":"O login esta validado com sucesso!"})
    return({"valido":False, "mensagem":"O login esta invalido"}),201

@app.route("/fornecedor/<int:indice>", methods=["GET"])
def buscar_fornecedor():
    busca_fornecedor = request.get_json()
    ret = validar_fornecedor(busca_fornecedor)
    if ret == True:
        return({"valido":True, "mensagem":"O produto foi encontrado com sucesso!"})
    return({"valido":False, "mensagem":"O produto não foi encontrado"}),201

@app.route("/fornecedor/<int:indice>", methods=["PUT"])
def atualizar_fornecedor():
    atualiza_fornecedor = request.get_json()
    ret = validar_fornecedor(atualiza_fornecedor)
    if ret == True:
        return({"valido":True, "mensagem":"O estoque foi atualizado com sucesso!"})
    return({"valido":False, "mensagem":"O estoque não foi atualizado"}),201


@app.route("/fornecedor/<int:indice>", methods=["DELETE"])
def deletar_fornecedor():
    deleta_fornecedor = request.get_json()
    ret = validar_fornecedor(deleta_fornecedor)
    if ret == True:
        return({"valido":True, "mensagem":"O estoque foi deletado com sucesso!"})
    return({"valido":False, "mensagem":"O estoque não foi deletado!"})

pedido_entrada = []

@app.route("/pedido_entrada", methods=["GET"])
def listar_pedido_entrada():
    return jsonify(pedido_entrada)

@app.route("/pedido_entrada", methods=["POST"])
def adicionar_pedido_entrada():
    novo_pedido_entrada = request.get_json()
    ret = validar_pedido_entrada(novo_pedido_entrada)
    if ret == True:
        return({"valido":True, "mensagem":"O pedido_entrada esta validado com sucesso!"})
    return({"valido":False, "mensagem":"O pedido_entrada esta invalido"}),201

@app.route("/pedido_entrada/<int:indice>", methods=["GET"])
def buscar_pedido_entrada():
    busca_pedido_entrada = request.get_json()
    ret = validar_pedido_entrada(busca_pedido_entrada)
    if ret == True:
        return({"valido":True, "mensagem":"O pedido_entrada foi encontrado com sucesso!"})
    return({"valido":False, "mensagem":"O pedido_entrada não foi encontrado"}),201

@app.route("/pedido_entrada/<int:indice>", methods=["PUT"])
def atualizar_pedido_entrada():
    atualiza_pedido_entrada = request.get_json()
    ret = validar_pedido_entrada(atualiza_pedido_entrada)
    if ret == True:
        return({"valido":True, "mensagem":"O pedido_entrada foi atualizado com sucesso!"})
    return({"valido":False, "mensagem":"O pedido_entrada não foi atualizado"}),201


@app.route("/pedido_entrada/<int:indice>", methods=["DELETE"])
def deletar_pedido_entrada():
    deleta_pedido_entrada = request.get_json()
    ret = validar_pedido_entrada(deleta_pedido_entrada)
    if ret == True:
        return({"valido":True, "mensagem":"O pedido_entrada foi deletado com sucesso!"})
    return({"valido":False, "mensagem":"O pedido_entrada não foi deletado!"})


localizacoes = []

@app.route("/localizacoes", methods=["GET"])
def listar_localizacoes():
    return jsonify(localizacoes)

@app.route("/localizacoes", methods=["POST"])
def adicionar_localizacao():
    nova_localizacao = request.get_json()
    ret = validar_localizacao(nova_localizacao)
    if ret == True:
        return({"valido":True, "mensagem":"O login esta validado com sucesso!"})
    return({"valido":False, "mensagem":"O login esta invalido"}),201


@app.route("/localizacoes/<int:indice>", methods=["GET"])
def buscar_localizacao():
    localizacao_estoque = request.get_json()
    ret = validar_localizacao(localizacao_estoque)
    if ret == True:
        return({"valido":True, "mensagem":"O produto foi encontrado com sucesso!"})
    return({"valido":False, "mensagem":"O produto não foi encontrado"}),201

@app.route("/localizacoes/<int:indice>", methods=["PUT"])
def atualizar_localizacao():
    atualiza_localizacao = request.get_json()
    ret = validar_localizacao(atualiza_localizacao)
    if ret == True:
        return({"valido":True, "mensagem":"A localização foi atualizada com sucesso!"})
    return({"valido":False, "mensagem":" não foi atualizada"}),201

@app.route("/localizacoes/<int:indice>", methods=["DELETE"])
def deletar_localizacao():
    deleta_localizacao= request.get_json()
    ret = validar_localizacao(deleta_localizacao)
    if ret == True:
        return({"valido":True, "mensagem":"A localização foi deletada com sucesso!"})
    return({"valido":False, "mensagem":"A localização não foi deletada"}),201 

estoque=[]

@app.route("/estoque",methods = ["POST"])
def adicionar_estoque():
    novo_estoque = request.get_json()
    ret = validar_estoque(novo_estoque)
    if ret == True:
        return({"valido":True, "mensagem":"O login esta validado com sucesso!"})
    return({"valido":False, "mensagem":"O login esta invalido"}),201

@app.route("/estoque", methods=["GET"])
def buscar_estoque():
    busca_estoque = request.get_json()
    ret = validar_estoque(busca_estoque)
    if ret == True:
        return({"valido":True, "mensagem":"O produto foi encontrado com sucesso!"})
    return({"valido":False, "mensagem":"O produto não foi encontrado"}),201

@app.route("/estoque", methods=["PUT"])
def atualizar_estoque():
    atualizar_estoque = request.get_json()
    ret = validar_estoque(atualizar_estoque)
    if ret == True:
        return({"valido":True, "mensagem":"O estoque foi atualizado com sucesso!"})
    return({"valido":False, "mensagem":"O estoque não foi atualizado"}),201

@app.route("/Produtos", methods=["DELETE"])
def deletar_estoque():
    deletar_estoque = request.get_json()
    ret = validar_estoque(deletar_estoque)
    if ret == True:
        return({"valido":True, "mensagem":"O estoque foi deletado com sucesso!"})
    return({"valido":False, "mensagem":"O estoque não foi deletado"}),201
    
produtos = []

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/estoque",methods = ["POST"])
def adicionar_produtos():
    novo_produto = request.get_json()
    ret = validar_produto(novo_produto)
    if ret == True:
        return({"valido":True, "mensagem":"O produto foi validado com sucesso!"})
    return({"valido":False, "mensagem":"O produto esta invalido"}),201

@app.route("/produtos", methods=["GET"])
def buscar_produtos():
    busca_produtos = request.get_json()
    ret = validar_produto(busca_produtos) 
    if ret == True:
        return ({"valido":True, "mensagem":"O produto foi encontrado"})
    return ({"erro": "Produto não encontrado"}), 404

@app.route("/produtos", methods=["PUT"])
def atualizar_produtos():
    atualizar_produto = request.get_json()
    ret = validar_produto(atualizar_produto)
    if ret == True:
        return ({"mensagem": "Produto atualizado com sucesso!"})
    return ({"erro": "Produto não atualizado"}), 404

@app.route("/produtos", methods=["DELETE"])
def deletar_produtos():
    deleta_produtos = request.get_json()
    ret = validar_produto(deleta_produtos)
    if ret == True:
        return ({"mensagem": "Produto removido com sucesso!"})
    return ({"erro": "Produto não removido"}), 404



itens_entrada = []

@app.route("/itens_entrada", methods=["GET"])
def listar_itens_entrada():
    return jsonify(itens_entrada)

@app.route("/itens_entrada", methods=["POST"])
def adicionar_itens_entrada():
    novo_item = request.get_json()
    ret = validar_itens_entrada(novo_item)
    if ret == True:
        return({"valido":True, "mensagem":"Os itens foram validados com sucesso!"})
    return({"valido":False, "mensagem":"Os itens estam invalidos"}),201

@app.route("/itens_entrada/<int:indice>", methods=["GET"])
def buscar_itens_entrada():
    busca_itens_entrada = request.get_json()
    ret = validar_itens_entrada(busca_itens_entrada) 
    if ret == True:
        return ({"valido":True, "mensagem":"Os itens foram encontrados"})
    return ({"erro": "Itens não encontrados"}), 404

@app.route("/itens_entrada/<int:indice>", methods=["PUT"])
def atualizar_itens_entrada():
    busca_itens = request.get_json()
    ret = validar_itens_entrada(busca_itens) 
    if ret == True:
        return ({"valido":True, "mensagem":"Os itens foram atualizados"})
    return ({"erro": "Itens não atualizados"}), 404

@app.route("/itens_entrada/<int:indice>", methods=["DELETE"])
def deletar_itens_entrada():
    deleta_itens = request.get_json()
    ret = validar_itens_entrada(deleta_itens)
    if ret == True:
        return ({ "valido":True,"mensagem":"Item removido com sucesso!"})
    return ({"erro": "Item não removido"}), 404

itens_saida=[]

@app.route("/itens_saida", methods=["POST"])
def adicionar_itens_saida():
    novo_itens_saida = request.get_json()
    ret = validar_itens_saida(novo_itens_saida)
    if ret == True:
        return ({"valido":True,"mensagem":"Item adicionado com sucesso!"})
    return({"mensagem": "itens saida não foi adicionado!"}), 201

@app.route("/itens_saida/<int:indice>", methods=["GET"])
def buscar_itens_saida():
    busca_itens_saida = request.get_json()
    ret = validar_itens_saida(busca_itens_saida)
    if ret == True:
        return ({"valido":True, "mensagem":"Item encontrado com sucesso!"})
    return({"mensagem": "itens saida não foi encontrado!"}), 201

@app.route("/itens_saida/<int:indece>", methods=["PUT"])
def atualizar_itens_saida():
    atualizar_iten_saida = request.get_json()
    ret = validar_itens_saida(atualizar_iten_saida)
    if ret == True:
        return({"valido":True, "mensagem":"O item de saida foi atualizado com sucesso!"})
    return({"valido":False, "mensagem":"O item de saida não foi atualizado"}),201


@app.route("/itens_saida/<int:indice>", methods=["DELETE"])
def deletar_itens_saida():
    deleta_iten_saida = request.get_json()
    ret = validar_itens_saida(deleta_iten_saida)
    if ret == True:
        return({"valido":True, "mensagem": "itens saida removido com sucesso!"})
    return({"valido":False, "erro": "itens saida nao removido"}), 404

Pedidos_saida = []

@app.route("/Pedidos_saida", methods=["POST"])
def adicionar_Pedidos_saida():
    novo_Pedidos_saida = request.get_json()
    ret = validar_pedido_saida(novo_Pedidos_saida)
    if ret == True:
        return({"valido":True, "mensagem":"O Pedidos_saida esta validado com sucesso!"})
    return({"valido":False, "mensagem":"O Pedidos_saida esta invalido"}),201



@app.route("/Pedidos_saida /<int:indice>", methods=["GET"])
def buscar_Pedidos_saida():
    busca_Pedidos_saida = request.get_json()
    ret = validar_pedido_saida(busca_Pedidos_saida)
    if ret == True:
        return({"valido":True, "mensagem":"O Pedidos_saida foi encontrado com sucesso!"})
    return({"valido":False, "mensagem":"O Pedidos_saida não foi encontrado"}),201


@app.route("/Pedidos_saida/<int:indice>", methods=["PUT"])
def atualizar_Pedidos_saida():
    atualizar_Pedidos_saida = request.get_json()
    ret = validar_pedido_saida(atualizar_Pedidos_saida)
    if ret == True:
        return({"valido":True, "mensagem":"O Pedidos_saida foi atualizado com sucesso!"})
    return({"valido":False, "mensagem":"O Pedidos_saida não foi atualizado"}),201


@app.route("/Pedidos_saida/<int:indice>", methods=["DELETE"])
def deletar_Pedidos_saida():
    deletar_Pedidos_saida = request.get_json()
    ret = validar_pedido_saida(deletar_Pedidos_saida)
    if ret == True:
        return({"valido":True, "mensagem":"O pedido_saida foi deletado com sucesso!"})
    return({"valido":False, "mensagem":"O pedido_saida não foi deletado"}),201


clientes=[]

@app.route("/cliente", methods=["POST"])
def adicinar_cliente():
    novo_clientes = request.get_json()
    ret = vailadar_cliente(novo_clientes)
    if ret == True:
        resposta = insert_cliente(novo_clientes)
        return jsonify(resposta), 200 if resposta.get("status") == "sucesso" else 400
    return({"valido":False, "mensagem":"O clientes esta invalido"}),201


@app.route("/cliente/<int:id>", methods=["GET"])
def buscar_cliente():
    busca_cliente = request.get_json()
    ret = vailadar_cliente(busca_cliente)
    if ret == True:
        resposta = read_cliente(busca_cliente)
        return jsonify(resposta), 200 if resposta.get("status") == "sucesso" else 400
    return({"valido":False, "mensagem":"O cliente não foi encontrado"}),201


@app.route("/cliente/<int:id>", methods=["PUT"])
def atualizar_cliente():
    atualizar_cliente = request.get_json()
    ret = vailadar_cliente(atualizar_cliente)
    if ret == True:
        resposta = update_cliente(atualizar_cliente)
        return jsonify(resposta), 200 if resposta.get("status") == "sucesso" else 400
    return({"valido":False, "mensagem":"O cliente não foi atualizado"}),201


@app.route("/cliente/<int:id>", methods=["DELETE"])
def deletar_cliente():
    deletar_cliente = request.get_json()
    ret = vailadar_cliente(deletar_cliente)
    if ret == True:
        resposta = delete_cliente(deletar_cliente)
        return jsonify(resposta), 200 if resposta.get("status") == "sucesso" else 400
    return({"valido":False, "mensagem":"O cliente não foi deletado"}),201



if __name__=="__main__":
    app.run(debug=True)


