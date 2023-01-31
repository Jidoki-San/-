# Permitir que usuários existentes possam fazer o login
resposta = input('[1] - Cadaastrar novo usuário [2] - Fazer login: ')
# armazenando os usuários existentes
usuarios = ['carol', 'amanda','jeff']  
senhas = ['123456', 'abcdef', '123abcd']

if resposta == '1':
    # recebendo um usuário
    usuario_digitado = input('digite seu usuário: ')
    if usuario_digitado in usuarios:
        print('Usuário existente')
    else:
        # recebendo uma senha
        senha_digitado = input('Digite sua senha: ')
        # caso não existe, cadastrar aquele usuário	e senha
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitado)   
elif resposta == '2':
    # Permitir que usuários existentes possam fazer o login
    # pedir usuário
    usuario_digitado = input('Digite seu usuário: ')
    # pedir senha
    senha_digitado = input('Digite sua senha: ')
    encontrado = False
    # preiciso verificar se usuário e a senha providênciada para aquele usuario
    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitado == senhas[indice]:
            print('Login efetuado com sucesso!') 
            encontrado = True 
        elif encontrado == False:
            print('Usuário ou senha incorreto!') 
else:
    print('digite apenas 1 ou 2')