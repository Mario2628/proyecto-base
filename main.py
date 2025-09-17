from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()
    
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo (resto)")
        print("6. Cambiar números")
        print("0. Salir")
        
        try:
            opcion = int(input("Elige una opción (0-6): "))
            if opcion == 1:
                op.sumar()
            elif opcion == 2:
                op.restar()
            elif opcion == 3:
                op.multiplicar()
            elif opcion == 4:
                op.dividir()
            elif opcion == 5:
                op.modulo()
            elif opcion == 6:
                op.leerNumeros()
                continue  
            elif opcion == 0:
                print("¡Gracias por usar la calculadora!")
                break
            else:
                print("Opción inválida, intenta de nuevo.")
                continue
            
            op.mostrarResultado()
        
        except Exception:
            print("Entrada inválida, intenta de nuevo.")
            continue

if __name__ == "__main__":
    main()
