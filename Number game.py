# This Python file uses the following  encoding: utf-8
# Number chalenge
# players get 3 answers
# ugotoviti nakljucno stevilko
# mora biti st od 0 do 14
# poves ali je stevilka premajhna ali prevelika
# in povej koliko krat se lahko ugibajo
# This Python file uses the following encoding: utf-8


import random

random_number = random.randint(1, 14)
poskusi = 0
poskusi_ostane = 3

while poskusi < 3:
    guess = raw_input("Ugotovi naključno številko od 1 do 14. ")
    poskusi += 1
    poskusi_ostane -= 1

    guess_num = int(guess)

    if guess_num == random_number:
        print ("Čestitke! pravilno")
        print ("Porabili ste {} poskusov.".format(poskusi))
        poskusi = 3
    elif guess_num < random_number:
        if poskusi_ostane > 0:
            print("Oprosti ta številka je premajhna. Na razpolago še imaš {} poskusov.".format(int(poskusi_ostane)))
        else:
            print("Oprosti moja številka je bila {}".format(int(random_number)))
            print("Zmanjkalo ti je poskusov. Več sreče prihodnjič")
    else:
        if poskusi_ostane > 0:
            print("Oprosti ta številka je previsoka. Na razpolago še imaš {} poskusov.".format(int(poskusi_ostane)))
        else:
            print("Oprosti moja številka je bila {}".format(int(random_number)))
            print ("Zmanjkalo ti je poskusov. Več sreče prihodnjič")
