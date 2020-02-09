import math
import sys


def read_input_file(input_file):    # read dt_train.txt
    transaction = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split('\t')
            transaction.append(line)
        f.close()
    return transaction


def write_out_file(output_file, test_trans, answer_list):  # write dt_result.txt
    f = open(output_file, "w")
    for i in range(len(test_trans)):   # make result table
        test_trans[i].append(answer_list[i])
    for i in range(len(test_trans)):  # write table to dt_result.txt
        row = ""
        for j in range(len(test_trans[0])):
            row += test_trans[i][j]
            if j != len(test_trans[0])-1:
                row += "\t"
            else:
                row += "\n"
        f.write(row)
    f.close()


def get_trans_answer_val_list(trans):  # make target class domain and dictionary
    target_domain = []
    target_dict = dict()
    for i in range(1, len(trans)):  # make target class domain
        target_domain.append(trans[i][-1])
        target_domain = list(set(target_domain))
    for i in range(len(target_domain)):
        target_dict[target_domain[i]] = 0
    for i in range(1, len(trans)):  # make target class dictionary
        for key in target_dict.keys():
            if key == trans[i][-1]:
                target_dict[key] += 1  # count each class label num
    return target_dict, target_domain


def make_attr_dict_list(trans):  # make attribute dictionary
    attrs_dict_list = []
    attr_domains = []
    for i in range(len(trans[0])-1):  # get attrs domain and attrs_value dictionary
        attr = trans[0][i]
        attr_domain = []
        attr_dict = dict()
        for j in range(1, len(trans)):   # get attr domain
            attr_domain.append(trans[j][i])
        attr_domain = list(set(attr_domain))
        attr_domain.sort()
        for j in range(len(attr_domain)):
            attr_dict[attr_domain[j]] = []
        for key in attr_dict.keys():   # ex {'<=30': [yes, yes, no ...., yes] ... }
            for j in range(1,len(trans)):
                if key == trans[j][i]:
                    attr_dict[key].append(trans[j][-1])
        attrs_dict_list.append(attr_dict)

    for i in range(len(attrs_dict_list)):
        domain = []
        for key in attrs_dict_list[i].keys():
            domain.append(key)
        attr_domains.append(domain)

    return attrs_dict_list, attr_domains


def trans_impurity(trans):   # calculate full trans table entropy
    target_entropy = 0
    target_domain = []
    target_dict = dict()
    for i in range(1, len(trans)):
        target_domain.append(trans[i][-1])
        target_domain = list(set(target_domain))
    for i in range(len(target_domain)):
        target_dict[target_domain[i]] = 0
    for i in range(1, len(trans)):
        for key in target_dict.keys():
            if key == trans[i][-1]:
                target_dict[key] += 1
    for key in target_dict.keys():  # calculate trans table entropy
        target_entropy += (target_dict[key]/(len(trans)-1))*(-math.log(target_dict[key]/(len(trans)-1), 2))

    return target_entropy


def make_new_trans(attr, trans, re_col):  # make new trans remove determined attribute column
    # if attr 'age' selected, remove 'age' column from trans table
    new_trans = []
    attrs = []
    for i in range(len(trans[0])):
        if i != re_col:
            attrs.append(trans[0][i])
    new_trans.append(attrs)
    for i in range(len(trans)):
        if trans[i][re_col] == attr:
            row = []
            for j in range(len(trans[0])):
                if j != re_col:
                    row.append(trans[i][j])
            new_trans.append(row)
    return new_trans


def find_max_info_gain(trans, dt_tree):
    if len(trans[0]) == 1:
        return []
    max_gain = -10000
    dt_var = 0
    entropy_list = []
    attrs_dict_list, attr_domains = make_attr_dict_list(trans)
    target_entropy = trans_impurity(trans)
    for i in range(len(attrs_dict_list)):  # find attribute that has max information gain value
        gain = 0
        attr_entropys = []
        for key in attrs_dict_list[i].keys():
            entropy = 0
            re_domain = list(set(attrs_dict_list[i][key]))
            re_dict = dict()
            for j in range(len(re_domain)):
                re_dict[re_domain[j]] = 0
            for j in range(len(attrs_dict_list[i][key])):
                for h in range(len(re_domain)):
                    if attrs_dict_list[i][key][j] == re_domain[h]:
                        re_dict[re_domain[h]] += 1
            for k in re_dict.keys():
                val = (re_dict[k]/(len(trans)-1))*(-math.log(re_dict[k]/len(attrs_dict_list[i][key]), 2))
                entropy += val
            attr_entropys.append(entropy)
        sum_entropy = 0
        for k in range(len(attr_entropys)):
            sum_entropy += attr_entropys[k]
        gain = target_entropy - sum_entropy
        if gain > max_gain:
            max_gain = gain
            dt_var=i
            entropy_list = attr_entropys

    for i in range(len(entropy_list)):
        if entropy_list[i] == 0.0:
            attrs_dict_list[dt_var][attr_domains[dt_var][i]] = attrs_dict_list[dt_var][attr_domains[dt_var][i]][0]
        else:
            attrs_dict_list[dt_var][attr_domains[dt_var][i]] = 0

    # make dt_tree sub set
    dt_tree[trans[0][dt_var]] = attrs_dict_list[dt_var]

    for key in attrs_dict_list[dt_var].keys():
        if attrs_dict_list[dt_var][key] == 0:
            new_trans = make_new_trans(key, trans, dt_var)  # make new trans table
            new_tree = dict()
            dt_tree[trans[0][dt_var]][key] = find_max_info_gain(new_trans, new_tree)  # recursion

    return dt_tree


def find_answer(trans_row, dt_tree, attrs, return_domain, val_list):  # get target value through dt_tree
    for key in dt_tree.keys():
        sub_tree = dt_tree[key]
        if trans_row[attrs[key]] in sub_tree.keys():
            ssub_tree = sub_tree[trans_row[attrs[key]]]
        else:  # if leaf node is not purity, voting
            min_val = 1000000
            min_key = ""
            val_dict = dict()
            for key in val_list:
                val = "\'"+str(key)+"\'"
                if val in str(sub_tree):
                    val = val[1:-1]
                    val_dict[val] = 1
            for key in val_dict.keys():
                if val_list[key] < min_val:
                    min_val = val_list[key]
                    min_key = key
            return min_key
        if ssub_tree in return_domain:
            return ssub_tree
        answer = find_answer(trans_row, ssub_tree, attrs, return_domain, val_list)

    return answer

def main(input_file, test_file, output_file):
    attrs = dict()
    dt_tree = dict()
    answer_list = []

    trans = read_input_file(input_file)  # make trans table
    val_list, return_domain = get_trans_answer_val_list(trans)  # get target class information
    for i in range(len(trans[0])-1):
        attrs[trans[0][i]] = i
    dt_tree = find_max_info_gain(trans, dt_tree)  # make dt_tree

    test_trans = read_input_file(test_file)
    for i in range(1, len(test_trans)):  # get test.txt and make result.txt file
        answer = find_answer(test_trans[i], dt_tree, attrs, return_domain, val_list)
        answer_list.append(answer)
    answer_list.insert(0, trans[0][-1])
    write_out_file(output_file, test_trans, answer_list)


if __name__== "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
