# Created by: Sarah Bicknell
# Date: 15th September 2015
# Info: Latin vocabulary practice program as practice

def openFiles():
        # edit this to allow selection of specific chapter lists maybe
        latinDict = {}
        dictFile = open("unit1vocab.txt")
        for line in dictFile:
            latin, eng = line.split(":")
            eng = eng[:-1]
            latinDict[latin] = eng
        return latinDict

def main():

        latinDict = openFiles()
        dictIndex = []
        for key in latinDict.keys():
            dictIndex.append(key)

        transInput = "q"
        i = 0
        print("Salve! Type in the correct translation of the Latin word!")
        
        while transInput != "EXIT":
            currentWord = dictIndex[i]
            print(currentWord)
            transInput = input("Enter the English translation (or EXIT to stop): ")
            print("You said: ", transInput)
            if transInput != "EXIT":
                if transInput in latinDict[currentWord]:
                    print("You are correct! The right answer was: ", latinDict[currentWord])
                    i = i + 1
                else:
                    print("Incorrect. The right answer was: ", latinDict[currentWord])
                    i = i + 1

main()
                                                                                                                                                                                                                                            
