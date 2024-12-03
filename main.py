from random import choice

print('Добро пожаловать в генератор паролей')
print()

# Выбор параметров пользователем
def user_data():
    number_of_passwords = int(input('Введите необходимое количество паролей: '))
    len_of_passwords = int(input('Введите желаемую длину паролей: '))
    availability_of_numbers = input('Наличие цифр в пароле, ДА/НЕТ: ').lower()
    lowercase_letters_present = input('Наличие строчных букв, ДА/НЕТ: ').lower()
    capital_letters_available = input('Наличие прописных букв, ДА/НЕТ: ').lower()
    presence_of_special_characters = input('Наличие спец символов, ДА/НЕТ: ').lower()
    presence_of_ambiguous_characters = input('Исключить неоднозначные символы, ДА/НЕТ: ').lower()

    chars = ''
    if availability_of_numbers == 'да':
        chars += '0123456789'
    if lowercase_letters_present == 'да':
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if capital_letters_available == 'да':
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if presence_of_special_characters == 'да':
        chars += '!#$%&*+-=?@^_.'

    if presence_of_ambiguous_characters == 'да':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')

    return number_of_passwords, len_of_passwords, chars

# Генерация пароля с выбранными параметрами
def generate_password(number_of_passwords, len_of_passwords, chars):
    for i in range(number_of_passwords):
        password = ''.join(choice(chars) for _ in range(len_of_passwords))
        print(f'{i + 1}: {password}')

# Основной код
number_of_passwords, len_of_passwords, chars = user_data()
if chars:  # Проверяем, что набор символов не пуст
    generate_password(number_of_passwords, len_of_passwords, chars)
else:
    print('Набор символов пуст. Пожалуйста, повторите попытку с другими параметрами.')