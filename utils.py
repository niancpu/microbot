from dotenv import dotenv_values
from pydantic import SecretStr

def get_env(*args)->list:
    args=[dotenv_values()[x] for x in dotenv_values().keys()]
    return args

def get_key(LLM_API:str)->SecretStr|None:
    key=dotenv_values()[LLM_API]
    if key is None:
        return None
    return SecretStr(key)