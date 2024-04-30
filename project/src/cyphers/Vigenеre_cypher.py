class Vigenеre_cypher:
  @staticmethod
  def __textchange__(text, key, type):
    array_key = []
    for element in key:
      array_key.append(ord(element))
    final_text = ""
    for i in range(len(text)):
      # final_symbol = chr(32 + (ord(text[i]) + array_key[i % len(key)] * ((-1) ** type)) % (126 - 31))
      final_symbol = chr((ord(text[i]) + array_key[i % len(key)] * ((-1) ** type)))
      final_text += final_symbol
    return final_text

  @staticmethod
  def encryption(text, key):
    return Vigenеre_cypher.__textchange__(text, key, 2)
  
  @staticmethod
  def decryption(text, key):
    return Vigenеre_cypher.__textchange__(text, key, 1)

with open("/Users/mihailakusin/Desktop/PractPython/shifr/1.txt") as f:
  with open ("/Users/mihailakusin/Desktop/PractPython/shifr/2.txt", "w") as g:
    g.write(Vigenеre_cypher.encryption(f.read(), "111"))

with open("/Users/mihailakusin/Desktop/PractPython/shifr/2.txt") as f:
  with open ("/Users/mihailakusin/Desktop/PractPython/shifr/3.txt", "w") as g:
    g.write(Vigenеre_cypher.decryption(f.read(), "111"))