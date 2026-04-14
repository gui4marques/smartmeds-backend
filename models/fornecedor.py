from core.crud_base import CrudBase
from core.database import Database
from core.validator import Validator

class Produto(CrudBase):
    table = "fornecedor"
    fields = [
        "nome",
        "endereço",
        "produto",
        "cnpj",
        "telefone",
        "email",
    ]

    def __init__(self, nome, endereço, produto, cnpj, telefone, email):
        self.nome = nome
        self.endereço = endereço
        self.produto = produto
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
  

def validate(self):
    erros = [
        Validator.required(self.nome, "nome"),
        Validator.cracteres_minimos(self.carac_min, "nome"),   
        Validator.caracteres_maximos(self.carac_max, "nome"), 

        Validator.required(self.endereço, "endereço"),
        Validator.cracteres_minimos(self.carac_min, "endereço"),  

        Validator.required(self.produto, "produto"),
        Validator.cracteres_minimos(self.carac_min, "min"),  

        Validator.required(self.email, "email"),
        Validator.cracteres_minimos(self.carac_min, "email"),  

        Validator.required(self.cnpj, "cnpj"),
         Validator.cracteres_minimos(self.carac_min, "cnpj"),   
         
        Validator.required(self.telefone, "telefone"),
        Validator.cracteres_minimos(self.carac_min, "telefone"),  
]
return [erro for erro in erros if erro]

      
      
      
@classmethod
def safe_delete(cls, id):
    produto = cls.find_by_id(id)
    if not produto:
        raise ValueError("Fornecedor não encontrado.")
    if cls.has_related_records(id):
        raise ValueError("Não é possível excluir o fornecedor porque ele possui informações ou movimentações vinculadas.")
    cls.delete(id)
