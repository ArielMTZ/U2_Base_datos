import math

def mostrar_historial(historial):
    if not historial:
        print("\nNo hay operaciones en el historial todavía.")
    else:
        print("\n--- Historial de Operaciones ---")
        for item in historial:
            print(f"• {item}")
        print("-------------------------------")

def calculadora():
    historial = []
    
    while True:
        print("\n=== CALCULADORA EN PYTHON ===")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Potencia (^)")
        print("6. Raíz cuadrada (sqrt)")
        print("7. Ver historial")
        print("8. Salir")
        
        opcion = input("\nElige una opción (1-8): ").strip()
        
        if opcion == '8':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
            
        if opcion == '7':
            mostrar_historial(historial)
            continue
            
        # Opciones que requieren dos números
        if opcion in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("❌ Error: Por favor, ingresa números válidos.")
                continue
                
            if opcion == '1':
                resultado = num1 + num2
                operacion = f"{num1} + {num2} = {resultado}"
            elif opcion == '2':
                resultado = num1 - num2
                operacion = f"{num1} - {num2} = {resultado}"
            elif opcion == '3':
                resultado = num1 * num2
                operacion = f"{num1} * {num2} = {resultado}"
            elif opcion == '4':
                if num2 == 0:
                    print("❌ Error: No se puede dividir entre cero.")
                    continue
                resultado = num1 / num2
                operacion = f"{num1} / {num2} = {resultado}"
            elif opcion == '5':
                resultado = num1 ** num2
                operacion = f"{num1} ^ {num2} = {resultado}"
                
            print(f"✅ Resultado: {resultado}")
            historial.append(operacion)
            
        # Opción de raíz cuadrada (requiere un solo número)
        elif opcion == '6':
            try:
                num = float(input("Ingresa el número: "))
                if num < 0:
                    print("❌ Error: No se puede calcular la raíz cuadrada de un número negativo.")
                    continue
                resultado = math.sqrt(num)
                operacion = f"sqrt({num}) = {resultado}"
                print(f"✅ Resultado: {resultado}")
                historial.append(operacion)
            except ValueError:
                print("❌ Error: Por favor, ingresa un número válido.")
                continue
        else:
            print("❌ Opción inválida. Por favor, elige un número del 1 al 8.")

if __name__ == "__main__":
    calculadora()
