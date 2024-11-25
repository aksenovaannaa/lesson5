immutable_var=5,10,'cat',10.5
print('Immutable var: ',immutable_var)
#immutable_var[2]='dog'
#print(immutable_var) #кортеж не поддерживает обращение по элементам
mutable_list=[5,10,'cat',10.5]
mutable_list[1]=11
mutable_list[2]='dog'
print('Mutable list: ',mutable_list)