import pandas as pd
"""
pessoas = pd.Series(['Amélia', 'Bonnie', 'Vesna', 'José'])
print("Imprimindo pessoas....")
print(pessoas)

indexHabilidades = ['witch', 'witch', 'guardian', 'warlock']

pessoas.index = indexHabilidades
print("...suas habilidades...")
print(pessoas)

tiposHabilidades = ['moon','sun','portals','green']

pessoas.index = tiposHabilidades
print("... e tipos.")
print(tiposHabilidades)
print(pessoas)
"""
pessoas = pd.Series(['witch', 'witch', 'guardian', 'warlock'], index = ['Amélia', 'Bonnie', 'Vesna', 'José'])

print("\nImprimindo pessoas e suas habilidades:\n")
print(pessoas)