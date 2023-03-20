#ACTUALIZAR VALORES
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'primer_nombre':  'Michael', 'apellido' : 'Jordan'},
     {'primer_nombre' : 'John', 'apellido' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#Cambiar 10 a 15
x[1][0] = 15
print(x)

#Cambiar Nombre: Jordan a Bryant
estudiantes[0]['primer_nombre'] = 'Bryant'
print(estudiantes)

#Cambiar Messi por Andres
directorio_deportes['futbol'][0] = 'Andres'
print(directorio_deportes['futbol'])

#Cambiar vbalor de 20 a 30
z[0]['y'] = 30
print(z)

#ITERAR

estudiantes= [
         {'primer_nombre':  'Michael', 'last_name' : 'Jordan'},
         {'primer_nombre' : 'John', 'last_name' : 'Rosales'},
         {'primer_nombre' : 'Mark', 'last_name' : 'Guillen'},
         {'primer_nombre' : 'KB', 'last_name' : 'Tonel'}
    ]

def interateDictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            
