import os, math
import codecs
import nltk
from konlpy.tag import Twitter


def read_dataset(dataset_path):  # read ratings_test.txt file and get document, label column
    cur_path = os.getcwd()
    os.chdir(cur_path)
    docs = []
    labels = []
    with codecs.open(dataset_path, 'r', encoding='UTF-8') as f:
        train_data = f.readlines()
        for data in train_data:
            split_data = data.split("\t")
            docs.append(split_data[1])
            label = split_data[2].replace("\r\n", "")
            labels.append(label)
    f.close()
    return docs, labels


def read_test_dataset(dataset_path):  # read ratings_test.txt and get id, document column
    cur_path = os.getcwd()
    os.chdir(cur_path)
    docs = []
    ids = []
    with codecs.open(dataset_path, 'r', encoding='UTF-8') as f:
        train_data = f.readlines()
        for data in train_data:
            split_data = data.split("\t")
            id = split_data[0]
            doc = split_data[1].replace("\r\n", "")
            ids.append(id)
            docs.append(doc)
    return ids, docs


def preprocessing_review(reviews, labels, is_test):  # get train data and preprocess reviews
    preprocessed_review = []
    for i in range(1, len(reviews)):
        tokenized_review = twitter.pos(reviews[i])
        tokens = []
        for token in tokenized_review:       # get rid of useless morpheme
            if token[1] == "Josa" or token[1] == "Punctuation":
                continue
            if token[1] == "Eomi" or token[1] == "Determiner":
                continue
            if token[0] == "영화":
                continue
            tokens.append(token[0])
        if is_test == True:
            preprocessed_review.append(tokens)
        else:
            preprocessed_review.append((tokens, labels[i]))

    return preprocessed_review


def tokenize_review(reviews):  # collect token by pos, collect token by neg
    pos_tokens = []
    neg_tokens = []
    for i in range(len(reviews)):
        if reviews[i][1] == "1":
            pos_tokens.extend(reviews[i][0])
        elif reviews[i][1] == "0":
            neg_tokens.extend(reviews[i][0])

    return pos_tokens, neg_tokens


def extract_prob(pos_tokens, neg_tokens, labels):  # make probability table
    prob_pos = 0
    prob_neg = 0
    pos_dic = {}
    neg_dic = {}
    for label in labels:
        if label == "1":
            prob_pos += 1
        else:
            prob_neg += 1
    for token in pos_tokens:
        pos_dic[token[0]] = token[1]/len(pos_tokens)
    for token in neg_tokens:
        neg_dic[token[0]] = token[1]/len(neg_tokens)

    return prob_pos/len(labels), prob_neg/len(labels), pos_dic, neg_dic


def naive_bayes_classifier(prob_pos, prob_neg, pos_dic, neg_dic, val_reviews):  # calculate naive bayes classifier
    results = []
    for i in range(len(val_reviews)):
        review = val_reviews[i]
        predict_pos = 0
        predict_neg = 0
        for token in review:
            pos_exist = pos_dic.get(token)
            neg_exist = neg_dic.get(token)
            if pos_exist == None:
                predict_pos += math.log2(0.0000079)
            else:
                predict_pos += math.log2(pos_dic.get(token))
            if neg_exist == None:
                predict_neg += math.log2(0.0000079)
            else:
                predict_neg += math.log2(neg_dic.get(token))
        predict_neg += math.log2(prob_neg)
        predict_pos += math.log2(prob_pos)
        if predict_pos > predict_neg:
            results.append("1")
        if predict_pos <= predict_neg:
            results.append("0")

    return results


if __name__ == '__main__':
    twitter = Twitter()
    no_data = []
    train_docs, train_labels = read_dataset("ratings_train.txt")
    test_ids, test_docs = read_test_dataset("ratings_test.txt")

    train_reviews = preprocessing_review(train_docs, train_labels, False)
    test_reviews = preprocessing_review(test_docs, no_data, True)
    print("preprocessing end")
    positive_tokens, negative_tokens = tokenize_review(train_reviews)
    re_pos = nltk.Text(positive_tokens, name="pos_train_data").vocab().most_common()
    re_neg = nltk.Text(negative_tokens, name="neg_train_data").vocab().most_common()
    print("train tokenize end")

    prob_pos, prob_neg, pos_dic, neg_dic = extract_prob(re_pos, re_neg, train_labels)
    t_result = naive_bayes_classifier(prob_pos, prob_neg, pos_dic, neg_dic, test_reviews)

    with open("ratings_result1.txt", "w", encoding="UTF-8") as f:
        f.write("id"+"\t"+"document"+"\t"+"label")
        f.write("\n")
        for i in range(len(t_result)):
            f.write(test_ids[i+1]+"\t"+test_docs[i+1]+"\t"+t_result[i])
            f.write("\n")

