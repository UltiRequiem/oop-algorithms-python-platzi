def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	print(funcion_entrante("David"))

consume_funciones(presentarse)
consume_funciones(estudiemos_juntos)
