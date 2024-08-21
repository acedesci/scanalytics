from IPython.core.display import display, HTML
import math

class HelloWorld_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Utilisez la fonction <a href="https://www.w3schools.com/python/ref_func_print.asp">print()</a>. Regardez le Chapitre 1 du livre, à la section <b>The First Program</b>'))

    @staticmethod
    def solution():
        print('Solution:\nprint(\'Hello World!\')')

class Types:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Regardez le Chapitre 1 du livre, à la section <b>Values et Types</b>'))

class Types_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Une variable <i>int</i> est une variable avec comme valeur un nombre entier'))

    @staticmethod
    def solution():
        print('Solution:\nvariable = 0')

    @staticmethod
    def check(variable):
        expected_value = type(1)
        obtained_value = type(variable)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0}, mais valeur obtenue de {1}'.format(expected_value, obtained_value))

class Types_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Une variable <i>float</i> est une variable avec comme valeur un nombre réel'))

    @staticmethod
    def solution():
        print('Solution:\nvariable = 3.14')

    @staticmethod
    def check(variable):
        expected_value = type(1.0)
        obtained_value = type(variable)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0}, mais valeur obtenue de {1}'.format(expected_value, obtained_value))

class Types_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Une variable <i>str</i> est une variable avec comme valeur un texte, avec des simples guillemets (ou doubles) au début et à la fin'))

    @staticmethod
    def solution():
        print('Solution:\nvariable = \'python\'')

    @staticmethod
    def check(variable):
        expected_value = type('1')
        obtained_value = type(variable)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0}, mais valeur obtenue de {1}'.format(expected_value, obtained_value))

class ArithmeticOperator:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Regardez le Chapitre 1 du livre, à la section <b>Arithmetic Operators</b>'))

class ArithmeticOperator_Q1:
    @staticmethod
    def solution():
        print('Solution:\n    return demand_A + demand_B')

    @staticmethod
    def check(total_demand):
        demand_A, demand_B, expected_value = 2.3, 7, 9.3
        obtained_value = total_demand(demand_A, demand_B)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1} et {2}), mais valeur obtenue de {3}'.format(expected_value, demand_A, demand_B, obtained_value))

class ArithmeticOperator_Q2:
    @staticmethod
    def solution():
        print('Solution:\n    return inventory - demand')

    @staticmethod
    def check(remaining_inventory):
        inventory, demand, expected_value = 9.3, 2.3, 7
        obtained_value = remaining_inventory(inventory, demand)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1} et {2}), mais valeur obtenue de {3}'.format(expected_value, inventory, demand, obtained_value))

class ArithmeticOperator_Q3:
    @staticmethod
    def solution():
        print('Solution:\n    return initial_price * (1 - discount/100)')

    @staticmethod
    def check(discount_price):
        initial_price, discount, expected_value = 500, 25, 375
        obtained_value = discount_price(initial_price, discount)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1} et {2}), mais valeur obtenue de {3}'.format(expected_value, initial_price, discount, obtained_value))

class Functions_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La formule de la QEC peut être trouvée <a href="https://en.wikipedia.org/wiki/Economic_order_quantity">ici</a>'))

    @staticmethod
    def solution():
        print('Solution:\n    return (2 * demand * order_cost / holding_cost) ** 0.5')

    @staticmethod
    def check(EOQ):
        demand, order_cost, holding_cost, expected_value = 800, 28, 10*0.35, math.sqrt(12800)
        obtained_value = EOQ(demand, order_cost, holding_cost)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, demand, order_cost, holding_cost, obtained_value))

class Functions_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La formule du coût total annuel peut être trouvée <a href="https://en.wikipedia.org/wiki/Economic_order_quantity">ici</a>'))

    @staticmethod
    def solution():
        print('Solution:\n    return (order_quantity/2 + safety_stock) * holding_cost + demand / order_quantity * order_cost + demand * purchase_price')

    @staticmethod
    def check(annual_total_cost):
        purchase_price, order_quantity, order_cost, holding_cost, = 30, 800, 28, 10*0.35
        safety_stock, demand, expected_value = int(order_quantity*0.1), order_quantity*12, 290016
        obtained_value = annual_total_cost(purchase_price, order_quantity, safety_stock, demand, order_cost, holding_cost)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3}, {4}, {5} et {6}), mais valeur obtenue de {7}'.format(expected_value, purchase_price, order_quantity, safety_stock, demand, order_cost, holding_cost, obtained_value))

class Functions_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La distance euclidienne entre deux points est la racine carrée de la somme du carré des différences'))

    @staticmethod
    def solution():
        print('Solution:\n    return math.sqrt((x_warehouse - x_client)**2 + (y_warehouse - y_client)**2)')

    @staticmethod
    def check(distance):
        x_warehouse, y_warehouse, x_client, y_client, expected_value = 1, 1, 0, 0, math.sqrt(2)
        obtained_value = distance(x_warehouse, y_warehouse, x_client, y_client)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3} et {4}), mais valeur obtenue de {5}'.format(expected_value, x_warehouse, y_warehouse, x_client, y_client, obtained_value))

class Conditions_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Regardez pour chaque période si ce qu\'il reste dans les stocks plus les nouvelles fournitures est assez pour satisfaire la nouvelle demande'))

    @staticmethod
    def solution():
        print('Solution:\n    inventory = supply1\n    if demand1 > inventory:\n        return True\n    inventory = inventory - demand1 + supply2\n    if demand2 > inventory:\n        return True\n    inventory = inventory - demand2 + supply3\n    if demand3 > inventory:\n        return True\n    return False')

    @staticmethod
    def check(shortage):
        demand1, supply1, demand2, supply2, demand3, supply3, expected_value = 20, 25, 15, 25, 15, 10, False
        obtained_value = shortage(demand1, supply1, demand2, supply2, demand3, supply3)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3}, {4}, {5} et {6}), mais valeur obtenue de {7}'.format(expected_value, demand1, supply1, demand2, supply2, demand3, supply3, obtained_value))
        demand1, supply1, demand2, supply2, demand3, supply3, expected_value = 20, 25, 35, 25, 15, 10, True
        obtained_value = shortage(demand1, supply1, demand2, supply2, demand3, supply3)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3}, {4}, {5} et {6}), mais valeur obtenue de {7}'.format(expected_value, demand1, supply1, demand2, supply2, demand3, supply3, obtained_value))

class Conditions_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Comparez la proportion de défauts avec le maximum toléré'))

    @staticmethod
    def solution():
        print('Solution:\n    return defect/sample_size <= criterion')

    @staticmethod
    def check(quality_control):
        sample_size, defect, criterion, expected_value = 250, 11, 0.05, True
        obtained_value = quality_control(sample_size, defect, criterion)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, sample_size, defect, criterion, obtained_value))
        defect, expected_value = 15, False
        obtained_value = quality_control(sample_size, defect, criterion)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, sample_size, defect, criterion, obtained_value))

class ForStatements_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La méthode du lissage exponentiel simple utilise la formule de récurrence forecast_t+1 = alpha * demand_t + (1-alpha) * forecast_t'))

    @staticmethod
    def solution():
        print('Solution:\n    current_forecast = initial_forecast\n    for period in range(nb_period):\n        current_forecast = alpha * demand + (1-alpha) * current_forecast\n    return current_forecast')

    @staticmethod
    def check(forecast):
        initial_forecast, demand, alpha, nb_period, expected_value = 500, 350, 0.6, 3, 359.6
        obtained_value = forecast(initial_forecast, demand, alpha, nb_period)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3} et {4}), mais valeur obtenue de {5}'.format(expected_value, initial_forecast, demand, alpha, nb_period, obtained_value))


class ForStatements_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Ceci peut être vu comme une séquence définie de la manière suivante u_{n} = u_{n-1} * (1 + interest) + salary, u_0 = 10'))

    @staticmethod
    def solution():
        print('Solution:\n    money = 10\n    for i in range(n):\n        money = money * (1 + interest) + salary\n    return money')

    @staticmethod
    def check(bank_account):
        interest, salary, n, expected_value = 0.05, 2000, 0, 10
        obtained_value = bank_account(interest, salary, n)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, interest, salary, n, obtained_value))
        n, expected_value = 3, 6316.57
        obtained_value = bank_account(interest, salary, n)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, interest, salary, n, obtained_value))

class Recursions_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La méthode du lissage exponentiel simple utilise la formule de récurrence forecast_t+1 = alpha * demand_t + (1-alpha) * forecast_t'))

    @staticmethod
    def solution():
        print('Solution:\n    if nb_period == 0:\n        return initial_forecast\n    else:\n        return alpha * demand + (1-alpha) * forecast(initial_forecast, demand, alpha, nb_period-1)')

    @staticmethod
    def check(forecast):
        initial_forecast, demand, alpha, nb_period, expected_value = 500, 350, 0.6, 3, 359.6
        obtained_value = forecast(initial_forecast, demand, alpha, nb_period)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3} et {4}), mais valeur obtenue de {5}'.format(expected_value, initial_forecast, demand, alpha, nb_period, obtained_value))

class Recursions_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Ceci peut être vu comme une séquence définie de la manière suivante u_{n} = u_{n-1} * (1 + interest) + salary, u_0 = 10'))

    @staticmethod
    def solution():
        print('Solution:\n    if n == 0:\n        return 10\n    return bank_account(interest, salary, n - 1) * (1 + interest) + salary')

    @staticmethod
    def check(bank_account):
        interest, salary, n, expected_value = 0.05, 2000, 0, 10
        obtained_value = bank_account(interest, salary, n)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, interest, salary, n, obtained_value))
        n, expected_value = 3, 6316.57
        obtained_value = bank_account(interest, salary, n)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, interest, salary, n, obtained_value))
