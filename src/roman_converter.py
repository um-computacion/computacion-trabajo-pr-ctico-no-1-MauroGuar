# Función para convertir un decimal a romano
def decimal_to_roman(decimal: int) -> str:

    # Según la posición del número (10^n) siempre se usa
    # un "uno" y/o un "cinco"
    ONES = ("I", "X", "C", "M")
    FIVES = ("V", "L", "D")

    # Acumulador
    roman = ""

    # Se itera sobre cada dígito del decimal
    # para ir colocando los números romanos uno detrás del otro
    dec_str = str(decimal)
    decimal_len = len(dec_str)
    for i in range(decimal_len):
        digit = int(dec_str[i])

        # La posición del dígito con respecto a 10^n (cuantos "ceros" tiene detrás)
        digit_pos = decimal_len - 1 - i

        # Dígito si entre 1 y 3: el valor del dígito son cuantos unos hay que colocar
        if 1 <= digit <= 3:
            roman += ONES[digit_pos] * digit

        # Dígito si 4: es un uno seguido de un cinco
        elif digit == 4:
            roman += ONES[digit_pos] + FIVES[digit_pos]

        # Dígito si entre 5 y 8: es un cinco seguido del excedente del mismo como unos
        elif 5 <= digit <= 8:
            roman += FIVES[digit_pos] + ONES[digit_pos] * (digit - 5)

        # Dígito si 9: es un uno seguido por el uno siguiente
        elif digit == 9:
            roman += ONES[digit_pos] + ONES[digit_pos + 1]
    return roman
