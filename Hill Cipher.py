import string
import numpy as np

def encode():
    msg=input('\033[1;34;40menter msg :\033[0m\n>')
    key=input('\033[1;34;40menter key like 1 2 3 4:\033[0m\n>').split(" ")
    determinal = int(key[0])*int(key[3]) - int(key[1])*int(key[2])
    if len(key) != 4 :
        print("\033[1;31;40m The key should consist of 4 integers\033[0m \n")
    elif find_mod_inv(determinal,26) == None:
        print("\033[1;31;40m Invalid key\033[0m \n")
    else:
        key = np.reshape(key,(2,2))
        n = 2
        arr_msg = [msg[index : index + n].lower() for index in range(0, len(msg), n)]
        matrix = [(string.ascii_lowercase.index(arr_msg[i][j])) for i in range(len(arr_msg)) for j in range(len(arr_msg[i])) ]
        matrix = np.reshape(matrix,(len(arr_msg),2))

        for i in range(len(arr_msg)):
            for j in range(2):
                print(f"\033[1;32;40m{string.ascii_lowercase[(matrix[i][0]*int(key[j%len(key)][0]) + matrix[i][1]*int(key[j%len(key)][1]))%26]}\033[0m",end="")
        print()
def decode():
    Cipher=input('\033[1;34;40menter Cipher :\033[0m\n>')
    key=input('\033[1;34;40menter key like 1 2 3 4:\033[0m\n>').split(" ")
    if len(key) != 4 :
        print("\033[1;31;40m The key should consist of 4 integers\033[0m \n")
    else:        
        key = np.reshape(key,(2,2))
        determinal = int(key[0][0])*int(key[1][1]) - int(key[0][1])*int(key[1][0])
        if find_mod_inv(determinal,26) != None :
            inv = find_mod_inv(determinal,26)
            key_dec=[[],[]]

            key_dec[0].append(((int(key[1][1])%26)*inv)%26)
            key_dec[0].append(((-1*int(key[0][1])%26)*inv)%26)
            key_dec[1].append(((-1*int(key[1][0])%26)*inv)%26)
            key_dec[1].append(((int(key[0][0])%26)*inv)%26)

            key = np.reshape(key,(2,2))
            n = 2
            arr_Cipher = [Cipher[index : index + n].lower() for index in range(0, len(Cipher), n)]
            matrix = [(string.ascii_lowercase.index(arr_Cipher[i][j])) for i in range(len(arr_Cipher)) for j in range(len(arr_Cipher[i])) ]
            matrix = np.reshape(matrix,(len(arr_Cipher),2))

            for i in range(len(arr_Cipher)):
                for j in range(2):
                    print(f"\033[1;32;40m{string.ascii_lowercase[(matrix[i][0]*int(key_dec[j%len(key_dec)][0]) + matrix[i][1]*int(key_dec[j%len(key_dec)][1]))%26]}\033[0m",end="")
            print()
        else :
            print("\033[1;31;40m Invalid key\033[0m \n")
def find_mod_inv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x

if __name__ == '__main__':

    while True:
        print("\033[1;34;40mWelcome to Simple Hill Cipher Encryption / Decryption Choose what you want\n1) encode\n2)decode\33[0m")
        do = input(">")
        if do == '1' :
            encode()
            break
        elif do == '2':
            decode()
            break
        else :
            print("\033[1;31;40mPlease choose number 1 or 2\033[0m ")
