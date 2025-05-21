def registro_horas():
    print("INICIO DEL SISTEMA DE REGISTRO DE HORAS")
    
    # Solicitar tipo de modalidad
    tipo_modalidad = input("¿Tipo de modalidad? (P para Presencial, R para Remoto): ").upper()
    
    # Verificar si es necesario registrar horas
    if tipo_modalidad == "R":
        print("No requiere registrar horas")
        return
    elif tipo_modalidad == "P":
        print("Inicia registro de horas")
    else:
        print("Error: Modalidad inválida. Debe ser P o R.")
        return
    
    # Solicitar hora de ingreso
    hora_ingreso = float(input("Ingrese la hora de entrada (formato 24 horas, ej: 8.30): "))
    
    # Verificar si la hora de ingreso es válida
    if hora_ingreso > 9.00:
        print("Error: Hora de ingreso inválido. Debe ser antes de las 9:00.")
        return
    
    # Solicitar hora de salida
    hora_salida = float(input("Ingrese la hora de salida (formato 24 horas, ej: 17.30): "))
    
    # Verificar si la hora de salida es mayor que la hora de entrada
    if not (hora_salida > hora_ingreso):
        print("Error: Horario inválido. La hora de salida debe ser posterior a la hora de entrada.")
        return
    
    # Verificar si la hora de salida es adecuada
    if hora_salida <= 18.00:
        print("Jornada correcta")
    else:
        print("Error: Hora de salida inválido. Debe ser antes de las 18:00.")
        return
    
    # Calcular horas trabajadas antes de considerar el almuerzo
    horas_totales = hora_salida - hora_ingreso
    
    # Solicitar tiempo de almuerzo
    tiempo_almuerzo = float(input("Ingrese el tiempo de almuerzo en horas (ej: 1.0): "))
    
    # Verificar si el tiempo de almuerzo es adecuado
    if tiempo_almuerzo < 1.0:
        print("Mostrar advertencia: El tiempo de almuerzo es menor a una hora.")
    
    # Restar el tiempo de almuerzo a las horas totales
    horas_efectivas = horas_totales - tiempo_almuerzo
    
    # Verificar si se cumplieron las horas mínimas
    if horas_efectivas >= 6:
        print(f"Horas trabajadas: {horas_efectivas}")
    else:
        print("Advertencia: Horas insuficientes. Debe trabajar al menos 6 horas efectivas.")
    
    # Registro de tareas
    primera_tarea = input("Ingrese la primera tarea realizada: ")
    
    # Preguntar si desea agregar otra tarea
    agregar_tarea = input("¿Desea agregar otra tarea? (S/N): ").upper()
    
    if agregar_tarea == "S":
        # Solicitar segunda tarea
        segunda_tarea = input("Ingrese la segunda tarea realizada: ")
        
        # Preguntar si desea agregar otra tarea más
        agregar_tarea = input("¿Desea agregar otra tarea? (S/N): ").upper()
        
        if agregar_tarea == "S":
            # Solicitar tercera tarea
            tercera_tarea = input("Ingrese la tercera tarea realizada: ")
            
            # Mostrar resumen con 3 tareas
            print("\nRESUMEN DE JORNADA:")
            print(f"Modalidad: Presencial")
            print(f"Hora de entrada: {hora_ingreso}")
            print(f"Hora de salida: {hora_salida}")
            print(f"Tiempo de almuerzo: {tiempo_almuerzo} horas")
            print(f"Horas efectivas trabajadas: {horas_efectivas}")
            print("Tareas realizadas:")
            print(f"  1. {primera_tarea}")
            print(f"  2. {segunda_tarea}")
            print(f"  3. {tercera_tarea}")
        else:
            
            print("\nRESUMEN DE JORNADA:")
            print(f"Modalidad: Presencial")
            print(f"Hora de entrada: {hora_ingreso}")
            print(f"Hora de salida: {hora_salida}")
            print(f"Tiempo de almuerzo: {tiempo_almuerzo} horas")
            print(f"Horas efectivas trabajadas: {horas_efectivas}")
            print("Tareas realizadas:")
            print(f"  1. {primera_tarea}")
            print(f"  2. {segunda_tarea}")
    else:
        # Mostrar resumen con 1 tarea
        print("\nRESUMEN DE JORNADA:")
        print(f"Modalidad: Presencial")
        print(f"Hora de entrada: {hora_ingreso}")
        print(f"Hora de salida: {hora_salida}")
        print(f"Tiempo de almuerzo: {tiempo_almuerzo} horas")
        print(f"Horas efectivas trabajadas: {horas_efectivas}")
        print("Tareas realizadas:")
        print(f"  1. {primera_tarea}")
    
    print("FIN DEL REGISTRO")

if __name__ == "__main__":
    registro_horas()

