from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users
from .config.database import engine
from .config.database import Base


api_description = """
Essa API é um Boilerplate utilizando como exemplo rotas de usuários com autenticação OAuth2 e JWT.
"""

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
# ]

Base.metadata.create_all(bind=engine)

app = FastAPI(
  title='FastAPI Boilerplate',
  description=api_description,
  version='0.0.1'
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(users.router)