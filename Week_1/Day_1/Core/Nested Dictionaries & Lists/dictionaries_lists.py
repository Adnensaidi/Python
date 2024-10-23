# 1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x [1][0] = 15

# 1.1 Change the last_name of the first student from 'Jordan' to 'Bryant'

students [0]{'last_name'} = Bryan 

# 1.2 In the sports_directory, change 'Messi' to 'Andres'

sports_directory {'soccer'} [0] = Andres 

# 1.3 Change the value 20 in z to 30

z [0] {'y'} = 30 

# 2 Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops
# through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary (some_list) :
    
    for i in range (len(some_list)):
        print(some_list[i]["first_name"]+'-'+["last_name"])

# 3 Get Values From a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iteratedDictionary2(key_name, some_list) :

    for i in range (some_list([i])) :
        print(some_list[i]["first_name"])
        print(some_list[i]["last_name"])

# 4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(some_dict) : 
    def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)

printInfo(dojo)




