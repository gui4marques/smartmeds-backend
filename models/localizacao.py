from datetime import datetime
from core.crud_base import CrudBase
from core.database import Database

class localizacao(CrudBase):
    table = "localizacao"
    fields = [
        "rua_id",
        "andar_id",
        "numero_id",
        ]

    def __init__(self, rua_id, andar_id, numero_id =None):
        self.rua_id = rua
        self.andar_id = andar
        self.numero_id = numero
        

    @classmethod
    def find_all_with_product(cls): 
        conexao = Database.connect()
        cursor = conexao.cursor(dictionary=True)
        
        try:
            sql = """
            SELECT m.id, p.nome AS produto, m.tipo_movimentacao, m.quantidade, m.data_movimentacao
            FROM localizacao m
            INNER JOIN produto p ON m.produto_id = p.id
            ORDER BY m.data_movimentacao DESC
            """
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()