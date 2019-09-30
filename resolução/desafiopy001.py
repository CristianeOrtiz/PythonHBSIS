print('='*60)

frase = input(' {0} Digite uma frase: '.format( ' '*5))
letra = input(' {0} Digite uma letra: '.format( ' '*5))

print('{0} A letra foi encontrada {1} vezes'.format( ' '*5, frase.count(letra ) ) )
print('{0} A letra foi encontrada pela primeira vez {1}'.format( ' '*5, frase.index(letra ) ) )
print('{0} A letra foi encontrada pela última vez {1}'.format(' '*5, frase.rindex(letra ) ) )

print('='*60)