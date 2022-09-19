# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# initText = "абвпыд длодлф жоыж шопжывь выжабв абв выпщоф"
# initList = initText.split()
# findText = "абв"

# resultList = list(filter(lambda x: findText not in x, initList))
# print(resultList)


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
