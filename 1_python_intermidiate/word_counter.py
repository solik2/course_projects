
def execute(file_path, n):
    file = open(file_path, 'r').read()
    delimiters = [",", "|", ";", "!", ".", "?","/"]
    for delimiter in delimiters:
        file = " ".join(file.split(delimiter))
    words = file.split()

    dictionary = {}
    for word in set(words):
        dictionary[word] = words.count(word)
    
    dictionary = dict(sorted(dictionary.items(),key=lambda x:x[1], reverse=True))
    for i in range(n):
        print(str(list(dictionary.keys())[i]) + " is repeteded this times => " + str(list(dictionary.values())[i]))
        



def main():
    execute("python_intermidiate/data.txt", 5) 

if __name__ == "__main__":
    main()