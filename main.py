def procesar_modalidad(tipo_modalidad):
    if tipo_modalidad == 'R' or tipo_modalidad == 'r':
        print("No requiere registrar horas")
    elif tipo_modalidad == 'P' or tipo_modalidad == 'p':
        registrar_horas_trabajadas()
    else:
        print("El dato ingresado no es válido")

def registrar_horas_trabajadas():
    hora_minima = 9
    hora_maxima = 18

    hora_inicio = int(input("Ingrese su hora de ingreso (Ej: 9, 10, etc): "))
    if hora_inicio >= hora_minima:
        hora_almuerzo_inicio = int(input("¿A qué hora almorzó? (Ej: 12, 13, etc): "))
        hora_almuerzo_fin = int(input("¿A qué hora retomó su trabajo? (Ej: 13, 14, etc): "))
        duracion_almuerzo = hora_almuerzo_fin - hora_almuerzo_inicio

        if duracion_almuerzo > 1:
            print("⚠️ Advertencia: Se ha excedido el tiempo de almuerzo permitido (1 hora).")

        hora_final = int(input("Ingrese su hora de salida (Ej: 10, 16, etc): "))
        if hora_final <= hora_maxima:
            if hora_final > hora_inicio:
                horas_totales = (hora_final - hora_inicio) - duracion_almuerzo
                print("🕒 La cantidad de horas registradas es:", horas_totales)
                verificar_minimo_horas(horas_totales)

                tarea1 = input("Ingrese una tarea realizada: ")
                continuar = input("¿Desea agregar otra tarea? (S/N): ")
                if continuar.lower() == 's':
                    tarea2 = input("Ingrese otra tarea realizada: ")
                    continuar2 = input("¿Desea agregar otra tarea más? (S/N): ")
                    if continuar2.lower() == 's':
                        tarea3 = input("Ingrese otra tarea más: ")
                        mostrar_resumen(horas_totales, tarea1, tarea2, tarea3)
                    else:
                        mostrar_resumen(horas_totales, tarea1, tarea2)
                else:
                    mostrar_resumen(horas_totales, tarea1)

            else:
                print("❌ La hora de salida debe ser mayor que la de ingreso")
        else:
            print("❌ La hora de salida no puede ser mayor a las 18:00")
    else:
        print("❌ La hora de ingreso no puede ser menor a las 9:00")

def verificar_minimo_horas(horas_trabajadas):
    minimo_horas = 6
    if horas_trabajadas < minimo_horas:
        print(f"⚠️ Advertencia: Las horas trabajadas ({horas_trabajadas}) son menores al mínimo requerido de {minimo_horas} horas.")
    else:
        print("✅ Jornada laboral registrada correctamente.")

def mostrar_resumen(horas_totales, tarea1, tarea2=None, tarea3=None):
    print("\n📝 RESUMEN DE LA JORNADA")
    print(f"Total de horas trabajadas (sin contar almuerzo): {horas_totales}")
    print("Tareas realizadas:")
    print(f"1. {tarea1}")
    if tarea2 is not None:
        print(f"2. {tarea2}")
    if tarea3 is not None:
        print(f"3. {tarea3}")
    print("✅ Gracias por registrar su jornada.")

def iniciar_programa():
    tipo_modalidad = input("Ingrese la modalidad de su puesto Remoto(R), Presencial(P): ")
    procesar_modalidad(tipo_modalidad)

iniciar_programa()


