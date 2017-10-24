import json
from random import choice

def generate_per():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z', 'y', 'x']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(name) != 5:
        name += choice(letters)

    while len(tel) != 9:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person

def write_json(person_dict):
    try:
        data = json.load(open('persons_2.json'))
    except:
        data = []

    data.append(person_dict)

    with open('persons_2.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():

    for i in range(5):
        write_json(generate_per())

if __name__ == '__main__':
    main()
