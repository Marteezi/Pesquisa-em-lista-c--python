store = ['Mobile', 'Ps4', 'Gabinete']
valor = ['3400', '5000', '378']

seach = input("Qual produto você está procurando: ")
if seach in store:
    pesquisar = store.index(seach)
    print("A valor do produto {} e de {}".format(store[pesquisar], valor[pesquisar]))
else:
    print("O produto {} não existe.".format(seach))
