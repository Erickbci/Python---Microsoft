print('Bem vindo ao curso de python!')
idadeUsuario = int(input('Insira sua idade:'))
descontoUsuario = input('Voce possui a cupom para entrar no curso?')
permissaoPai = input('Seu pai deixou voce fazer esse curso?')
stack = input('Stack')

if idadeUsuario > 10 and descontoUsuario == 'cupom':
    print('Sua idade permite se inscrever no curso e tera R$100 de desconto')
elif idadeUsuario > 10 and descontoUsuario == '':
    print('Sua idade permite se inscrever no curso e nao tera desconto')
elif idadeUsuario < 10:
    print('Sua idade não permite se inscrever no curso')
elif stack == 'dev' or permissaoPai == 'sim':
    print('Vc pode fazer o curso')
else: 
    print('Sua idade é a minima para se inscrever no curso')