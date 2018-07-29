def make_map():

    with open("neko.txt.mecab", "r") as f:
        data = f.readlines()
        sentence = []
        for line in data:
            left = line.split("\t")
            if len(left) <= 1:
                continue
            right = left[1].split(",")
            left = left[0]
            dic = {"surface": left,
                    "base": right[6],
                    "pos": right[0],
                    "pos1": right[1]
            }
            sentence.append(dic)

            if right[1] == "句点":
                yield sentence
                sentence = []


