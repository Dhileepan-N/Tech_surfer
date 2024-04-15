class title_verification:
    def __init__(self, acnt_title, cheque_title):
        self.acnt_title = acnt_title
        self.cheque_title = cheque_title

    def verify_title(self,acnt_title, cheque_title):
        dicitinory = {1: {'5': 'S'}, 2: {'S': '5'}, 3: {'0': 'O'}, 4: {'O': '0'}, 5: {'2': 'Z'}, 6: {'Z': '2'},
                      7: {'B': '8'}, 8: {'8': 'B'}, 9: {'1': 'I'}, 10: {'I': '1'}, 11: {'1': 'i'}, 12: {'i': '1'},
                      13: {'l': '1'}, 14: {'1': 'l'}, 15: {'1': 'L'}, 16: {'8': 'R'}, 17: {'R': '8'}, 18: {'Z': '7'},
                      19: {'7': 'Z'}, 20: {'I': 'l'}, 21: {'l': 'I'}, 22: {'O': 'Q'}, 23: {'Q': 'O'}, 24: {'L': 'I'},
                      25: {'I': 'L'}, 26: {'Q': 'G'}, 27: {'Q': 'g'}, 28: {'e': 'a'}, 30: {'a': 'e'}, 31: {'D': 'O'}}
        if (acnt_title.__eq__(cheque_title)):
            print("Matching. Proceed to Next")
            return cheque_title
        else:
            acnt_title_list = list(acnt_title)
            cheque_title_list = list(cheque_title)
            print(acnt_title_list)
            print(cheque_title_list)
            for i in range(len(cheque_title_list)):
                if cheque_title_list[i].casefold() != acnt_title[i].casefold():
                    for key , value in dicitinory.items():
                        if acnt_title[i] == value.get(cheque_title_list[i]):
                            cheque_title_list[i] = value.get(cheque_title_list[i])
            cheque_title = ''.join(cheque_title_list)
            return cheque_title
if __name__ == '__main__':
    # acnt_title = "patterns"
    # cheque_title ="pattars"
    acnt_title = input("Enter the account title : ")
    cheque_title = input("Enter the cheque title : ")
    title_verification_object = title_verification(str(acnt_title), str(cheque_title))
    final_check_title = title_verification_object.verify_title(acnt_title, cheque_title)
    print(final_check_title)
