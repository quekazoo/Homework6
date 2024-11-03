import string
def letters_between(input_str):
    start, end = input_str.split('-')
    start_index = string.ascii_letters.index(start)
    end_index = string.ascii_letters.index(end)
    return string.ascii_letters[start_index:end_index + 1]

user_input = input("Введіть дві літери через дефіс (наприклад, a-z): ")
result = letters_between(user_input)
print(result)