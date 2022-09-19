# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# initText = "абвпыд длодлф жоыж шопжывь выжабв абв выпщоф"
# initList = initText.split()
# findText = "абв"

# resultList = list(filter(lambda x: findText not in x, initList))
# print(resultList)


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Чтобы победить первому игроку надо в первый ход взять столько конфет, чтобы осталось ближайшее число,
# делящееся нацело на 29. Каждый следующий ход нужно делать чтобы за итерацию убывало 29 конфет.
# Если второй игрок берет 14 (1, 28) конфет, то нужно брать 29-14 (1, 28) = 15 (28, 1) конфет.
# В конце останется 29, и первый игрок победит в любом случае


# from random import randint

# countCandyes = 105
# maxTake = 28

# # 2 игрока:
# whoTurns = False

# while countCandyes > 0:
#     currentTake = int(input(f"Player {int(whoTurns)+1} turn: "))
#     if (0 < currentTake < 29) and (currentTake <= countCandyes):
#         countCandyes -= currentTake
#         print(f"{countCandyes} candyes left")
#         if countCandyes == 0:
#             print(f"Player {int(whoTurns)+1} wins")
#         whoTurns = not whoTurns
#     else:
#         print("Incorrect count, try again")


# # игрок против бота:

# while countCandyes > 0:
#     currentTake = int(input("Insert count of candyes you take: "))
#     if (0 < currentTake < 29) and (currentTake <= countCandyes):
#         countCandyes -= currentTake
#         print(f"{countCandyes} candyes left")
#         if countCandyes == 0:
#             print("You win!")
#             break
#         if countCandyes <= maxTake:
#             currentTake = randint(1, countCandyes)
#         else:
#             currentTake = randint(1, maxTake)
#         countCandyes -= currentTake
#         print(f"Bot take {currentTake} candyes")
#         print(f"{countCandyes} candyes left")
#         if countCandyes == 0:
#             print("Bot win!")
#     else:
#         print("Incorrect count, try again")


# # Бот ходит первым и выигрывает:

# print(f"{countCandyes} candyes left")
# while countCandyes > 0:
#     currentTake = countCandyes % (maxTake+1)
#     countCandyes -= currentTake
#     print(f"Bot take {currentTake} candyes")
#     print(f"{countCandyes} candyes left")
#     if countCandyes == 0:
#         print("Bot win!")
#         break
#     currentTake = int(input("Insert count of candyes you take: "))
#     if (0 < currentTake < 29) and (currentTake <= countCandyes):
#         countCandyes -= currentTake
#         print(f"{countCandyes} candyes left")
#         if countCandyes == 0:
#             print("You win!")
#     else:
#         print("Incorrect count, try again")


# Создайте программу для игры в ""Крестики-нолики"".

# import tkinter as tk

# window = tk.Tk()
# label1 = tk.Label(window, text=f"Turn of X", font="times 15")
# label1.grid(row=0, column=1)
# # Конечная надпись, вначале не видна:
# resultLabel = tk.Label(window, font=("Arial", 15, "bold"))
# resultLabel.grid(row=0, column=2)
# imageO = tk.PhotoImage(file="O.png").subsample(2, 2)
# imageX = tk.PhotoImage(file="X.png").subsample(2, 2)
# imageNoTurn = tk.PhotoImage(file="NoTurn.png").subsample(2, 2)
# dictImages = {
#     "X": imageX,
#     "O": imageO,
# }
# # Чей ход:
# whoTurns = "X"
# countTurns = 0
# # Варианты, чей может быть ход:
# strWhoTurns = "XO"
# # Словарь, в который будут записываться ходы:
# dictTurns = {
#     "X": [],
#     "O": []
# }
# # Список вариантов победы:
# winCorteges = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


# # Что происходит при нажатии кнопки х:
# def PlayerClick(x):
#     global buttons, countTurns, whoTurns
#     buttons[x].config(image=dictImages[whoTurns], state="disabled")
#     dictTurns[whoTurns].append(x)
#     for i in range(len(winCorteges)):
#         countOfIn = 0
#         for j in range(3):
#             if winCorteges[i][j] in dictTurns[whoTurns]:
#                 countOfIn += 1
#         if countOfIn == 3:
#             StopGame(buttons, resultLabel, whoTurns)
#     countTurns += 1
#     whoTurns = strWhoTurns[countTurns % 2]
#     label1.config(text=f"Turn of {whoTurns}")
#     if countTurns == 9:
#         resultLabel.config(text="DEAD HEAT")

# # Функция, на случай победы. все кнопки блокируются, выводится победитель


# def StopGame(buttons, label, whoWin):
#     for i in range(len(buttons)):
#         buttons[i].config(state="disabled")
#     label.config(text=f"{whoWin} WINS")


# # Создаем список кнопок:
# buttons = []

# for i in range(9):
#     buttons.append(tk.Button(window, width=150, height=150, image=imageNoTurn,
#                    command=lambda i=i: PlayerClick(i)))

# # и располагаем его на поле:
# tempIndex = 0
# for i in range(3):
#     for j in range(3):
#         buttons[tempIndex].grid(row=i+1, column=j+1)
#         tempIndex += 1

# window.mainloop()


# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# initData = "aaaaaaabcccddefggggg"


# def Encode(data):
#     data += " "
#     count = 1
#     encodeStr = ""
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]:
#             count += 1
#         else:
#             encodeStr += str(count) + data[i]
#             count = 1
#     return encodeStr


# def Decode(string):
#     data = ""
#     count = ""
#     for i in string:
#         if i.isdigit():
#             count += i
#         else:
#             data += i*int(count)
#             count = ""
#     return data


# print(Encode(initData))
# print(Decode(Encode(initData)))
