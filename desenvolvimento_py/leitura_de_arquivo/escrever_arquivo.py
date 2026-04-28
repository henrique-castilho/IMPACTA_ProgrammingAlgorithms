arquivo = open('novo_poema.txt', 'w', encoding='utf-8')

arquivo.write('Rosas são vermelhas,\n')
arquivo.write('Violetas são azuis,\n')
arquivo.write('A escrita é poderosa,\n')
arquivo.write('E a poesia é luz.\n')

arquivo.close()

print('Arquivo "novo_poema.txt" criado e escrito com sucesso!')

arquivo = open('novo_poema.txt', 'r', encoding='utf-8')

print(arquivo.read())

arquivo.close()