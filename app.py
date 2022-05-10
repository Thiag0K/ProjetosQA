

from unittest import result


def welcome(name):
    return "Olá " + name + ", bem vindo ao Curso básico de Robot Framework!"

result = welcome ("Thiago")
print(result)
