def read_text():
    quotes = open(r"C:\Users\user\coding\python\text.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close

read_text()