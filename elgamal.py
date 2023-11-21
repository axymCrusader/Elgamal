import random


def fast_power(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        # If the exponent is odd, multiply the result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Now exponent is even, divide it by 2
        exponent = exponent // 2
        base = (base * base) % modulus

    return result


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def generate_keys():
    # Choose a large prime number P
    P = 1234567890123456789012345678901234567890123456789

    # Choose a primitive root modulo P, for simplicity, we choose g = 2
    g = 2

    # Choose a private key (a) randomly
    private_key = random.randint(2, P - 2)

    # Calculate the public key (A)
    public_key = fast_power(g, private_key, P)

    return P, g, private_key, public_key


def encrypt(message, P, g, public_key):
    # Choose a random value (k) as the session key
    k = random.randint(2, P - 2)

    # Calculate the first part of the ciphertext (C1)
    C1 = fast_power(g, k, P)

    # Calculate the second part of the ciphertext (C2)
    C2 = (message * fast_power(public_key, k, P)) % P

    return C1, C2


def decrypt(C1, C2, P, private_key):
    # Calculate the shared secret
    s = fast_power(C1, private_key, P)

    # Calculate the modular inverse of the shared secret
    s_inverse = mod_inverse(s, P)

    # Calculate the decrypted message
    decrypted_message = (C2 * s_inverse) % P

    return decrypted_message


def word_to_number(word):
    mapping = {'А': '10', 'Б': '11', 'В': '12', 'Г': '13', 'Д': '14', 'Е': '15', 'Ж': '16', 'З': '17', 'И': '18',
               'Й': '19', 'K': '20', 'Л': '21', 'М': '22', 'Н': '23', 'О': '24', 'П': '25', 'Р': '26', 'С': '27',
               'Т': '28', 'У': '29', 'Ф': '30', 'Х': '31', 'Ц': '32', 'Ч': '33', 'Ш': '34', 'Щ': '35', 'Ъ': '36',
               'Ы': '37', 'Ь': '38', 'Э': '39', 'Ю': '40', 'Я': '41', 'A': '42', 'B': '43', 'C': '44', 'D': '45',
               'E': '46', 'F': '47', 'G': '48', 'H': '49', 'I': '50', 'J': '51', 'k': '52', 'L': '53', 'M': '54',
               'N': '55', 'O': '56', 'P': '57', 'Q': '58', 'R': '59', 'S': '60', 'T': '61', 'U': '62', 'V': '63',
               'W': '64', 'X': '65', 'Y': '66', 'Z': '67', ' ': '68', ',': '69', '.': '70'}
    number_list = [mapping[char] for char in word]
    return number_list


def number_to_word(number_list):
    mapping = {'10': 'А', '11': 'Б', '12': 'В', '13': 'Г', '14': 'Д', '15': 'Е', '16': 'Ж', '17': 'З', '18': 'И',
               '19': 'Й', '20': 'K', '21': 'Л', '22': 'М', '23': 'Н', '24': 'О', '25': 'П', '26': 'Р', '27': 'С',
               '28': 'Т', '29': 'У', '30': 'Ф', '31': 'Х', '32': 'Ц', '33': 'Ч', '34': 'Ш', '35': 'Щ', '36': 'Ъ',
               '37': 'Ы', '38': 'Ь', '39': 'Э', '40': 'Ю', '41': 'Я', '42': 'A', '43': 'B', '44': 'C', '45': 'D',
               '46': 'E', '47': 'F', '48': 'G', '49': 'H', '50': 'I', '51': 'J', '52': 'k', '53': 'L', '54': 'M',
               '55': 'N', '56': 'O', '57': 'P', '58': 'Q', '59': 'R', '60': 'S', '61': 'T', '62': 'U', '63': 'V',
               '64': 'W', '65': 'X', '66': 'Y', '67': 'Z', '68': ' ', '69': ',', '70': '.'}
    word = ''.join(mapping.get(str(num), '') for num in number_list)
    return word


def split_string(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]


def join_numbers(number_list):
    joined_string = ''.join(number_list)
    joined_number = int(joined_string)
    return joined_number


plaintext = "WORD"

plaintext_number_list = word_to_number(plaintext)
plaintext_number = join_numbers(plaintext_number_list)


P, g, private_key, public_key = generate_keys()

C1, C2 = encrypt(plaintext_number, P, g, public_key)

decrypted_message = decrypt(C1, C2, P, private_key)
decrypted_message_list = split_string(str(decrypted_message))

print("Original Message:", plaintext)
print("Encrypted C1:", C1)
print("Encrypted C2:", C2)
print("Decrypted Message:", number_to_word(decrypted_message_list))
