from IPython.core.display import display, HTML
import math

class WhileStatements_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La méthode du lissage exponentiel simple utilise la formule de récurrence forecast_t+1 = alpha * demand_t + (1-alpha) * forecast_t'))

    @staticmethod
    def solution():
        print('Solution:\n    current_forecast = initial_forecast\n    period = 0\n    while period < nb_period:\n        current_forecast = alpha * demand + (1-alpha) * current_forecast\n        period += 1\n    return current_forecast')

    @staticmethod
    def check(forecast):
        initial_forecast, demand, smoothing_factor, nb_period, expected_value = 500, 350, 0.6, 3, 359.6
        obtained_value = forecast(initial_forecast, demand, smoothing_factor, nb_period)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2}, {3} et {4}), mais valeur obtenue de {5}'.format(expected_value, initial_forecast, demand, smoothing_factor, nb_period, obtained_value))

class WhileStatements_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Ceci peut être vu comme une séquence définie de la manière suivante u_{n} = u_{n-1} * (1 + interest) + salary, u_0 = 10'))

    @staticmethod
    def solution():
        print('Solution:\n    money = 10\n    i = 0\n    while i < n:\n        money = money * (1 + interest) + salary\n        i += 1\n    return money')

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

class Strings_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Tronquez et formalisez la sous-chaîne composée des 2 derniers caractères afin de la comparer à l\'ensemble des provenances possibles'))

    @staticmethod
    def solution():
        print('Solution:\n    code = expedition_code[-2:].upper()\n    if code == \'QC\':\n        return \'Québec\'\n    elif code == \'ON\':\n        return \'Ontario\'\n    elif code == \'BC\':\n        return \'Colombie-Britannique\'\n    elif code == \'SK\':\n        return \'Saskatchewan\'\n    elif code == \'MB\':\n        return \'Manitoba\'\n    elif code == \'YT\':\n        return \'Yukon\'')

    @staticmethod
    def check(origin_shipment):
        expedition_code, expected_value = '2E4H7Y14ON', 'Ontario'
        obtained_value = origin_shipment(expedition_code)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, expedition_code, obtained_value))
        expedition_code, expected_value = '5dr5Q744yT', 'Yukon'
        obtained_value = origin_shipment(expedition_code)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, expedition_code, obtained_value))

class Strings_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Tronquez et convertissez en nombre la sous-chaîne composée des 4 premiers caractères afin de la comparer à la date limite'))

    @staticmethod
    def solution():
        print('Solution:\n    year = int(reference_product[:4])\n    return year >= 2004')

    @staticmethod
    def check(year_product):
        reference_product, expected_value = '200652Z568', True
        obtained_value = year_product(reference_product)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, reference_product, obtained_value))
        reference_product, expected_value = '19995SS5D2', False
        obtained_value = year_product(reference_product)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, reference_product, obtained_value))

class Strings_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Créez des sous-chaînes à partir des paramètres afin d\'avoir tous les morceaux à concaténer pour créer le code'))

    @staticmethod
    def solution():
        print("Solution:\n    return production_date[-2:] + production_date[2:4] + production_date[:2] + '-' + reference_product + '-' + shipment_location.upper()")

    @staticmethod
    def check(create_code):
        production_date, reference_product, shipment_location, expected_value = '03111994', 'FAD5E1Q', 'qc', '941103-FAD5E1Q-QC'
        obtained_value = create_code(production_date, reference_product, shipment_location)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, production_date, reference_product, shipment_location, obtained_value))

class Lists_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La formule de la moyenne mobile pour la période t+1 est 1/k * somme de i=t-k+1 à t des demandes de la période i'))

    @staticmethod
    def solution():
        print('Solution:\n    forecasted_demand = 0\n    for d in demand[-k:]:\n        forecasted_demand += d\n    return forecasted_demand / k')

    @staticmethod
    def check(moving_average_forecast):
        demand, k, expected_value = [103,130,125,123], 3, 126
        obtained_value = moving_average_forecast(demand, k)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1} et {2}), mais valeur obtenue de {3}'.format(expected_value, demand, nb_observation, obtained_value))

class Lists_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La formule de l\'écart moyen quadratique est 1/n * somme du carré de la différence des demandes et des prévisions'))

    @staticmethod
    def solution():
        print('Solution:\n    MSE = 0\n    for i in range(len(demand)):\n        MSE += (demand[i] - forecast[i])**2\n    return MSE/len(demand)')

    @staticmethod
    def check(MSE):
        demand, forecast, expected_value = [100,125,110,105,135,115], [105,112,120,110,103,135], 290.5
        obtained_value = MSE(demand, forecast)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1} et {2}), mais valeur obtenue de {3}'.format(expected_value, demand, forecast, obtained_value))

class Lists_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('La formule de l\'écart moyen  est 1/n * somme de la différence des demandes et des prévisions'))

    @staticmethod
    def solution():
        print('Solution:\n    forecast = initial_forecast\n    error = 0\n    for d in demand[:-1]:\n        error += d - forecast\n        forecast = alpha * d + (1-alpha) * forecast\n    error = (error + demand[-1] - forecast) / len(demand)\n    return error')

    @staticmethod
    def check(mean_error):
        initial_forecast, demand, alpha, expected_value = 650, [650, 678, 720, 785, 859, 920, 850], 0.4, 68.2356
        obtained_value = mean_error(initial_forecast, demand, alpha)
        if math.isclose(obtained_value, expected_value, abs_tol=0.001):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}, {2} et {3}), mais valeur obtenue de {4}'.format(expected_value, initial_forecast, demand, alpha, obtained_value))

class Lists_Q4:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('On peut itérer au travers de la liste et utiliser un compteur'))

    @staticmethod
    def solution():
        print('Solution:\n    from_Manitoba = 0\n    for product in products:\n        if origin_shipment(product) == \'Manitoba\':\n            from_Manitoba += 1\n    return from_Manitoba')

    @staticmethod
    def check(products_from_Manitoba):
        products, expected_value = ['90RC5451QC', 'O0993QQ1ON', '389FZIGKMB', 'J2P3W7Q2MB', '64657C0RON', '4T0WD7DVMB'], 3
        obtained_value = products_from_Manitoba(products)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, products, obtained_value))

class Lists_Q5:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Identifiez la référence du produit dans le code puis trouvez la séquence SK'))

    @staticmethod
    def solution():
        print('Solution:\n    defects = []\n    for product in products:\n        ref = product.split(\'-\')[1]\n        if \'SK\' in ref:\n            defects.append(product)\n    return defects')

    @staticmethod
    def check(find_defects):
        products, expected_value = ['020421-SOE5EJ-MB', '981101-558DSK-QC', '120131-6E4F5A-SK', '111121-6SKF5A-SK'], ['981101-558DSK-QC', '111121-6SKF5A-SK']
        obtained_value = find_defects(products)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({1}), mais valeur obtenue de {2}'.format(expected_value, products, obtained_value))

