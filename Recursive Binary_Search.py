from random import randint

random_list = []


def random_numbers():
    new_number = randint(0, 999)
    if new_number not in random_list:
        random_list.append(new_number)
    if len(random_list) == 100:
        return False
    else:
        return random_numbers()


random_numbers()

sorted_list = sorted(random_list)
mid_position = len(sorted_list) // 2
mid_number = sorted_list[mid_position]

with open("../Index(s).txt", "a") as indexss:
    for item in sorted_list:
        indexss.write(str(f'{item}, '))

print(sorted_list)
num = int(input('What number index are you looking for?: '))

index = sorted_list.index(num)
mid_position = len(sorted_list) // 2
mid_number = sorted_list[mid_position]


def binary_search():  # lista, chave,
    """Search for a certain number in a list and Returns the index from searched number."""

    global sorted_list, mid_position, mid_number, index, num  # nao recomendado usar variavel global em recursividade

    print(f"Current list is: \n{sorted_list}")
    print(f'Current middle position is: {mid_position}')
    print(f'Current middle positional number is: {mid_number}')

    keep = input('If you want to stop the program type "N", otherwise just press "Enter": ').upper()

    if keep == 'N':
        return False

    else:
        if num not in sorted_list:  # Se o número não estiver na lista
            print('The typed number is not in the list.')
            return False

        elif mid_number == num:  # Se o número do meio já for o procurado
            print(f'The number {num} is at index: {index}.')
            return False

        elif len(sorted_list) == 3 and sorted_list[2] == num:  # Lista com 3 elementos e o procurado está à direita.
            print(f'The number {num} is at index: {index}.')
            return False

        elif mid_number < num:  # Se o número do meio for menor que o número procurado.
            sorted_list = sorted_list[mid_position:]
            mid_position = len(sorted_list) // 2
            mid_number = sorted_list[mid_position]
            return binary_search()  # retornar lista atualizada

        else:  # Se o número do meio for maior que o número procurado.
            sorted_list = sorted_list[:mid_position]
            mid_position = len(sorted_list) // 2
            mid_number = sorted_list[mid_position]
            return binary_search()  # retornar lista atualizada


binary_search()

with open("../Index(s).txt", "a") as indexss:
    indexss.write(str(f"\nThe number {num} you are looking for is at index: {index}.\n"))  # add the number
    indexss.close()  # Por que usar o close() ?
