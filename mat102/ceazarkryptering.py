import unicodedata
from collections import Counter
def main():
    alfabet = [26]
    frekvenstab = [26]
    k = 0
    streng = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the  when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.".lower()

    for i in range(97, 123):
        alfabet.append(i)

    kryptert = ""
    NOKKEL = 1
    for k in range(len(streng)):
        if " " == streng[k]:
            kryptert += " "
        elif "." == streng[k]:
            kryptert += "."
        else:
            kryptert += chr(ord(streng[k]) + NOKKEL)

    print(streng)
    print(kryptert)

    # words = Counter()
    # words.update(streng)
    # print(words.most_common())

main()