    #recieves the word and separates it into a list
def recebePlv():
    word = input("Please type a word: ")
    char_list = []
    for i in range(len(word)):
        char_list.append(word[i])
    return char_list


    #Reverses the word
def wrev(palavra):

    rev_word =[]
    for i in range(len(palavra)):
        rev_word.append(palavra[-1-i])
    return ''.join(rev_word)


    #Checks if the word is a palindrome
def check_palindrome(palavra, revpalavra):
    palindrome = False
    word = ''.join(palavra);
    revword = ''.join(revpalavra)

    if word.lower() == revword.lower():
        palindrome = True
        print("It's a Palindrome")
    else:
        print('Not a Palindrome')
    return palindrome


if __name__=='__main__':
    palavra = recebePlv()

    rev_pal = wrev(palavra)

    check_palindrome(palavra, rev_pal)
