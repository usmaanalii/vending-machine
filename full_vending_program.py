import csv
import os
from random import randint, uniform

# A_csv_to_dicts.py

# File converts the csv files into the required data structures (dictionaries)


# denominations dictionary converter
def curr_to_dict(currency_file):
    denominations = {}
    with open(currency_file, 'r') as my_file:
        reader = csv.reader(my_file)
        for row in reader:
            value = []
            for column in row:
                value.append(column)
            denominations[row[0]] = value[1:]
    return denominations


# denominations stock dictionary converter
def denom_stock_to_dict(stock_file, currency):
    denom_stock = {}

    with open(stock_file, 'r') as my_file:
        reader = csv.reader(my_file)
        value = {}
        for row in reader:
            value[row[0]] = int(row[1])
        denom_stock[currency] = value
    return denom_stock


# products stock dictionary converter
def products_to_dict(prod_file):
    products = {}
    with open(prod_file, 'r') as my_file:
        reader = csv.reader(my_file)
        for row in reader:
            value = {}
            value['product name'] = row[1]
            value['price'] = float(row[2])
            value['count'] = int(row[3])
            products[int(row[0])] = value
    return products

# data in dict format
currency = curr_to_dict('currency.csv')
denom_stock = denom_stock_to_dict('dstock.csv', 'GBP')
products = products_to_dict('products.csv')


# F_Change.py
def change(amount, coins, result=None):
    result = [] if result is None else result
    if len(coins) == 0:
        return len(result), result

    max_coin = max(coins)
    coins.remove(max_coin)
    answer = amount // max_coin
    if answer == 0 and max_coin < amount:
        result = result + ([max_coin] * answer)
        return result
    else:
        result = result + ([max_coin] * answer)
        return change(amount % max_coin, coins, result)


coin_list = [200, 100, 50, 20, 10, 5, 2, 1]


def formatter(amount, coins, result=None):
    if amount < 0:
        return []
    result_coins = change(amount, coins, result=None)[1]

    change_given = []
    for coin in result_coins:
        change_given.append(str(format(coin / float(100), '.2f')))
    return change_given


# Script adds to the relevent logging files

# B_purchase_logging.py


def add_change_log(code, input_val):

    coins_given = formatter(int(float(format
                            (input_val - products[code]['price'],
                             '.2f')) * 100), [200, 100, 50, 20, 10, 5, 2, 1])

    change = [str(code).zfill(2), str(round(input_val, 2))]
    change.extend(coins_given)
    with open('changes.txt', 'a') as my_file:
        my_file.write(', '.join(change))
        my_file.write('\n')


def add_product_log(code):
    product_log = [str(code).zfill(2), products[code]['product name'],
                   products[code]['price'], (products[code]['count'])]
    with open('purchase_log.csv', 'a') as my_file:
        writer = csv.writer(my_file, dialect='excel')
        writer.writerow(product_log)


def add_denom_log(code, input_val):
    coins_given = formatter(int(float(format
                            (input_val - products[code]['price'],
                             '.2f')) * 100), [200, 100, 50, 20, 10, 5, 2, 1])
    for coin in coins_given:
        denom_log = [coin, denom_stock['GBP'][coin]]
        with open('dstock_log.csv', 'a') as my_file:
            writer = csv.writer(my_file)
            writer.writerow(denom_log)


def add_denom_log_2():
    with open('dstock_log.csv', 'a') as my_file:
        writer = csv.writer(my_file)
        for row in sorted(denom_stock['GBP'].iteritems()):
            writer.writerow(row)


# coin checking function, needs moving
def coin_check(code, input_val):
    change_given = format(input_val - products[code]['price'], '.2f')
    coin_list = denom_stock['GBP'].keys()
    if ((change_given in coin_list or change_given is '0.0') and
       change_given is not '0.0'):
        coin_count = denom_stock['GBP'][change_given]
        if coin_count > 1 or change_given is '0.0':
            print(change_given, 'Exact change CAN be returned')
        # this needs to decrement the coin count in denom_log
        else:
            print(change_given)
    else:
        print(change_given)


# C_purchase_function.py

def purchase_test(code, input_val):
    if code in products:  # if code exists in product list
        if input_val >= products[code]['price']:  # if enough money
            if products[code]['count'] > 0:  # if item in stock

                change_given = format(input_val -
                                      products[code]['price'], '.2f')
                coins_given = formatter(int
                                        (float(format
                                         (input_val - products[code]['price'],
                                          '.2f')) * 100),
                                        [200, 100, 50, 20, 10, 5, 2, 1])

                if float(change_given) == 0:
                    products[code]['count'] -= 1
                    # changes.txt file
                    add_change_log(code, input_val)  # add change 'log'
                    # products.csv file
                    add_product_log(code)  # add product 'log'
                    # if required coins are in stock

                elif len(coins_given) > 0:
                    if all(denom_stock['GBP'][coin] > 0 for
                           coin in coins_given):
                        products[code]['count'] -= 1
                        for coin in coins_given:
                            denom_stock['GBP'][coin] -= 1
                        # decrement stock count
                        # changes.txt file
                        add_change_log(code, input_val)  # add change 'log'
                        # products.csv file
                        add_product_log(code)  # add product 'log'
                        # dstock.csv file
                        add_denom_log(code, input_val)  # add denom 'log'
                    else:
                        with open('changes.txt', 'a') as my_file:
                            my_file.write("Can't return change\n")
            else:
                with open('changes.txt', 'a') as my_file:
                    my_file.write("Item out of stock\n")  # if stock count < 1
        else:
            with open('changes.txt', 'a') as my_file:
                my_file.write("Insufficient funds\n")  # if not enough money
    else:
            with open('changes.txt', 'a') as my_file:  # if code doesn't exist
                my_file.write("Wrong code inserted\n")
    coins_given = formatter(int(float(format
                            (input_val - products[code]['price'],
                             '.2f')) * 100), [200, 100, 50, 20, 10, 5, 2, 1])
    return coins_given


# D_dict_to_csv.py

# used to create a temporary products file after orders
def prod_updated_csv(in_csv, out_csv):
    if os.path.exists('purchase_log.csv') is False:
        open('purchase_log.csv', 'w')
    upd_products = products_to_dict(in_csv)
    full = products.keys()
    current = upd_products.keys()
    missing = list(set(full) - set(current))

    for i in missing:
        upd_products[i] = products[i]

    fields = ['product name', 'price', 'count']
    with open(out_csv, 'w') as out_file:
        writer = csv.DictWriter(out_file, fields)
        for key in upd_products:
            writer.writerow(({field: upd_products[key].get(field) for
                             field in fields}))

prod_updated_csv('purchase_log.csv', 'products_updated_temp.csv')


# issue with csv, workaround
def add_column(in_csv, out_csv):

    with open(in_csv, 'r') as input_file, open(out_csv, 'wb') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        all = []
        row = next(reader)
        row.insert(0, 1)
        all.append(row)
        for k, row in enumerate(reader):
            all.append([str(k + 2)] + row)
        writer.writerows(all)

add_column('products_updated_temp.csv', 'products_updated.csv')


# used to create a temporary denom file after orders
def denom_updated_csv(in_csv, out_csv):
    if os.path.exists('dstock_log.csv') is False:
        open('dstock_log.csv', 'w')
    upd_denom_stock = denom_stock_to_dict(in_csv, 'GBP')
    full = denom_stock['GBP'].keys()
    current = upd_denom_stock['GBP'].keys()
    missing = list(set(full) - set(current))

    for i in missing:
        upd_denom_stock['GBP'][i] = denom_stock['GBP'][i]

    coins = upd_denom_stock[upd_denom_stock.keys()[0]].keys()
    coin_to_counts = []
    for i in coins:
        pair = (str(format(float(i), '.2f')),
                upd_denom_stock[upd_denom_stock.keys()[0]][i])
        coin_to_counts.append(pair)

    with open(out_csv, 'w') as out_file:
        csv_out = csv.writer(out_file)
        for row in coin_to_counts:
            csv_out.writerow(row)

denom_updated_csv('dstock_log.csv', 'dstock_updated.csv')


# E_remove_files.py

# remove the temporary and logging csv files
def clean():
    to_remove = ['products_updated_temp.csv',
                 'purchase_log.csv',
                 'dstock_log.csv',
                 'products.csv',
                 'dstock.csv'
                 ]

    for f in to_remove:
        os.remove(f)

    os.rename('products_updated.csv', 'products.csv')
    os.rename('dstock_updated.csv', 'dstock.csv')


# main.py

def main(code, input_val):

    # write the results of each simulation to simulations.tct
    if os.path.exists('simulations.txt') is False:
        open('simulations.txt', 'w')
    with open('simulations.txt', 'a') as my_file:
        simulation = [code, format(input_val, '.2f')]
        writer = csv.writer(my_file, dialect='excel')
        writer.writerow(simulation)

    # simulation
    purchase_test(code, input_val)

    # dict to csv
    prod_updated_csv('purchase_log.csv', 'products_updated_temp.csv')
    add_column('products_updated_temp.csv', 'products_updated.csv')
    denom_updated_csv('dstock_log.csv', 'dstock_updated.csv')

    # clean
    clean()


def test(num):
    for i in range(0, num):
        main(randint(1, 4), round(uniform(0.5, 2) / 0.01) * 0.01)

test(100)
