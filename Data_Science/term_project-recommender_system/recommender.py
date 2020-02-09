import math, sys

def read_input_file(input_file):    # read u#.base
    user_num, item_num = 0, 0
    user_info = []
    input_data = []
    object_dict = dict()
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(int, line.strip().split('\t')))
            input_data.append(line)
        f.close()
    for row in input_data:
        if row[0] > user_num:
            user_num = row[0]
        if row[1] > item_num:
            item_num = row[1]
    for i in range(item_num):
        object_dict[i+1] = []
    for row in input_data:
        object_dict[row[1]].append(row[0])
    for _ in range(user_num+1):
        tmp = [0 for _ in range(2000)]
        user_info.append(tmp)
    for row in input_data:
        user_info[row[0]][row[1]] = row[2]

    return user_info, object_dict


def read_input_matrix_file(input_file):    # read u#_matrix.txt
    user_matrix = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(float, line.strip().split(' ')))
            user_matrix.append(line)
        f.close()

    return user_matrix


def read_test_file(test_file):
    test_data = []
    with open(test_file) as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(int, line.strip().split('\t')))
            test_data.append(line)
        f.close()

    return test_data


def write_output_file(output_file, rating_result):
    f = open(output_file, "w")
    for row in rating_result:
        line = str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2])
        f.write(line)
        f.write('\n')
    f.close()


def get_user_frequent_score(user_info):
    freq_score = [[0, 0, 0, 0, 0]]
    for i in range(1, len(user_info)):
        freq_score.append([0, 0, 0, 0, 0])
        for j in range(1, len(user_info[0])):
            if user_info[i][j] != 0:
                freq_score[i][user_info[i][j]-1] += 1
    return freq_score


def get_user_frequent_value(freq_user_scores, row):
    freq_user_val = max(freq_user_scores[row[0]])
    freq_user_index = freq_user_scores[row[0]].index(freq_user_val)
    if sum(freq_user_scores[row[0]]) != 0:
        freq_user_per = round(freq_user_scores[row[0]][freq_user_index]/sum(freq_user_scores[row[0]]), 2)
    else:
        freq_user_per = 0
    return freq_user_index+1, freq_user_per


def get_item_frequent_score(user_info):
    freq_score = [[0, 0, 0, 0, 0]]
    for i in range(1, len(user_info[0])):
        freq_score.append([0, 0, 0, 0, 0])
        for j in range(1, len(user_info)):
            if user_info[j][i] != 0:
                freq_score[i][user_info[j][i]-1] += 1
    return freq_score


def get_item_frequent_value(freq_item_scores, row):
    freq_item_val = max(freq_item_scores[row[1]])
    freq_item_index = freq_item_scores[row[1]].index(freq_item_val)
    if sum(freq_item_scores[row[1]]) != 0:
        freq_item_per = round(freq_item_scores[row[1]][freq_item_index]/sum(freq_item_scores[row[1]]), 2)
    else:
        freq_item_per = 0
    return freq_item_index+1, freq_item_per


def calcul_all_euclidean_dis(user_info):
    sim_dict = dict()
    for i in range(len(user_info)):
        sim_dict[i] = dict()
    for i in range(1, len(user_info)-1):
        for j in range(i+1, len(user_info)):
            sub_dict1, sub_dict2 = sim_dict[i], sim_dict[j]
            elem = 0
            for h in range(1, len(user_info[0])):
                elem += pow((user_info[i][h]-user_info[j][h]), 2)
            dis = pow(elem, 0.5)
            sub_dict1[j] = dis
            sub_dict2[i] = dis
            sim_dict[i] = sub_dict1
            sim_dict[j] = sub_dict2
    return sim_dict


def calcul_all_cos_sim(user_info):
    sim_dict = dict()
    for i in range(len(user_info)):
        sim_dict[i] = dict()
    for i in range(1, len(user_info)-1):
        for j in range(i+1, len(user_info)):
            sub_dict1, sub_dict2 = sim_dict[i], sim_dict[j]
            co_sim_numer, co_sim_denom1, co_sim_denom2 = 0, 0, 0
            for h in range(1, len(user_info[0])):
                co_sim_numer += user_info[i][h]*user_info[j][h]
                co_sim_denom1 += user_info[i][h]*user_info[i][h]
                co_sim_denom2 += user_info[j][h]*user_info[j][h]
            co_sim_denom = math.sqrt(co_sim_denom1*co_sim_denom2)
            co_sim = co_sim_numer/co_sim_denom
            sub_dict1[j] = co_sim
            sub_dict2[i] = co_sim
            sim_dict[i] = sub_dict1
            sim_dict[j] = sub_dict2
    return sim_dict


def calcul_all_pearson_sim(user_info):
    sim_dict = dict()
    for i in range(len(user_info)):
        sub_dict = dict()
        sim_dict[i] = sub_dict
    for i in range(1, len(user_info)-1):
        for j in range(i+1, len(user_info)):
            n, sum1, sum2, pow1, pow2, sum_pow = 0, 0, 0, 0, 0, 0
            sub_dict1 = sim_dict[i]
            sub_dict2 = sim_dict[j]
            for h in range(1, len(user_info[0])):
                if user_info[i][h] != 0 and user_info[j][h] != 0:
                    n += 1
                    sum1 += user_info[i][h]
                    sum2 += user_info[j][h]
                    pow1 += user_info[i][h]**2
                    pow2 += user_info[j][h]**2
                    sum_pow += user_info[i][h]*user_info[j][h]
            pear_sim = -1
            if n != 0:
                pear_sim = ((n*pow1-(sum1**2))*(n*pow2-(sum2**2)))**0.5
                if pear_sim != 0:
                    pear_sim = (n*sum_pow-sum1*sum2) / pear_sim
                    if complex == type(pear_sim):
                        pear_sim = pear_sim.real
                else:
                    pear_sim = -1
            sub_dict1[j] = pear_sim
            sub_dict2[i] = pear_sim
            sim_dict[i] = sub_dict1
            sim_dict[j] = sub_dict2
    return sim_dict


# find similar users that rank to input item
def find_similar_users(user_info, user_name, item, object_list, sim_dict):
    max_rate, max_score = 0, 0
    scores = dict()
    count = 0
    for i in range(1, 6):
        scores[i] = 0
    for i in range(len(object_list)):
        val = round(sim_dict[user_name][object_list[i]], 2)
        if val > 0:
            count += 1
            scores[user_info[object_list[i]][item]] += val
    for k in scores.keys():
        if max_score < scores[k]:
            max_score = scores[k]
            max_rate = k

    all_zero_flag = False
    for k in scores.keys():
        if scores[k] > 0:
            all_zero_flag = True
    if all_zero_flag == False:
        max_rate = 0

    return [user_name, item, max_rate]


def find_sim_users(user_info, user_id, item_id):
    if len(user_info[0]) < item_id:
        rated_rank = [user_id, item_id, -1]
    else:
        rated_rank = [user_id, item_id, round(user_info[user_id-1][item_id-1])]
    return rated_rank


def main(input_file, test_file):
    user_info, object_dict = read_input_file('data\\'+input_file)
    user_matrix = read_input_matrix_file('trained_u_matrix\\'+input_file[:2]+'_matrix.txt')
    test_matrix = read_test_file('data\\'+test_file)
    write_file = 'test\\'+input_file[:2]+'.base_prediction.txt'

    rated_result = []
    freq_user_scores = get_user_frequent_score(user_info)
    freq_item_scores = get_item_frequent_score(user_info)

    for i in range(len(user_matrix)):
        for j in range(len(user_matrix[0])):
            user_matrix[i][j] = round(user_matrix[i][j])

    #sim_dict = calcul_all_euclidean_dis(user_info)

    for row in test_matrix:
        rated_info = find_sim_users(user_matrix, row[0], row[1])
        freq_user_index, freq_user_per = get_user_frequent_value(freq_user_scores, row)
        freq_item_index, freq_item_per = get_item_frequent_value(freq_item_scores, row)
        if rated_info[2] < 1 or rated_info[2] > 5:
            if freq_user_per >= freq_item_per:
                rated_info[2] = freq_user_index
            else:
                rated_info[2] = freq_item_index

        rated_result.append(rated_info)

    write_output_file(write_file, rated_result)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
