def main():
    alfabet = [26]

    for a in range(97, 123):
        alfabet.append(chr(a))

    x = 24
    c = 3
    y = 25
    print(alfabet[x], alfabet[c], alfabet[y])

    for k in alfabet:
        x += 1
        c += 1
        y += 1

        if x > 26:
            x = 1
        elif y > 26:
            y = 1
        elif c > 26:
            c = 1

        print(alfabet[x], alfabet[c], alfabet[y])
main()