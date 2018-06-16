stop_words = ["a","an","restaurant","restaurant"]
from collections import Counter
# Function to remove stopwords
def remove_stopwords(input_list):
    return [i for i in input_list if i not in stop_words]

# Function to find String Matching
def match_string(str1, str2):
    list1 = str1.lower().strip().split()
    list2= str2.lower().strip().split()
    set_list1 = list(set(list1))
    set_list2 = list(set(list2))
    ps12=0
    ps21=0
    combined_list = set_list1+set_list2
    wt_stopwords = remove_stopwords(combined_list)
    counter = Counter(wt_stopwords)
    matched_words = []
    for i in counter:
        if counter[i]>1:
            matched_words.append(counter[i])
    try:
        ps12 = len(matched_words)/len(list1)
    except Exception as e:
        print("Exception in calculating percentage 1 : ",e)
        pass

    try:
        ps21 = len(matched_words)/len(list2)*100
    except Exception as e:
        print("Exception in calculating percentage 2 : ",e)
        pass
    return ps12,ps21


