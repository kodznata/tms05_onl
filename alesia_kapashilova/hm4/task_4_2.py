# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus.
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

name = ['Ivan', 'Ivanou']
str1 = 'Minsk'
str2 = 'Belarus'
new_name = ' '.join(name)
print(f'Привет, {new_name}! Добро пожаловать в {str1} {str2}')
