from fractions import Fraction


# La imagen usa 0.667 para P(+m | +g), pero los valores dados en la tabla
# corresponden a la fraccion exacta 2/3.
P_G = {
    "+": Fraction(1, 10),
    "-": Fraction(9, 10),
}

P_M_G = {
    ("+", "+"): Fraction(2, 3),
    ("-", "+"): Fraction(1, 3),
    ("+", "-"): Fraction(1, 4),
    ("-", "-"): Fraction(3, 4),
}

P_B_M = {
    ("+", "+"): Fraction(2, 5),
    ("-", "+"): Fraction(3, 5),
    ("+", "-"): Fraction(1, 5),
    ("-", "-"): Fraction(4, 5),
}

P_C_M = {
    ("+", "+"): Fraction(1, 4),
    ("-", "+"): Fraction(3, 4),
    ("+", "-"): Fraction(1, 2),
    ("-", "-"): Fraction(1, 2),
}

ROWS = [
    ("+", "+", "+", "+"),
    ("+", "+", "+", "-"),
    ("+", "+", "-", "+"),
    ("+", "+", "-", "-"),
    ("+", "-", "+", "+"),
    ("+", "-", "+", "-"),
    ("+", "-", "-", "+"),
    ("+", "-", "-", "-"),
    ("-", "+", "+", "+"),
    ("-", "+", "+", "-"),
    ("-", "+", "-", "+"),
    ("-", "+", "-", "-"),
    ("-", "-", "+", "+"),
    ("-", "-", "+", "-"),
    ("-", "-", "-", "+"),
    ("-", "-", "-", "-"),
]

MISSING_ROWS = {
    ("+", "+", "+", "-"),
    ("+", "+", "-", "-"),
    ("+", "-", "-", "+"),
    ("-", "+", "+", "+"),
    ("-", "+", "-", "+"),
    ("-", "-", "-", "+"),
}


def joint_probability(g, m, b, c):
    return P_G[g] * P_M_G[(m, g)] * P_B_M[(b, m)] * P_C_M[(c, m)]


def format_fraction(value):
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def print_table(rows):
    print("G M B C  P(G,M,B,C)")
    print("---------------------")

    for row in rows:
        probability = format_fraction(joint_probability(*row))
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}  {probability}")


def main():
    print("Tabla conjunta completa:")
    print_table(ROWS)

    print("\nValores faltantes:")
    print_table([row for row in ROWS if row in MISSING_ROWS])

    total = sum(joint_probability(*row) for row in ROWS)
    print(f"\nSuma de probabilidades: {format_fraction(total)}")


if __name__ == "__main__":
    main()
