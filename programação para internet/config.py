import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345@localhost:3306/nome_banco'