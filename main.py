# cleaning text
# 1. create example txt which contain text that we want to convert
# 2. Convert the letter to lower case for consistency
# 3. Remove any punctuation like @ ! <> and soo on

import string
from  collections import Counter

text = open('example_text.txt', encoding='utf-8').read()
text_lower_case = text.lower()
clean_text = text_lower_case.translate(str.maketrans('','',string.punctuation))
# print(clean_text)

# Stopword List
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

tokenize_word = clean_text.split()

final_word = []
for word in tokenize_word:
    if word not in stop_words:
        final_word.append(word)

# print(final_word)

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace("'", '').replace(',','').strip()
        word, emotion = clear_line.split(':')
        if word in final_word:
            emotion_list.append(emotion)

print(emotion_list)
count_emotion = Counter(emotion_list)
print(count_emotion)
