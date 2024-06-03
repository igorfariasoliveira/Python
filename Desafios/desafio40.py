n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))
media = (n1+n2)/2
if media < 5:
  print('Sua média foi {:.1f}. Você está reprovado!'.format(media))
elif media >= 5 and media < 7:
  print('Sua média foi {:.1f}. Você irá fazer a recuperação!'.format(media))
else:
  print('Sua média foi {:.1f}. Parabéns, você foi aprovado!'.format(media))