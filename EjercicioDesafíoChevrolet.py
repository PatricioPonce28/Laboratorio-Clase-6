print ("Bienvenido a Automotores Chevrolet")
Talleres = 3
Fugas = 0

for taller in range(1, Talleres + 1):
    respuesta = input(f"¿Existe fuga de gas en el taller {taller}? (Si/No) ? ")
    if respuesta == "Si" :
        Fugas = Fugas + 1

if Fugas > 1:
    print("¡Alerta! Más de un taller tiene la alerta se enviará un informe al correo .")
else:
    print("No se detectaron suficientes fugas para enviar una alerta.")
