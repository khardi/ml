"""


[title]: # (Задача о рекламе)


Задача о рекламе
----------------

Задача линейного программирования.

Дано:
    Радио реклама: $5 за минуту
    Теле реклама: $30 за минуту
    Компания использует Радио рекламу в 3 раза чаще чем Теле реламу
    1 минута Теле рекламы приносит продаж в 30 раз больше чем 1 минута Радио рекламы

Переменные:    
    x1 - количество запусков Теле Рекламы
    x2 - количество запусков Радио рекламы
    
Целевая функция: 
    $30 x1 + x2

Ограничение по буджету: 
    $90 x1 + $5 x2 <= $10000    

Соотношение времени показа:
    x2 = 3 x1
    
Найти значения переменных x1, x2, при которых целевая функция будет максимальна


    >>> import pulp
    
    >>> problem = pulp.LpProblem('Увеличние продаж', pulp.LpMaximize)
    
    >>> x1 = pulp.LpVariable('x1', 0)
    >>> x2 = pulp.LpVariable('x2', 0)
    
    >>> problem += 30 * x1 + x2, 'Целевая функция. Максимальное количество продаж'
    >>> problem += 90 * x1 + 5 * x2 <= 10000, 'Ограничение по бюджету'
    >>> problem += x2 == 3 * x1, 'Соотношение времени показа'
    >>> problem.solve()
    1
    
    >>> pulp.LpStatus[problem.status]
    'Optimal'
    
Значения переменных:

    >>> for v in problem.variables():
    ...     '{}={}'.format(v.name, v.varValue)
    'x1=95.238095'
    'x2=285.71429'


Значение целефой функции:

    >>> pulp.value(problem.objective)
    3142.85714


"""
