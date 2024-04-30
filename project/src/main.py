from Interface import Interface

print(
  "Приветствую тебя, пользователь!"
  "Это приложение для шифровки и дешифровки твоего текста\n"
)
while True:
  Interface.operation()
  print(
    "\nВы хотите еще раз воспользоваться приложением?\n"
    "1. Да\n"
    "2. Нет"
  )
  answer = input()
  if (answer == "2" or answer.lower() == "нет"):
    print("До свидания! Ждем Вас снова!")
    break