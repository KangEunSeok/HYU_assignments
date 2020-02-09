import sys
from itertools import combinations

save_freq_patterns = dict()   # save all frequent patterns dictionary


def read_input_file(input_file):    # read input file and make transaction data function
    transaction = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split('\t')
            transaction.append(line)

        f.close()
    return transaction


def make_one_itemset(transaction, min_sup):  # make 1 length frequent patterns
    candidates = []
    removed_patterns = []   # use for remove length 2 patterns that are not frequent pattern
    for tran in transaction:
        candidates += tran
    candidates = list(set(candidates))
    item_set = []
    for pattern in candidates:   # find 1 length frequent patterns and count
        count = 0
        for tran in transaction:
            if pattern in tran:
                count += 1
        if int(count/len(transaction)*100) >= min_sup:  # check item is frequent
            item_set.append(pattern)
            key = tuple([pattern])
            save_freq_patterns[key] = [round(count/len(transaction)*100, 2), count]
        else:  # save no frequent patterns
            removed_patterns.append(pattern)

    return item_set, removed_patterns


def remove_by_minsup(trans, candidates, min_sup):  # remove no frequent patterns in candidate patterns
    freq_patterns = []
    removed_patterns = []
    for key in candidates:
        count = 0
        for tran in trans:  # count candidate pattern in transactions
            if all(elem in tran for elem in key):
                count += 1
        if int(count/len(trans)*100) >= min_sup:  # check item is frequent pattern
            freq_patterns.append(key)
            key = tuple(sorted(key))
            save_freq_patterns[key] = [round(count/len(trans)*100, 2), count]
        else:  # save no frequent patterns
            removed_patterns.append(key)

    return freq_patterns, removed_patterns


def extension_itemset(freq_patterns, join_count):
    # make candidate patterns from frequent patterns ex) length N -> N+1
    patterns = []
    if join_count > 2:
        for freq in freq_patterns:
            for i in range(len(freq)):
                patterns.append(freq[i])
    else:
        patterns = freq_patterns

    patterns = list(set(patterns))
    next_patterns = list(combinations(patterns, join_count))   # make length+1 patterns

    return next_patterns


def pruning(next_patterns, removed_patterns):  # pruning patterns that include removed patterns
    candidate_patterns = []
    # if pattern include removed patterns, pattern is not frequent pattern
    for pattern in next_patterns:
        flag = True
        for r_pattern in removed_patterns:
            if all(elem in pattern for elem in r_pattern):
                flag = False
                continue
        if flag == True:
            candidate_patterns.append(pattern)

    return candidate_patterns


def calcul_sup_conf(freq_patterns):  # calculate frequent pattern support and confidence
    result = []
    for key in freq_patterns.keys():
        if len(key) != 1:
           for i in range(1, len(key)):  # make frequent pattern's sub set
                item_set = list(combinations(key, i))
                for set in item_set:  # calculate support confidence
                    association_set = list(key)
                    set_list = list(set)
                    for s in set_list:  # make association item set
                        association_set.pop(association_set.index(s))
                    result.append([set, association_set, freq_patterns[key][0],
                          round(freq_patterns[key][1]/freq_patterns[set][1]*100, 2)])

    return result


def write_output_file(output_data, output_file):
    # make output file from calculate support and confidence data
    outputs = []
    for data in output_data:
        out = "{"
        for i in range(len(data[0])):
            if i == len(data[0])-1:
                out += data[0][i]
            else:
                out = out + data[0][i] + ","
        out += "}\t{"
        for i in range(len(data[1])):
            if i == len(data[1])-1:
                out += data[1][i]
            else:
                out = out + data[1][i] + ","

        out = out + "}\t" + str(data[2]) + "\t" + str(data[3]) + "\n"
        outputs.append(out)

    f = open(output_file, "w")
    for out in outputs:
        f.write(out)
    f.close()


def main(min_sup, input_file, output_file):
    min_sup = int(min_sup)
    join_count = 1
    trans = read_input_file(input_file)
    patterns, re_patterns = make_one_itemset(trans, min_sup)  # make 1 length frequent patterns
    while len(patterns) != 0:
        join_count += 1
        # remove patterns that are lower than min support
        if join_count > 2:
            fre_patterns, re_patterns = remove_by_minsup(trans, patterns, min_sup)
        if join_count == 2:
            fre_patterns = patterns

        next_patterns = extension_itemset(fre_patterns, join_count)   # make next patterns from frequent patterns
        patterns = pruning(next_patterns, re_patterns)  # pruning patterns that include removed patterns

    output_data = calcul_sup_conf(save_freq_patterns)  # calculate support and confidence
    write_output_file(output_data, output_file)  # make output file


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
