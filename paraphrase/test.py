from PyDictionary import PyDictionary 
words = ['seid', 'hello', 'peace']

dictionary = PyDictionary(words)

print(dictionary.meaning('indentation'))
print(dictionary.synonym("life"))
print(dictionary.getMeanings()) 
print (dictionary.getSynonyms())