import ast
import random


def fast_exp(a, b, n):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b //= 2
    return result


def extended_euclidean(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = extended_euclidean(b, a % b)
        return y, x - (a // b) * y


def elgamal_encrypt(plaintext_list, p, g, y):
    ciphertext_list = []
    for m in plaintext_list:
        k = random.randint(1, 16318)
        a = fast_exp(g, k, p)
        b = (int(m) * fast_exp(y, k, p)) % p
        ciphertext_list.append((a, b))
    return ciphertext_list


def elgamal_decrypt(ciphertext_list, p, x):
    decrypted_text_list = []
    for a, b in ciphertext_list:
        s = fast_exp(a, x, p)
        m = (b * extended_euclidean(s, p)[0]) % p
        decrypted_text_list.append(str(m))
    return decrypted_text_list


def word_to_number(word):
    mapping = {'А': '10', 'Б': '11', 'В': '12', 'Г': '13', 'Д': '14', 'Е': '15', 'Ж': '16', 'З': '17', 'И': '18',
               'Й': '19', 'K': '20', 'Л': '21', 'М': '22', 'Н': '23', 'О': '24', 'П': '25', 'Р': '26', 'С': '27',
               'Т': '28', 'У': '29', 'Ф': '30', 'Х': '31', 'Ц': '32', 'Ч': '33', 'Ш': '34', 'Щ': '35', 'Ъ': '36',
               'Ы': '37', 'Ь': '38', 'Э': '39', 'Ю': '40', 'Я': '41', 'A': '42', 'B': '43', 'C': '44', 'D': '45',
               'E': '46', 'F': '47', 'G': '48', 'H': '49', 'I': '50', 'J': '51', 'K': '52', 'L': '53', 'M': '54',
               'N': '55', 'O': '56', 'P': '57', 'Q': '58', 'R': '59', 'S': '60', 'T': '61', 'U': '62', 'V': '63',
               'W': '64', 'X': '65', 'Y': '66', 'Z': '67', ' ': '68', ',': '69', '.': '70'}
    number_list = [mapping[char] for char in word]
    return number_list


def number_to_word(number_list):
    mapping = {'10': 'А', '11': 'Б', '12': 'В', '13': 'Г', '14': 'Д', '15': 'Е', '16': 'Ж', '17': 'З', '18': 'И',
               '19': 'Й', '20': 'K', '21': 'Л', '22': 'М', '23': 'Н', '24': 'О', '25': 'П', '26': 'Р', '27': 'С',
               '28': 'Т', '29': 'У', '30': 'Ф', '31': 'Х', '32': 'Ц', '33': 'Ч', '34': 'Ш', '35': 'Щ', '36': 'Ъ',
               '37': 'Ы', '38': 'Ь', '39': 'Э', '40': 'Ю', '41': 'Я', '42': 'A', '43': 'B', '44': 'C', '45': 'D',
               '46': 'E', '47': 'F', '48': 'G', '49': 'H', '50': 'I', '51': 'J', '52': 'K', '53': 'L', '54': 'M',
               '55': 'N', '56': 'O', '57': 'P', '58': 'Q', '59': 'R', '60': 'S', '61': 'T', '62': 'U', '63': 'V',
               '64': 'W', '65': 'X', '66': 'Y', '67': 'Z', '68': ' ', '69': ',', '70': '.'}
    word = ''.join(mapping.get(str(num), '') for num in number_list)
    return word


p = 16319
g = 2
x = 123
y = fast_exp(g, x, p)

plaintext = "WORD"
print("Plaintext:", plaintext)

plaintext_number_list = word_to_number(plaintext)
print(plaintext_number_list)

ciphertext = elgamal_encrypt(plaintext_number_list, p, g, y)
decrypted_text = elgamal_decrypt(ciphertext, p, x)
decrypted_word = number_to_word(decrypted_text)

print("Ciphertext:", ciphertext)
print("Decrypted numbers:", decrypted_text)
print("Decrypted text:", decrypted_word)

# with open("F:\output.txt", "w") as f:
#     f.write(str(ciphertext))
#
# with open('F:\output.txt', 'r') as f:
#     content = f.read()
#     ciphertext_from_file = ast.literal_eval(content)
#
# decrypted_text_from_file = elgamal_decrypt(ciphertext_from_file, p, x)
# decrypted_word_from_file = number_to_word(decrypted_text_from_file)
# with open("F:\output2.txt", "w") as f:
#     f.write(decrypted_word_from_file)
