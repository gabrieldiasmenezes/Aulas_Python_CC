escolha_usuario=1

#0-sair do programa
#1-entrar no programa
#>>>> erro

match escolha_usuario:
    case 0:
        print('Saindo do programa')
    case 1:
        print('Entrando no programa')
    case _:
        print("Erro")