#Logica E

verifica_email=True
verifica_senha=True

verifica_login=verifica_email and verifica_senha

print(verifica_login)

if verifica_login:
    print("Entrar no programa")


#Logica ou

logica_ou=False or False or True

print(logica_ou)

#Operador de negação

negacao=not False

print(negacao)

if not verifica_login:
    print("Loga certo ai..")