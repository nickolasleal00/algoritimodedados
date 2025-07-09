def Embaralhar(s):
 return sorted(s)


carro = map(Embaralhar, ('Civic','Corolla','Toro'))

print(carro)
print('---------------')
print(list(carro))