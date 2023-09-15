import parse_tag_prob as parse

word_tag = parse.parse_word_tag("./train.txt")
tag_tag = parse.parse_tag_tag("./train.txt")

print(word_tag)