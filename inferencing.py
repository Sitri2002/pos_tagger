import parse_tag_prob as parse
import numpy as np
word_tag = parse.parse_word_tag("./train.txt")
tag_tag = parse.parse_tag_tag("./train.txt")

def input_ngram(input):
    input = "<s> " + input
    ngram = []
    input = input.split(" ")
    print(input)
    for i in range(len(input)+1):
        ngram.append(input[:i])
    return ngram[1:]


def viterbi(input , word_tag, tag_tag):
    prob_init = 1
    for state in ("<s> "+input).split(" "):
        for key in word_tag[state]:
            


viterbi("I am racing .", word_tag, tag_tag)
