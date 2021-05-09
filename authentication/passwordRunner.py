#!/usr/bin/env python3
import hashlib
import binascii
from itertools import permutations 

def hashString(password):
    # Compute the MD5 hash of this example password
    #password = 'moose' # type=string
    #print('password ({0}): {1}'.format(type(password), password))

    encodedPassword = password.encode('utf-8') # type=bytes
    #print('encodedPassword ({0}): {1}'.format(type(encodedPassword), encodedPassword))

    md5 = hashlib.md5(encodedPassword)
    passwordHash = md5.digest() # type=bytes
    #print('passwordHash ({0}): {1}'.format(type(passwordHash), passwordHash))

    passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes
    #print('passwordHashAsHex ({0}): {1}'.format(type(passwordHashAsHex), passwordHashAsHex))
    
    passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
    #print('passwordHashAsHexString ({0}): {1}'.format(type(passwordHashAsHexString), passwordHashAsHexString))
    return passwordHashAsHexString

def produce_dic(filename):
    return_dic = {}
    words = [line.strip() for line in open("passwords.txt")]
    for word in words:
        
        return_dic[word.split(':')[1]] = word.split(':')[0]

    
    '''perm = permutations(words, 2)
    print("every one word is in the dictionary")
    

    for i in list(perm):
        temp_word = i[0] + i[1]
        return_dic[hashString(temp_word)] = temp_word
    '''
    return return_dic

def crack_passwords_one(dic):
    print("starting")
    words = [line.strip().lower() for line in open("words.txt")]
    temp_words = words
    f = open("test.txt", "w")
    i = 0
    j = 0
    for z in range(len(words)):
        
        j = j + 1
        if hashString(words[z]) in dic:
            i = i + 1
            f.write(dic[hashString(words[z])] + ":" + words[z] + "\n")

        
        for temp_word in words[z + 1:]:
            j = j + 2
            #print(words[z] + temp_word)
            
            if hashString(words[z] + temp_word) in dic: 
                i = i + 1
                f.write(dic[hashString(words[z] + temp_word)] + ":" + words[z] + temp_word + "\n")
            if hashString(temp_word + words[z]) in dic:
                i = i + 1
                f.write(dic[hashString(temp_word + words[z])] + ":" + temp_word + words[z] + "\n")
        if z == len(words)//2:
            print("halfway")
        if z == len(words)//4:
            print("quarter")
        if z == len(words)//8:
            print("eighth")    
    '''perm = permutations(words, 2)
    
    

    for element in list(perm):
        j = j + 1
        temp_word = element[0] + element[1]
        if hashString(temp_word) in dic:
            i = i + 1
            print(i)
            f.write(dic[hashString(temp_word)] + ":" + temp_word + "\n")
        
        #print(hashed_password)'''
        
    f.write("Number of passwords cracked: " + str(i) + "\n")
    f.write("Number of hashes: " + str(j) + "\n")
    f.close()

def produce_dic_salted():
    return_dic = {}
    words = [line.strip().lower() for line in open("words.txt")]
    salts = [line.strip().lower() for line in open("salted_passwords.txt")]
    for word in words:
        #print(hashString(word))
        return_dic[hashString(word)] = word

    
    perm = permutations(words, 2)
    print("every one word is in the dictionary")
    

    for i in list(perm):
        temp_word = i[0] + i[1]
        for line in salts:
            salt = line.split(":")[1].split("$")[0]

            return_dic[hashString(salt + temp_word)] = salt + temp_word
    
    return return_dic, len(return_dic)

def crack_passwords_two(dic,filename, number_of_hashes):
    words = [line.strip().lower() for line in open(filename)]
    f = open("passwords2.txt", "w")
    i = 0
    for word in words:
        
        username = word.split(':')[0]
        hashed_password = word.split(':')[1].split["$"][1]
        #print(hashed_password)
        if hashed_password in dic:
            i = i + 1
            f.write(username + ":" + dic[hashed_password] + "\n")
    f.write("Number of passwords cracked: " + str(i) + "\n")
    f.write("Number of hashes: " + str(number_of_hashes) + "\n")
    f.close()

    

def main():
    print(len([line.strip().lower() for line in open("passwords.txt")]))
    #dic = produce_dic("words.txt")
    #crack_passwords_one(dic)
    #dic2, number_of_hashes2 = produce_dic_salted("words.txt")
    #crack_passwords_two(dic2,"salted_passwords.txt", number_of_hashes2)

main()
#print(hashString("e75fa822moose"))
#astr = "er:sdasda$32323:33"



