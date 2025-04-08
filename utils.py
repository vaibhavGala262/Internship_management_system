from passlib.context import CryptContext
pwd_context= CryptContext(schemes=["bcrypt"],deprecated = "auto")


def hash(password:str):
    return pwd_context.hash(password)

def compare(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def to_dict_list(results):
    return [dict(row._mapping) for row in results]