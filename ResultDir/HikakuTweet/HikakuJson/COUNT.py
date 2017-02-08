#coding:utf-8

if __name__ == '__main__':
    import codecs
    import json
    import glob

    count = 0

    fileList = glob.glob("*.json")
    for fn in fileList:
        with codecs.open(fn, "r", "utf-8") as f:
            jsonFILE = json.load(f)
        for j in jsonFILE:
            count += 1

    print count
