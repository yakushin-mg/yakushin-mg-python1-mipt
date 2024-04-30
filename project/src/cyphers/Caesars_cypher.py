class Caesars_cypher:
  @staticmethod
  def encryption(text, parametr):
    final_text = ""
    for element in text:
      final_text += chr(ord(element) + parametr)
    return final_text
  
  @staticmethod
  def decryption(text, parametr):
    return Caesars_cypher.encryption(text, parametr * (-1))

  @staticmethod
  def hack(text):
    frequency = {}
    text = text.lower()
    for element in text:
      if (not element in frequency):
        frequency[element] = 0
      frequency[element] += 1
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return Caesars_cypher.decryption(text, ord(sorted_frequency[0][0]) - ord('e'))