def calculate_annuity_payment(P, annual_rate, n):
    # Преобразуем годовую процентную ставку в месячную
    r = annual_rate / 100 / 12
    # Рассчитываем ежемесячный платеж
    M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return M

print(calculate_annuity_payment(1000000, 12, 48))
