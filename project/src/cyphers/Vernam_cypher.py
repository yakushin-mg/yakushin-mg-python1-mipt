class Vernam_cypher:
  @staticmethod
  def encryption(text, key):
    final_text = ""
    for i in range(len(text)):
      final_symbol = ord(text[i])
      final_symbol ^= ord(key[i])
      final_text += chr(final_symbol)
    return final_text

  def decryption(text, key):
    return Vernam_cypher.encryption(text, key)