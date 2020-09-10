import re

f-input-ts = open("file.ts", "r")

orig = f-input-ts.read()

f-input-translated = open("input-translated.txt", "r")

lista = re.findall(".+(?:$)", f-input-translated.read(), re.MULTILINE)

listaIter = iter(lista)

final = re.sub("(?<=name: ').+(?=')", lambda x: (next(listaIter)), orig)

f = open("output.ts", "w")
f.write(final)
