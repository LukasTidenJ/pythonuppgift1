#comments in english for easier understanding for you bro
import sys

def clean_text(text):
    # empty string
    ren_text = ""

    # for loop to check each symbol in a word
    for tecken in text:

        # check if symbol is in alphabet
        if tecken.isalpha():
            # remove eventual capitalization and add to the empty array ren_text
            ren_text = ren_text + tecken.lower()

            # check if symbol is a space
        elif tecken.isspace():
            # add the space to the array so it looks better
            ren_text = ren_text + tecken

            # we dont need isdigit() since this for loop only saves it in the array if the symbol is a letter or a space

    # split it to put each word in an array so we can check if the word is positive or negative or nothing
    return ren_text.split()


def load_dictionary(filename):
    #create the dictionary here with an empty array
    sentiment_weights = {}

    # 'r' means read so we read the file
    fil = open(filename, 'r')

    # save every row in a list and read the file
    alla_rader = fil.readlines()
    #go through the list one row at a time
    for rad in alla_rader:
        # make a new line
        rad = rad.replace('\n', '')

        # split at the comma sign
        delar = rad.split(',')

        # here we make sure we get both the word and the point
        if len(delar) == 2:
            ordet = delar[0]
            poang = delar[1]

            # skip the first row
            if ordet == "word":
                continue
            else:
                # make the point to int and save in dictionary
                sentiment_weights[ordet] = int(poang)
    #close the file
    fil.close()

    return sentiment_weights


def calculate_score(text, sentiment_weights):
    # use the clean_text function
    ordlista = clean_text(text)

    # made a variable to save the points
    poang = 0

    # go through one word at a time
    for ordet in ordlista:

        # if word is in our dictionary we plus the point to the total
        if ordet in sentiment_weights:
            poang = poang + sentiment_weights[ordet]

    # send the text and point back
    return text, poang


def analyze_sentiment(document, sentiment_weights):
    # make an empty array where we collect the results
    resultat_lista = []

    # go through the document one row at a time
    for rad in document:

        # use the function calculate_score to - surprise!!! - calculate the score
        text_och_poang = calculate_score(rad, sentiment_weights)

        # make the points and text separately
        texten = text_och_poang[0]
        poangen = text_och_poang[1]

        # use if here to make points over 0 positive and below 0 negative
        if poangen > 0:
            kansla = "Positive"
        elif poangen < 0:
            kansla = "Negative"
        else:
            kansla = "Neutral"

        fardig_trio = (texten, poangen, kansla)

        # append to our list of results
        resultat_lista.append(fardig_trio)

    # send it baackkkk after the entire list has gone through our little processing
    return resultat_lista


def print_report(results, n=None):
    # print out
    # make it look nice with ljust and rjust
    print("Post Content".ljust(60) + "| " + "Score".rjust(5) + " | Sentiment")

    # make it look nice here too
    print("-" * 80)

    if n == None:
        n = len(results)

    # range in loop here to just loop n amount of times
    for i in range(n):
        # safety check because im paranoid
        if i < len(results):
            # text, points and feelings
            trio = results[i]
            texten = trio[0]
            poangen = trio[1]
            kanslan = trio[2]

            # ljust and rjust only works on text so we make the points a string
            poang_text = str(poangen)

            # print
            print(texten.ljust(60) + "| " + poang_text.rjust(5) + " | " + kanslan)


#
if len(sys.argv) < 3:
    print("Not supported")
else:
    ord_fil = sys.argv[1]
    text_fil = sys.argv[2]

    # load the words.csv
    sentiment_weights = load_dictionary(ord_fil)

    # read the reviews.txt
    dokument = []
    recensioner_fil = open(text_fil, 'r')
    rader = recensioner_fil.readlines()

    for rad in rader:
        ren_rad = rad.strip()
        if ren_rad != "":
            dokument.append(ren_rad)
    recensioner_fil.close()

    # analyze the document with this little function here
    alla_resultat = analyze_sentiment(dokument, sentiment_weights)


    if len(sys.argv) == 4:
        kommando = sys.argv[3]

        if kommando == "POS":
            # here for positive pick it out
            pos_lista = []
            for res in alla_resultat:
                if res[2] == "Positive":
                    pos_lista.append(res)
            print_report(pos_lista)

        elif kommando == "NEG":
            # pick out the negative
            neg_lista = []
            for res in alla_resultat:
                if res[2] == "Negative":
                    neg_lista.append(res)
            print_report(neg_lista)

        elif kommando == "NEUT":
            # pick out the neutral
            neut_lista = []
            for res in alla_resultat:
                if res[2] == "Neutral":
                    neut_lista.append(res)
            print_report(neut_lista)

        elif kommando.isdigit():
            # if you want to print like the first 10 or something we can use this
            antal = int(kommando)
            print_report(alla_resultat, antal)

        else:
            print("Not supported")

    elif len(sys.argv) == 3:
        # if number is not specified print out the entire thing
        print_report(alla_resultat)

    else:
        print("Not supported")