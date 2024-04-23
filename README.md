# yakushin-mg-python1-mipt

Версия Python3 3.11.1 и выше

Шифрование

Описание:
Этот проект реализует простое консольное приложение на Python для шифрования и дешифрования текстовых файлов с помощью:
1) шифра Цезаря
2) шифра Виженера
3) шифра Вернама
Также есть функция автоматический взлома шифра Цезаря методами частотного анализа.
(Если хватит времени, хотелось бы реализовать другие варианты шифрования файлов, например, матричный)

Описание работы приложенияи
Изменил работу приложения чтобы оно стало больше user-friendly
Запуск происходит с помощью командной строки
   python3 main.py
Затем у пользователя запрашивается режим работы, тип шифрования (если это не взлом), адрес первого файла, адрес второго файла. После каждого ввода проверяется верность введеных данных, иначе приложение попросит заново ввести тот пункт, который оказался неверным.

Архитектура
Используемый библиотеки:
   1. Стандартная
   2. pathlib

Класс Interface для работы приложения, в нем 4 статических метода:
   1. Приватный __choose_mode__ для выбора режима работы (шифрование, дешифрование, взлом).
   2. Приватный __choose_type__(mode) для выбора типа шифра (для взлома всегда шифр Цезаря).
   3. Приватный __get_address__ для получения адреса файла и проверки того, что это файл.
   4. Публичный operation для работы приложения: в нем вызываются три предыдущих метода и исходя из них выбирается нужый метод шифрования,               дешифрования или взлом. Для шифрования и дешифрования также считывается параметр (для шифра Цезаря) или ключ (для шифров Вернама или               Виженера). Как раз этот метод вызывается в заглавном файле main.py.

Cделаем три класса по типу шифрования:
1) Caesar's_cipher
   В нем будет три статических метода: шифрование, дешифрование и автоматический взлом
   1. Шифрование (исходный текст, параметр сдвига)
      Шифр Цезаря сдвигает буквы на указанное количество позиций, поэтому в параметрах функции будет исходный текст и параметр сдвига (число):
      У каждого элемента узнаем его код в Unicode формате с помощью ord(), затем к нему прибавляем параметр сдвига, и с помощью char() получаем          новый символ.
   2. Дешифрование (зашифрованный текст, параметр сдвига)
      При дешифровании выполняется точно такой же алгоритм, что и при шифровании, но параметр сдвига умножается на -1.
   3. Автоматический взлома шифра Цезаря методами частотного анализа (зашифрованный текст)
      Добавляем таблицу частот появления символов в зашифрованном тексте. Сортируем ее по убыванию. Так как самым частым символом является 'e', тo       считаем разность между ord(элемент, который встречается чаще всего в зашифрованном тексте) и ord('e'). Это и есть параметр сдвига. Затем       вызываем дешифрование(зашифрованный текст, параметр сдвига).


2) Vigenеre_cipher
   В нем будет три статических метода: __text_change__, шифрование и дешифрование
   1. __text_change(исходный текст, ключ-слово, тип операции)
      Шифр Виженера - использует ключевое слово для повторения ключа и шифрует текст по ключу, поэтому в параметрах функции будет исходный текст и       ключ. У каждого элемента ключа узнаем его код в Unicode формате с помощью ord(), сохраняя это в массиве unicode_key. Затем циклом проходимся       по каждому элементу изначальной строки и в зависимости от типа операции(шифрование или дешифрование) к коду символа прибавляем или вычитаем        unicode_key[i % len(unicode_key)] (это почти шифр Цезаря, только несколько параметров). Этот метод сделан для избежания копипасты.
   2. Шифрование (исходный текст, ключ-слово)
      При шифровании прибавляется unicode_key[i % len(unicode_key)].
   3. Дешифрование (зашифрованнай текст, ключ-слово)
      При дешифровании вычитается unicode_key[i % len(unicode_key)].

3) Vernam_cipher
   В нем будет два статических метода: шифрование и дешифрование
   1. Шифрование (исходный текст, ключ)
      Шифр Вернама - одноразовый блокнот, где каждая буква текста XOR'ится с соответствующей буквой ключа, поэтому в параметрах функции будет            исходный текст и ключ. Ключ должен быть не меньше, чем длина самого сообщения. Каждый элемент сообщения и ключа переводим в Unicode-формат,        а затем переводим полученные числа в двоичную записи с помощью bin(). Проводим XOR этих двух чисел, затем переводим число в десятичную             запись с помощью int("...", 2), после этого получаем новый элемент с помощью char().
   2. Дешифрование (зашифрованный текст, ключ)
      Вызывается шифрование (исходный текст, ключ), так как xor((a,b), b) = a.
