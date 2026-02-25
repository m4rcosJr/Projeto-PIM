import json
import hashlib
import os


ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def cadastrar_usuario(nome, usuario, senha):
    usuarios = carregar_usuarios()
    # Verifica se já existe o usuário
    if any(u["usuario"] == usuario for u in usuarios):
        return False
    # Criptografa a senha usando SHA-1
    senha_hash = hashlib.sha1(senha.encode("utf-8")).hexdigest()
    usuarios.append({
        "nome": nome,
        "usuario": usuario,
        "senha": senha_hash
    })
    salvar_usuarios(usuarios)
    return True

def validar_login(usuario, senha):
    usuarios = carregar_usuarios()
    senha_hash = hashlib.sha1(senha.encode("utf-8")).hexdigest()
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha_hash:
            return True
    return False
