print('Bem vindo ao curso de python!')
idadeUsuario = input('Insira sua idade:', 0)

if idadeUsuario > 10:
    print('Sua idade permite se inscrever no curso')
elif idadeUsuario < 10:
    print('Sua idade não permite se inscrever no curso')
else:
    print('Sua idade é a minima para se inscrever no curso')