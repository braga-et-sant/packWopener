import os


def main(whitelist, ydk, output):
    """
    Merges a whitelist with a ydk into a new whitelist.
    Used for adding pulls to one's file.
    :param whitelist: Original whitelist filepath
    :param ydk: YDK filepath
    :param output: Resulting file filepath
    """
    d = {}
    if (os.path.isfile(whitelist) and os.path.isfile(ydk)):

        with open(whitelist, 'r') as wfile:
            for line in wfile:
                if not line.startswith(('#', '!', 'ï»¿', '$')):
                    v = line.split(" ", 2)
                    d[v[0]] = int(v[1])

        with open(ydk, 'r') as yfile:
            for line in yfile:
                if not line.startswith(('#', '!', 'ï»¿', '$')):
                    v = line.split(" ", 2)
                    if v[0] in d.keys():
                        if d[v[0]] != 3:
                            d[v[0]] += 1
                    else:
                        d[v[0]] = 1

        with open(output, 'x') as ofile:
            ofile.write("#[" + output + "]" + "\n")
            ofile.write("!" + output + "\n")
            ofile.write("$whitelist\n")
            for key, value in d.items():
                ofile.write(key + " " + str(value) + " --" + "\n")


if __name__ == '__main__':
    main("./test/DraftBanlist.lflist.CONF", "./test/Absolute Powerforce Draft.ydk",
         "./test/DraftListNew.lflist.CONF")
