def solicitar_modalidad():
    modalidad = input("¿Tipo de modalidad? (P para Presencial, R para Remoto): ").upper()
    if modalidad == "R":
        print("No requiere registrar horas")
        return None
    elif modalidad == "P":
        print("Inicia registro de horas")
        return modalidad
    else:
        print("Error: Modalidad inválida. Debe ser P o R.")
        return None

def solicitar_hora_ingreso():
    hora = float(input("Ingrese la hora de entrada (formato 24 horas, ej: 8.30): "))
    if hora > 9.00:
        print("Error: Hora de ingreso inválido. Debe ser antes de las 9:00.")
        return None
    return hora

def solicitar_hora_salida(hora_ingreso):
    hora = float(input("Ingrese la hora de salida (formato 24 horas, ej: 17.30): "))
    if hora <= hora_ingreso:
        print("Error: Horario inválido. La hora de salida debe ser posterior a la hora de entrada.")
        return None
    if hora > 18.00:
        print("Error: Hora de salida inválido. Debe ser antes de las 18:00.")
        return None
    print("Jornada correcta")
    return hora

def calcular_horas_efectivas(hora_ingreso, hora_salida):
    total = hora_salida - hora_ingreso
    almuerzo = float(input("Ingrese el tiempo de almuerzo en horas (ej: 1.0): "))
    if almuerzo < 1.0:
        print("Mostrar advertencia: El tiempo de almuerzo es menor a una hora.")
    efectivas = total - almuerzo
    if efectivas >= 6:
        print(f"Horas trabajadas: {efectivas}")
    else:
        print("Advertencia: Horas insuficientes. Debe trabajar al menos 6 horas efectivas.")
    return efectivas, almuerzo

def registrar_tareas():
    tareas = []
    while True:
        tarea = input("Ingrese una tarea realizada: ")
        tareas.append(tarea)
        continuar = input("¿Desea agregar otra tarea? (S/N): ").upper()
        if continuar != "S":
            break
    return tareas

def mostrar_resumen(hora_ingreso, hora_salida, tiempo_almuerzo, horas_efectivas, tareas):
    print("\nRESUMEN DE JORNADA:")
    print(f"Modalidad: Presencial")
    print(f"Hora de entrada: {hora_ingreso}")
    print(f"Hora de salida: {hora_salida}")
    print(f"Tiempo de almuerzo: {tiempo_almuerzo} horas")
    print(f"Horas efectivas trabajadas: {horas_efectivas}")
    print("Tareas realizadas:")
    for i in range(len(tareas)):
        print(f"  {i + 1}. {tareas[i]}")


def registro_horas():
    print("INICIO DEL SISTEMA DE REGISTRO DE HORAS")
    
    modalidad = solicitar_modalidad()
    if modalidad is None:
        return
    
    hora_ingreso = solicitar_hora_ingreso()
    if hora_ingreso is None:
        return

    hora_salida = solicitar_hora_salida(hora_ingreso)
    if hora_salida is None:
        return

    horas_efectivas, tiempo_almuerzo = calcular_horas_efectivas(hora_ingreso, hora_salida)

    tareas = registrar_tareas()
    mostrar_resumen(hora_ingreso, hora_salida, tiempo_almuerzo, horas_efectivas, tareas)

if __name__ == "__main__":
    registro_horas()
