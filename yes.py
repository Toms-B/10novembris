def lasit_datni():
    # Pajautājam ievadīt datnes nosaukumu
    datnes_nosaukums=input("Ievadīt datnes nosaukumu: ")
    try:                                                                                                                                                                                       

    # Kā ielādēt datnes saturu?
        with open(datnes_nosaukums, 'r') as ff:
            saturs=ff.read()
            # print(saturs) pārliecinājos par to, ka datnē ir skaitļi
            # izvadi simbolu skaitu datnē 
            print(f"Simbolu skaits datnē ir {len(saturs)}")
            
            # izvadi pirmos 10 simbolus
            print(f"Pirmie ir:{saturs[:10]}")

            #izvadi pirmo un pēdējo simbolu
            print(f"Izvadīt pirmo un pēdējo simbolu: {saturs[0]} un {saturs[-3]}")
    except FileNotFoundError:
         print("Datne nav atrasta!")
    except ValueError:
         print("Datu kļūda")

if __name__=="__main__":
    lasit_datni()