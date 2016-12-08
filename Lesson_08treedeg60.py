word = input("enter a word")
stop = len(word)

def tree(word,start,stop):
    if start <= stop:
        print("{:>10s}".format(word[0 : start ]))
        return tree(word, start + 1 ,stop)

tree(word, 0, stop)
        
