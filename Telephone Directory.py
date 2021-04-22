import pickle

def get_key(val,d1):
    for k, value in d1.items():
         if val == value or val in value:
             return k

ch = True
while ch is True:
    pickle_in = open("dict.pickle", "rb")
    dict1 = pickle.load(pickle_in)
    str1 = input("Command : ")
    t_lst = str1.split()
    if t_lst == []:
        print("Enter a valid command , The valid commands are :\nwhois , add , search , show , delete , update ,quit")
    else:
        if (t_lst[0] == 'whois' or t_lst[0] == 'WHOIS') and len(t_lst) == 2:
            if int(t_lst[1]) in dict1:
                print(dict1.get(int(t_lst[1])))
            else:
                print("Kindly check the entered number , Type 'show' to print the database s")

        elif t_lst[0] == 'quit' or t_lst[0] == 'QUIT':
            ch = False
            pickle_in.close()
        elif t_lst[0] == 'search' or t_lst[0] == 'SEARCH':
            if len(t_lst) == 2:
                temp = False
                for v in dict1.values():
                    if t_lst[1] in v or t_lst[1] == v:
                        for key,val in dict1.items():
                            if t_lst[1] == val or t_lst[1] == val[1] or t_lst[1] == val[0]:
                                if len(val) == 2:
                                    print(key, ':', val[0], val[1])
                                    temp = True
                                else:
                                    print(key, ':', dict1[key])
                                    temp = True
                if temp is False:
                    print("The entered name is not found in the database kindly recheck")
            else:
                print("Enter a valid input")
        elif t_lst[0] == 'add' or t_lst[0] == 'ADD':
            pickle_in.close()
            pickle_change = open("dict.pickle", "wb")
            if len(t_lst) > 3:
                k1 = int(t_lst[1])
                v1 = [t_lst[2], t_lst[3]]
                dict1[k1] = v1
                pickle.dump(dict1, pickle_change)
                pickle_change.close()
            else:
                k1 = int(t_lst[1])
                v1 = t_lst[2]
                dict1[k1] = v1
                pickle.dump(dict1, pickle_change)
                pickle_change.close()
        elif t_lst[0] == 'delete':
            if int(t_lst[1]) in dict1:
                pickle_in.close()
                pickle_change = open("dict.pickle", "wb")
                del dict1[int(t_lst[1])]
                pickle.dump(dict1, pickle_change)
                pickle_change.close()
            else:
                print("Enter a valid input")
        elif t_lst[0] == 'show':
            print(dict1)
        elif t_lst[0] == 'update' and (t_lst[2] == 'to' or t_lst[3] == 'to'):
            if len(t_lst) == 4 or len(t_lst) == 5:
                if t_lst[1].isnumeric():
                    pickle_in.close()
                    pickle_change = open("dict.pickle", "wb")
                    if len(t_lst) == 4:
                        dict1.update({int(t_lst[1]): t_lst[3]})
                    else:
                        dict1.update({int(t_lst[1]): [t_lst[3], t_lst[4]]})
                    pickle.dump(dict1, pickle_change)
                    pickle_change.close()
                elif t_lst[1].isalpha():
                    temp2 = False
                    for no,name in dict1.items():
                        if t_lst[1] in name or t_lst[1] == name:
                            temp2 = True
                            break
                    if temp2 is True:
                        pickle_in.close()
                        pickle_change = open("dict.pickle", "wb")
                        k_1 = get_key(t_lst[1],dict1)
                        if len(t_lst) > 4:
                            del dict1[k_1]
                            k1 = int(t_lst[4])
                            v1 = [t_lst[1], t_lst[2]]
                            dict1[k1] = v1
                            pickle.dump(dict1, pickle_change)
                            pickle_change.close()
                        else:
                            del dict1[k_1]
                            k1 = int(t_lst[3])
                            v1 = t_lst[1]
                            dict1[k1] = v1
                            pickle.dump(dict1, pickle_change)
                            pickle_change.close()
                    else:
                        print("Kindly recheck the entered values ")
                else:
                    print("Invalid Input")
        else:
            print("Enter a valid command , The valid commands are :\nwhois , add , search , show , delete , update ,quit")
    pickle_in.close()
