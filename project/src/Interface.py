from pathlib import Path
from cyphers.Caesars_cypher import Caesars_cypher
from cyphers.Vernam_cypher import Vernam_cypher
from cyphers.Vigenеre_cypher import Vigenеre_cypher

class Interface:
  @staticmethod
  def __choose_mode__():
    print(
      "Выбери режим работы приложения (введите цифру или название режима):\n"
      "1. Шифрование\n"
      "2. Дешифрование\n"
      "3. Взлом (пока доступно только для шифра Цезаря)"
    )
    while (True):
      mode = input()
      if (mode == "1" or mode.lower() == "шифрование"):
        return "encryption"
      elif (mode == "2" or mode.lower() == "дешифрование"):
        return "decryption"
      elif (mode == "3" or mode.lower() == "взлом"):
        return "hack"
      else:
        print("Скорее всего Вы ошиблись при выборе режима, еще раз введите цифру или название режима")

  @staticmethod
  def __choose_type__(mode):
    if (mode == "hack"):
      return "caesar"
    print(
      "Выбери тип шифра (введите цифру или название шифра):\n"
      "1. Шифр Цезаря\n"
      "2. Шифр Вернама\n"
      "3. Шифр Виженера"
    )
    while (True):
      type = input()
      if (type == "1" or type.lower() == "шифр цезаря"):
        return "caesar"
      elif (type == "2" or type.lower() ==  "шифр вернама"):
        return "vernam"
      elif (type == "3" or type.lower() ==  "шифр виженера"):
        return "vigenere"
      else:
        print("Скорее всего Вы ошиблись при выборе шифра, введите цифру или название шифра")

  @staticmethod
  def __get_address__(number_of_file):
    print(
      f"Введите адрес файла №{number_of_file}"
    )
    while (True):
      path = Path(input())
      if (not path.exists()):
        print("Такого файла не существует, введите адрес файла")
      elif (not path.is_file()):
        print("Это не файл, введите адрес файла")
      else:
        return path

  @staticmethod
  def operation():
    mode = Interface.__choose_mode__()
    type = Interface.__choose_type__(mode)
    first_file_address = Interface.__get_address__(1)
    second_file_address =  Interface.__get_address__(2)
    with open(first_file_address, 'r') as first_file:
      with open(second_file_address, 'w') as second_file:
        if (mode == "hack"):
          print("Если текст не очень большой, то возможны ошибки")
          second_file.write(Caesars_cypher.hack(first_file.read()))
        else:
          if (type == "caesar"):
            print("Введите число, не равное нулю - параметр сдвига")
            while True:
              parametr = int(input())
              if (parametr != 0):
                break
              print("Введите число, не равное нулю")
            if (mode == "encryption"):
              second_file.write(Caesars_cypher.encryption(first_file.read(), parametr))
            else:
              second_file.write(Caesars_cypher.decryption(first_file.read(), parametr))

          elif (type == "vernam"):
            print("Введите ключ (строку), длина которого не меньше длины исходного текста")
            original_text = first_file.read()
            while True:
              key = input()
              if (len(key) >= len(original_text)):
                break
              print("Введите ключ, длина которого не меньше длины исходного текста")
            if (mode == "encryption"):
              second_file.write(Vernam_cypher.encryption(original_text, key))
            else:
              second_file.write(Vernam_cypher.decryption(original_text, key))

          else:
            print("Введите ключ (строку)")
            while True:
              key = input()
              if (len(key) != 0):
                break
              print("Введите ключ, состоящий хотя бы из одного элемента")
            print(key)
            if (mode == "encryption"):
              second_file.write(Vigenеre_cypher.encryption(first_file.read(), key))
            else:
              second_file.write(Vigenеre_cypher.decryption(first_file.read(), key))
    print("Результат ждет Вас во втором файле")
            