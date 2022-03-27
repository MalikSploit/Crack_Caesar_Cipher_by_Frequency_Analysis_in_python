import matplotlib.pylab as plt #Install this library first, because it does not come pre-installed

#These are the letters we are interested in when dealing with frequency-analysis
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#The methode to do frequency analysis : we just count the occurrences of the given characters
def frequency_analysis(cipher_text):
    #The text we analyse
    cipher_text = cipher_text.upper()
    #We use a dictionary to store the letter-frquency pair
    letter_frequencies = {}

    #Initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS :
        letter_frequencies[letter] = 0

    #Let's consider the text we want to analyse
    for letter in cipher_text:
        #We keep incrementing the occurence of the given letter
        if letter in LETTERS:
            letter_frequencies[letter]+=1
    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


def caesar_crack(cipher_text):
    frequency= frequency_analysis(cipher_text)
    print(frequency)
    plot_distribution(frequency)
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse = True )
    print("\nHere is the frequency sorted : ")
    print(frequency)
    #To find the letter with the highest frequency
    print("\nThe possible key value is : %s" % (LETTERS.find(frequency[0][0]) - LETTERS.find('E')))

if __name__ == '__main__':
    #The key to cipher this message was : 3
    cipher_text = 'Wkh frqihuhqfh zloo eulqj wrjhwkhu hashuwv lq frpsxwhu vflhqfh, qdqrwhfkqrorjb dqg uhodwhg ilhogv'
    caesar_crack(cipher_text) #Information Leaking in this cryptosystem, because the most used letter in the english alphabet is E.
                              #So we know that the most used letter crypted corresponds to E, in our case it's H.
                              #Therefore we will immediatly know the key used for crypting, which is 3.
