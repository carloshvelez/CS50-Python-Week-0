def main():
    pesos = pesos_a_float(input("¿Cuánto costó la comida? "))
    porcentaje = porcentaje_a_float(input("¿Qué porcentaje le gustaría dejar de propina? "))
    propina = pesos * porcentaje
    print(f"Leave ${propina: .2f}")

def pesos_a_float(valor):
    pesos = float(valor.replace("$", ""))
    return pesos

def porcentaje_a_float(valor):
    porcentaje = float(valor.replace("%", ""))/100
    return porcentaje

main()