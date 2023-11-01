# Expreción de generador

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list]
my_second_list_gen = (x*2 for x in my_list)

print("lista original", my_list)
print("segunda lista con list comprehasion", my_second_list)
print("tercer lista con generator expression", my_second_list_gen)
