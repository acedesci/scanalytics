from IPython.core.display import display, HTML
import math

class Dictionnaries_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Créez un dictionnaire pour compter le nombre de fornisseur pour chaque province puis prenez l\'enregistrement avec la plus grande valeur'))

    @staticmethod
    def solution():
        print('Solution:\n    count = {}\n    max_origin_value = 0\n    max_origin_province = 0\n    for supplier in suppliers:\n        count[supplier] = count.get(supplier, 0) + 1\n    for key in count:\n        if max_origin_value < count[key]:\n            max_origin_value = count[key]\n            max_origin_province = key\n    return provinces[max_origin_province]')

    @staticmethod
    def check(most_common_origin):
        suppliers, provinces, expected_value = ['QC', 'AB', 'ON', 'QC', 'QC', 'MB', 'MB', 'ON', 'QC', 'ON'], {'QC':'Québec','AB':'Alberta','ON':'Ontario','MB':'Manitoba'}, 'Québec'
        obtained_value = most_common_origin(suppliers, provinces)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2} et {3}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, suppliers, provinces))

class Dictionnaries_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Itérez à travers la liste et comparez la valeur du champ \'price\' avec le minimum courant'))

    @staticmethod
    def solution():
        print("Solution:\n    name = ''\n    price = 0\n    for client in clients:\n        if client['price'] > price:\n            name = client['name']\n            price = client['price']\n    return name")

    @staticmethod
    def check(find_client):
        clients, expected_value = [{'name':'John','price':3.14},{'name':'Fitz','price':2.71},{'name':'Gerald','price':1.61},{'name':'Ken','price':1.41},{'name':'Eddy','price':3.3}], 'Eddy'
        obtained_value = find_client(clients)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, clients))

class Dictionnaries_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Créez un nouveau dictionnaire et ajoutez les entrées des dictionnaires en paramètres'))

    @staticmethod
    def solution():
        print("Solution:\n    merged_clients = dict()\n    for client_id in clients1:\n        merged_clients[client_id] = clients1[client_id]\n    for client_id in clients2:\n        merged_clients[client_id] = clients2[client_id]\n    return merged_clients")

    @staticmethod
    def check(merge_clients):
        clients1, clients2, expected_value = {'CLI_1_001':'John','CLI_1_002':'Fitz','CLI_1_003':'Gerald'}, {'CLI_2_001':'Ken','CLI_2_002':'Eddy'}, {'CLI_1_001':'John','CLI_1_002':'Fitz','CLI_1_003':'Gerald','CLI_2_001':'Ken','CLI_2_002':'Eddy'}
        obtained_value = merge_clients(clients1, clients2)
        if obtained_value == expected_value:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2} et {3}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, clients1, clients2))

class Tuples_Q1:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Utilisez la formule (X-0.577*R, X+0.577*R) où X est la moyenne des moyennes et R est la moyenne des étendues. En d\'autres mots, il faut calculer la moyenne et l\'étendue des observations à l\'intérieur de chaque échantillon. Par la suite, il faut calculer respectivement la moyenne de ces moyennes et la moyenne de ces étendues. Finalement, il faut utiliser la formule proposée.'))

    @staticmethod
    def solution():
        print("Solution:\n    avg_average = 0\n    avg_span = 0\n    for sample in samples:\n        average = 0\n        for observation in sample:\n            average += observation\n        average /= len(sample)\n        avg_average += average\n        avg_span += max(sample) - min(sample)\n    avg_average /= len(samples)\n    avg_span /= len(samples)\n    return avg_average - 0.577 * avg_span, avg_average + 0.577 * avg_span")

    @staticmethod
    def check(limit_control):
        samples, expected_value = [[5,6,8,5,6],[6,5,6,8,4],[7,5,5,6,3]], (3.55, 7.78)
        obtained_value = limit_control(samples)
        if math.isclose(obtained_value[0], expected_value[0], abs_tol=0.01) and math.isclose(obtained_value[1], expected_value[1], abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, samples))

class Tuples_Q2:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Créez une liste des clients basés en Ontario puis convertissez cette liste en tuple'))

    @staticmethod
    def solution():
        print("Solution:\n    clients_from_ON = []\n    for client in clients:\n        if client['origin'] == 'ON':\n            clients_from_ON.append(client['name'])\n    return tuple(clients_from_ON)")

    @staticmethod
    def check(from_Ontario):
        clients, expected_value = [{'name':'John','origin':'QC'},{'name':'Fitz','origin':'ON'},{'name':'Gerald','origin':'QC'},{'name':'Ken','origin':'AB'},{'name':'Eddy','origin':'ON'}], ('Fitz', 'Eddy')
        obtained_value = from_Ontario(clients)
        correct = True
        for v in obtained_value:
            if v not in expected_value:
                correct = False
        for v in expected_value:
            if v not in obtained_value:
                correct = False
        if not isinstance(obtained_value, tuple):
            correct = False
        if correct:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, clients))

class Tuples_Q3:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Calculez la moyenne des prix puis trouvez les fournisseurs moins cher que la moyenne'))

    @staticmethod
    def solution():
        print("Solution:\n    suppliers_lower_than_average = []\n    average = 0\n    for supplier in suppliers:\n        average += supplier['price']\n    average /= len(suppliers)\n    for supplier in suppliers:\n        if supplier['price'] < average:\n            suppliers_lower_than_average.append(supplier['name'])\n    return tuple(suppliers_lower_than_average)")

    @staticmethod
    def check(lower_than_average):
        suppliers, expected_value = [{'name':'John','price':3.14},{'name':'Fitz','price':2.71},{'name':'Gerald','price':1.61},{'name':'Ken','price':1.41},{'name':'Eddy','price':3.3}], ('Gerald', 'Ken')
        obtained_value = lower_than_average(suppliers)
        correct = True
        for v in obtained_value:
            if v not in expected_value:
                correct = False
        for v in expected_value:
            if v not in obtained_value:
                correct = False
        if not isinstance(obtained_value, tuple):
            correct = False
        if correct:
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, suppliers))

class Tuples_Q4:
    @staticmethod
    def hint():
        print('Indice:')
        display(HTML('Pour chaque valeur de demande, créez une tranche composée des 3 valeurs précédentes de demande et faites la prévision'))

    @staticmethod
    def solution():
        print("Solution:\n    MSE = 0\n    for i in range(3, len(demands)):\n        forecast = average_forecast(*demands[i-3:i])\n        MSE += (demands[i] - forecast)**2\n    return MSE / (len(demands) - 3)")

    @staticmethod
    def check(MSE):
        demands, expected_value = [100,125,111,105,135,115], 169.37
        obtained_value = MSE(demands)
        if math.isclose(obtained_value, expected_value, abs_tol=0.01):
            print('Correct')
        else:
            print('Incorrect: Valeur attendue de {0} avec les paramètres ({2}), mais valeur obtenue de {1}'.format(expected_value, obtained_value, demands))
