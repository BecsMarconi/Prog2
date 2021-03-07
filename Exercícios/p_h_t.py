import pandas as pd

dic = {'pessoas': pd.Series(['Amélia', 'Bonnie', 'Vesna', 'José'], index=[1, 2, 3, 4]),
     'tipo': pd.Series(['witch','witch','guardian','warlock'], index=[1, 2, 3, 4]),
     'vital': pd.Series(['moon','sun','portals','elemental'], index=[1, 2, 3, 4]),
     'cidade': pd.Series(['Tealxa', 'Ghutaã', 'Aruh', 'Ospel'], index=[1, 3, 2, 4])}

df = pd.DataFrame(dic)
print(df)

"""
'''''' PRINT '''''
  pessoas      tipo      vital  cidade
1  Amélia     witch       moon  Tealxa
2  Bonnie     witch        sun    Aruh
3   Vesna  guardian    portals   Ghutaã
4    José   warlock  elemental   Ospel
"""