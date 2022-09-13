from typing import List
from fastapi import APIRouter
from ..schemas.users import User, UserCreate, UserUpdate


router = APIRouter(
  prefix='/users',
  tags=['users']
)

@router.get('/', response_model=List[User])
def list_users():
  """# Lista todos os usuários existentes.

  O parâmetro query é utilizado para fazer o filtro de usuários.
  """
  pass

@router.get('/{user_id}', response_model=User)
def get_user_by_id(user_id: int):
  """# Pega os dados de um usuário específico"""
  pass

@router.post('/', response_model=User)
def create_user(user: UserCreate):
  """# Cria uma usuário de acordo com os dados passados.
  
  O parâmetro user é um schema com base nos dados a serem recebidos.
  """
  pass

@router.put('/{user_id}', response_model=User)
def update_user(user_id: int, user: UserUpdate):
  """# Atualiza as informações do usuário de acordo com os dados passados.
  
  O parâmetro user é um schema com base nos dados a serem recebidos.
  """
  pass

@router.delete('/{user_id}', response_model=User)
def delete_user(user_id: int):
  """# Apaga um usuário específico e todos seus dados relacionados."""
  pass