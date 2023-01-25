# print('permanent_period: ', permanence_period)
# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), ...]

# print('target_time: ', target_time)
# target_time = 5, expected = 3


def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""

    if type(target_time) != int:
        return None
    contador = 0
    for a, b in permanence_period:
        try:
            if a <= target_time <= b:
                contador += 1
        except TypeError:
            return None
    return contador
