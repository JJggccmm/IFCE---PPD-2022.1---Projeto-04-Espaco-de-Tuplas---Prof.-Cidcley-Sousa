# teste

# https://algoritmosempython.com.br/cursos/programacao-python/tuplas/ <---- Ajudou na manipulação de tuplas
import linsimpy # https://github.com/robwalton/linsimpy <---- GRAÇAS A DEUSSSS ISSO FUNCIONAAAAA!!!!
import time

tse = linsimpy.TupleSpaceEnvironment()
print()

tupla_teste = (2,3)

tse.out(('three', 4)) #<---- Isso cria e põe uma tupla no espaço
tse.out(('three', 3)) 
tse.out(('three', 11))
tse.out(('three', 2))
tse.out(('tupla_teste', tupla_teste))
tse.out(('tupla_teste', 22))

#tse.run()

val = tse.items[1]
#assert tse.now == 2
print(tse.items)

time.sleep(2)

val = tse.inp(('tupla_teste', object)) # <--- Aqui, Object pode ser "tuple" tmb que dá no msm!
#tse.inp(('tupla_teste', object))

print(str(val)+" foi removido")

print(tse.items)

