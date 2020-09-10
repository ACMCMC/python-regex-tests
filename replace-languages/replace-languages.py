import re

def sigIter(iter, x):
  returnVal = next(iter)
  print("Returned: " + returnVal + ", Got: " + x.group(0))
  return(returnVal)

f_input_ts = open("file.ts", "r")

orig = f_input_ts.read()

f_input_translated = open("input_translated.txt", "r")

lista = re.findall(".+(?:$)", f_input_translated.read(), re.MULTILINE)

listaIter = iter(lista)

final = re.sub("(?<=name: ').+(?=')", lambda x: sigIter(listaIter, x), orig)

f = open("output.ts", "w")
f.write(final)
