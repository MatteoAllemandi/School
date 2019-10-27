key_word = "ITISDELPOZZO"

phrase_value_list= []
key_value_list = []
result_list = []
str_result = ""

key_value_dict = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26,
}

back_to_normal_dict = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H",
    9:"I",
    10:"J",
    11:"K",
    12:"L",
    13:"M",
    14:"N",
    15:"O",
    16:"P",
    17:"Q",
    18:"R",
    19:"S",
    20:"7",
    21:"U",
    22:"V",
    23:"W",
    24:"X",
    25:"Y",
    26:"Z",
}

phrase = input("insert message (MAX 26): ")

def CodeString(phrase):
    for i in phrase.upper():
        phrase_value_list.append(key_value_dict[i])

    for i in key_word.upper():
        key_value_list.append(key_value_dict[i])

    for i in range(0,len(phrase_value_list)):
        result_list.append(phrase_value_list[i] + key_value_list[i])
        str_result = str_result + str(result_list[i])

print("Stringa convertita -> " + CodeString(phrase))
