def parse_word_tag(file):
    f = open(file, "r")
    word_tag_dict = {}
    for line in f.readlines():
        if line == "\n":
            line = "<s> <s> <s>"
        word_tag = line.split(" ")[:2]
        if word_tag[0] not in word_tag_dict.keys():
            word_tag_dict[word_tag[0]] = {}
        if word_tag[1] not in word_tag_dict[word_tag[0]].keys():
            word_tag_dict[word_tag[0]][word_tag[1]] = 1
        else:
            word_tag_dict[word_tag[0]][word_tag[1]]+=1
    for key1 in word_tag_dict.keys():
        count = sum(word_tag_dict[key1].values())
        for key2 in word_tag_dict[key1].keys():
            word_tag_dict[key1][key2] /= count
    return word_tag_dict

def parse_tag_tag(file):
    f = open(file, "r")
    tag_tag_dict = {}
    tag_list = []
    for line in f.readlines():
        if line == "\n":
            line = "<s> <s> <s>"
        line = line.split(" ")
        tag = line[1]
        tag_list.append(tag)
    for i in range(len(tag_list)-1):
        t0 = tag_list[i]
        t1 = tag_list[i+1]
        if t0 not in tag_tag_dict.keys():
            tag_tag_dict[t0] = {}
        if t1 not in tag_tag_dict[t0].keys():
            tag_tag_dict[t0][t1] = 1
        else:
            tag_tag_dict[t0][t1] +=1
    for key1 in tag_tag_dict.keys():
        count = sum(tag_tag_dict[key1].values())
        for key2 in tag_tag_dict[key1].keys():
            tag_tag_dict[key1][key2] /= count    
    return tag_tag_dict
