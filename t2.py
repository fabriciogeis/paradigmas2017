#Defina uma função addSuffix(suf,nomes) que retorne a lista de nomes
#com o sufixo suf adicionado. Exemplos:
#>>> addSuffix('@inf.ufsm.br',['fulano','beltrano'])
#  ['fulano@inf.ufsm.br', 'beltrano@inf.ufsm.
def addSuffix(suf,nomes):
    lista = [nome + suf for nome in nomes]
    return lista

#Escreva uma função countShorts(words), que receba uma lista
#de palavras e retorne a quantidade de palavras dessa lista
#que possuem menos de 5 caracteres.
#>>> t2.countShorts(['lazy','dog','brown','fox'])
#3
def countShorts(words):
    lista = [len(x)< 5 for x in words]
    return  lista#filter(lambda x : x < 5,[words])
    #return  lista

#Defina uma função stripVowels(s) que receba uma string e retire suas vogais,
#conforme os exemplos abaixo:
#>>> stripVowels('Andrea')
#'ndr'
#>>> stripVowels('xyz')
#'xyz'
#>>> stripVowels('')
#''
def stripVowels(s):
    lista = [ x for x in s]
    listanova = str.strip(['a','e','i','o','u'])
    return lista,listanova
