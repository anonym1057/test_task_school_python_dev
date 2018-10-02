"""
author: Nosova Olga
email: nosova-olenka@mail.ru

Write a program that takes two strings in JSON format and compares them.
The program should output the difference between those JSON strings.
"""
import json


def compare_json(str1: str, str2: str):
    """
    Campare strings on format json.
    :param str1: jstrings on format json.
    :param str2: strings on format json.
    :return: difference between jsons
    """
    try:
        json1 = json.loads(str1)
    except Exception as e:
        print("Error: can't convert to json")
        return []
        #raise TypeError(f"{str1} can't convert to json")

    try:
        json2 = json.loads(str2)
    except Exception as e:
        print("Error: can't convert to json")
        return []
        #raise TypeError(f"{str2} can't convert to json")

    key2 = set(json2.keys())
    key1 = set(json1.keys())

    difference = [[{k: json1[k]}, {k: json2[k]}] for k in key1.intersection(key2) if json1[k] != json2[k]]
    difference =difference + [[None, {k: json2[k]}] for k in key2.difference(key1)]
    difference =difference + [[{k: json1[k]},None] for k in key1.difference(key2)]

    return difference


if __name__ == '__main__':
    s1 = input("String 1: ")
    s2 = input("String 2: ")
    print("Difference: ")
    for pair in compare_json(s1, s2):
        print(pair[0],pair[1],sep=',')
