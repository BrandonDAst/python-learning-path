def run():
    my_dictionary = {
        'K1': 1,
        'K2': 2,
        'K3': 3,
        'K4': 4,
    }

    print(my_dictionary['K1'])

    for k in my_dictionary.keys():
        print(k)
    for v in my_dictionary.values():
        print(v)
    for k, v in my_dictionary.items():
        print(f"K: {k}, V: {v}")


if __name__ == '__main__':
    run()
