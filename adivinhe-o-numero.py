import random



cont = 5
adm = True
numero =int(random.randint(0,100))
while adm == True:

    resp_user = int(input("Digite o seu numero de 0 a 100: "))
    if resp_user > numero:
        cont = cont - 1
        print("O seu numero e maior, tente de novo")
        print("Voce  tem {} tentativas".format(cont))
        if cont == 0:
            print ("Suas chances acabaram. :(")
            adm = False

    elif resp_user < numero:
        cont = cont - 1
        print("O seu numero e menor, tente de novo")
        print("Voce tem {} tentativas".format(cont))
        if cont == 0:
            print ("Suas chances acabaram. :(")
            adm = False
    elif resp_user == numero:
            print("Parabens! Voce acertou! :D")
        
            adm = False
            