import re
text = r'dfefe stank1in@mail.ru sadw eqrfgs dagfe efe mgtustankin@gmail.com.com atvgrs stanok@mail.ru adsada a stakan@yandex.ru d 312323@312 425235 asfw4 '
finder = re.compile(r"\w+@\w+\.\w{2,6}\b", re.IGNORECASE)
print(re.findall(finder, text))
