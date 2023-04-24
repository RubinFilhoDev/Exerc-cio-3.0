import json

informacao_clientes = [
    {"id": "1", "nome": "João da Silva", "idade": 30, "sexo": "M", "cidade": "São Paulo"},
    {"id": "2", "nome": "Maria Oliveira", "idade": 25, "sexo": "F", "cidade": "Rio de Janeiro"},
    {"id": "3", "nome": "Pedro Alves", "idade": 40, "sexo": "M", "cidade": "Belo Horizonte"},
    {"id": "4", "nome": "Ana Souza", "idade": 28, "sexo": "F", "cidade": "Porto Alegre"},
    {"id": "5", "nome": "Lucas Santos", "idade": 35, "sexo": "M", "cidade": "Brasília"},
    {"id": "6", "nome": "Juliana Pereira", "idade": 27, "sexo": "F", "cidade": "Fortaleza"},
    {"id": "7", "nome": "Gustavo Lima", "idade": 32, "sexo": "M", "cidade": "Recife"},
    {"id": "8", "nome": "Carla Fernandes", "idade": 23, "sexo": "F", "cidade": "Salvador"}
]

informacao_compras = [
    {
        "id": "1",
        "id_cliente": "4",
        "data": "2022-08-25",
        "valor": 153.79,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "2",
        "id_cliente": "3",
        "data": "2022-01-27",
        "valor": 918.12,
        "descricao": "Compra de roupas"
    },
    {
        "id": "3",
        "id_cliente": "5",
        "data": "2022-10-22",
        "valor": 702.77,
        "descricao": "Compra de sapatos"
    },
    {
        "id": "4",
        "id_cliente": "4",
        "data": "2022-11-15",
        "valor": 59.38,
        "descricao": "Pagamento de conta"
    },
    {
        "id": "5",
        "id_cliente": "5",
        "data": "2022-08-06",
        "valor": 143.59,
        "descricao": "Compra de eletronicos"
    },
    {
        "id": "6",
        "id_cliente": "4",
        "data": "2022-06-27",
        "valor": 352.69,
        "descricao": "Compra de sapatos"
    },
    {
        "id": "7",
        "id_cliente": "4",
        "data": "2022-08-19",
        "valor": 151.53,
        "descricao": "Compra de roupas"
    },
    {
        "id": "8",
        "id_cliente": "6",
        "data": "2022-09-10",
        "valor": 829.97,
        "descricao": "Pagamento de conta"
    },
    {
        "id": "9",
        "id_cliente": "8",
        "data": "2022-09-14",
        "valor": 711.87,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "10",
        "id_cliente": "1",
        "data": "2022-11-18",
        "valor": 448.52,
        "descricao": "Compra de sapatos"
    },
    {
        "id": "11",
        "id_cliente": "1",
        "data": "2022-10-14",
        "valor": 39.27,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "12",
        "id_cliente": "7",
        "data": "2022-03-22",
        "valor": 404.95,
        "descricao": "Compra de eletronicos"
    },
    {
        "id": "13",
        "id_cliente": "8",
        "data": "2022-02-26",
        "valor": 760.94,
        "descricao": "Compra de roupas"
    },
    {
        "id": "14",
        "id_cliente": "1",
        "data": "2022-07-09",
        "valor": 535.58,
        "descricao": "Compra de roupas"
    },
    {
        "id": "15",
        "id_cliente": "1",
        "data": "2022-04-15",
        "valor": 989.57,
        "descricao": "Compra de eletronicos"
    },
    {
        "id": "16",
        "id_cliente": "6",
        "data": "2022-09-10",
        "valor": 48.8,
        "descricao": "Compra de eletronicos"
    },
    {
        "id": "17",
        "id_cliente": "8",
        "data": "2022-11-25",
        "valor": 667.54,
        "descricao": "Compra de roupas"
    },
    {
        "id": "18",
        "id_cliente": "8",
        "data": "2022-01-19",
        "valor": 133.27,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "19",
        "id_cliente": "5",
        "data": "2022-07-23",
        "valor": 721.39,
        "descricao": "Compra de roupas"
    },
    {
        "id": "20",
        "id_cliente": "3",
        "data": "2022-07-28",
        "valor": 414.54,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "21",
        "id_cliente": "6",
        "data": "2022-02-14",
        "valor": 56.83,
        "descricao": "Compra de roupas"
    },
    {
        "id": "22",
        "id_cliente": "4",
        "data": "2022-09-24",
        "valor": 981.49,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "23",
        "id_cliente": "7",
        "data": "2022-05-23",
        "valor": 892.48,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "24",
        "id_cliente": "3",
        "data": "2022-04-19",
        "valor": 439.11,
        "descricao": "Compra de sapatos"
    },
    {
        "id": "25",
        "id_cliente": "1",
        "data": "2022-05-14",
        "valor": 416.69,
        "descricao": "Compra de alimentos"
    },
    {
        "id": "26",
        "id_cliente": "5",
        "data": "2022-04-07",
        "valor": 955.16,
        "descricao": "Compra de sapatos"
    },
    {
        "id": "27",
        "id_cliente": "5",
        "data": "2022-02-21",
        "valor": 418.03,
        "descricao": "Compra de roupas"
    },
    {
        "id": "28",
        "id_cliente": "1",
        "data": "2022-08-15",
        "valor": 363.73,
        "descricao": "Compra de roupas"
    },
    {
        "id": "29",
        "id_cliente": "6",
        "data": "2022-05-20",
        "valor": 520.42,
        "descricao": "Pagamento de conta"
    },
    {
        "id": "30",
        "id_cliente": "3",
        "data": "2022-09-18",
        "valor": 224.99,
        "descricao": "Compra de sapatos"
    }
]

def get_compras_from_cliente(id):
    def recebe_cliente(id): 
        for cliente in informacao_clientes:
            if cliente["id"] == id:
                return cliente
            
    def recebe_compras(id_cliente):
        compras_encontradas = []
        for compra in informacao_compras:
            if compra["id_cliente"] == id_cliente:
                compras_encontradas.append(compra)
        return compras_encontradas


    cliente_encontradas = recebe_cliente(id)

    compras_encontradas = recebe_compras(id)

    total = sum(item["valor"] for item in compras_encontradas)

    compras = [{"data" : item["data"], "valor" : item["valor"]} for item in compras_encontradas]

    cliente_e_compras = {
        'id' : id,
        'nome': cliente_encontradas['nome'], 
        'compras': compras,
        'total' : total,
        'media_valor_gasto' : total/len(compras_encontradas),
    }

    return cliente_e_compras

with open("resultados.json", "w") as arquivo:     
    json.dump(get_compras_from_cliente("8"), arquivo, indent=4)


