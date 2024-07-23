ano = int(input('Entre com o ano: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
        print('O ano {} é Bissexto'.format(ano))
else:
      print('O ano {} Não é bissexto'.format(ano))