import glob

books_path = glob.glob("data/books/*");

for book in books_path:
    with open(book, encoding="utf8") as f:
        print(book)
        contents = f.read()
        print("Cocaine : " + str(contents.count("cocaine")))
        print("Morphine : " + str(contents.count("morphine")))
        print("Heroin : " + str(contents.count("heroin")))
        print("Alcohol : "+ str(contents.count("alcohol")))
        print("Tobacco : " + str(contents.count("tobacco")))
        print("Opium : " + str(contents.count("opium")))
        print("-----------------------------")
        