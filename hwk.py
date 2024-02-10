info = {1 :{'name': 'Ivan',
         'age': 35,
         'lastname': 'Wolf'},
         2: {'name': 'Anna',
          'age': 27,
          'lastname': 'Fish'},
         3: {'name': 'Tom',
          'age': 45,
          'lastname': 'Cave'}
}

text = {'name': 'Ivan',}

result = ()

for key, i in info.items():
   for z, value in i.items():
      for x, words in text.items():
         if words == value:
            if info[key] not in result:
               result += (info[key],)
print(result)