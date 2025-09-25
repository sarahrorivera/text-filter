#define a function for filtered text
def filter_text(text):
    #make a list of banned words
    banned_list = ["Turkey","Dog","Fox","Cat","Chicken","turkey","dog","fox"""
                   "cat", "chicken"]
    #s p l i t 
    words = text.split()
    res = []
    #create the loop- decide parameters
    for word in text.split():
        if word in banned_list:
            continue
        else:
            res.append(word)
    #string + returns
    res = " ".join(res)
    return res
# main function
if __name__=="__main__":
    #get the sentence from user
    s = input('>: ')
    # print print print :D
    print('Input Message:',s)
    print('Output Message:',filter_text(s))