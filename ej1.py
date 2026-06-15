## Problema 1: Control de Velocidad en una Autopista (25 pts)
##
##**Enunciado:**
##Una autopista instaló sensores para registrar la velocidad de los vehículos y detectar infracciones. Debes crear un programa que analice los registros y emita alertas cuando corresponda.

##**Indicaciones paso a paso:**
##1. Solicita al usuario que ingrese 5 velocidades (en km/h).
##2. Guarda las velocidades en una lista.
##3. Calcula el promedio y la velocidad máxima registrada.
##4. Verifica si todas las velocidades están dentro del límite permitido (entre 60 y 120 km/h).
##5. Si alguna velocidad supera los 140 km/h o es menor a 20 km/h, muestra una advertencia de peligro.



velocidad=[]

print("Registro de velocidades")
for i in range(1,6):
    
        
    int(input(f"Ingresa cinco velocidades {i} : "))
            
            
print("Resultado")

dentro_de_limite=True

fuera_de_limite=False


if velocidad<60 or velocidad>120:
    fuera_de_limite=False
if velocidad<20 or velocidad>140:
    dentro_de_limite=True
























