def calculate_annuity_payment(P, annual_rate, n):
    # Преобразуем годовую процентную ставку в месячную
    r = annual_rate / 100 / 12
    # Рассчитываем ежемесячный платеж
    M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return M

if __name__ == "__main__":
    try:
        principal = float(input("Введите сумму кредита: "))
        annual_interest_rate = float(input("Введите годовую процентную ставку (в %): "))
        months = int(input("Введите количество месяцев: "))

        monthly_payment = calculate_annuity_payment(principal, annual_interest_rate, months)
        print(f"Ежемесячный платеж составит: {monthly_payment:.2f} руб.")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")
