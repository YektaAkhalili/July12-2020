def count_words(file):
    try:
        with open(file) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
            print("Sorry, the file " + file + " does not exist.")        
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file + " has about " + str(num_words) + 
        " words.")        

filename = 'lorel.txt' #120 words
count_words(filename)