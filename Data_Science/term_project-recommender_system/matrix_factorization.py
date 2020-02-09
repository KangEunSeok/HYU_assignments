import numpy as np


class MatrixFactorization():
    def __init__(self, M, K, learning_rate, reg_param, epochs):
        # init training param
        self.Matrix = M   # user/object rating matrix
        self.num_users, self.num_items = M.shape  # user_num, item_num
        self.K = K   # factorizing param
        self.learning_rate = learning_rate  # training learning rate
        self.reg_param = reg_param  # error update parameter
        self.epochs = epochs   # training epoch

    def factorize_training(self):
        # init factorize matrix
        self.user_F = np.random.normal(size=(self.num_users, self.K))  # user_num x K matrix, user feature
        self.item_F = np.random.normal(size=(self.num_items, self.K))  # item_num x K matrix, item feature
        # init biases
        self.bias_user_F = np.zeros(self.num_users)
        self.bias_item_F = np.zeros(self.num_items)
        self.bias = np.mean(self.Matrix[np.where(self.Matrix != 0)])

        for epoch in range(self.epochs):
            # traing matrix by existing rate information
            for i in range(self.num_users):
                for j in range(self.num_items):
                    if self.Matrix[i, j] > 0:
                        self.gradient_descent(i, j, self.Matrix[i, j])
            cost = self.cost()

            # print training status
            if (epoch + 1) % 10 == 0:
                print("iter: %d, cost = %.6f" % (epoch+1, cost))

    def cost(self):
        # compute root mean square error
        cost = 0
        valid_x, valid_y = self.Matrix.nonzero()  # In Matrix, no zero element == rated value
        predicted = self.bias + self.bias_user_F[:, np.newaxis] + self.bias_item_F[np.newaxis:, ] \
                    + self.user_F.dot(self.item_F.T)
        for x, y in zip(valid_x, valid_y):
            cost += pow(self.Matrix[x, y] - predicted[x, y], 2)

        return np.sqrt(cost) / len(valid_x)


    def gradient_descent(self, i, j, rating):
        # get error value
        prediction = self.bias + self.bias_user_F[i] + self.bias_item_F[j] \
                     + self.user_F[i, :].dot(self.item_F[j, :].T)
        error = rating - prediction

        # update biases
        self.bias_user_F[i] += self.learning_rate * (error - self.reg_param * self.bias_user_F[i])
        self.bias_item_F[j] += self.learning_rate * (error - self.reg_param * self.bias_item_F[j])
        # desent value
        dp = (error * self.item_F[j, :]) - (self.reg_param * self.user_F[i, :])
        dq = (error * self.user_F[i, :]) - (self.reg_param * self.item_F[j, :])
        # update latent feature
        self.user_F[i, :] += self.learning_rate * dp
        self.item_F[j, :] += self.learning_rate * dq

    def get_result_matrix(self):
        factorized_matrix = self.bias + self.bias_user_F[:, np.newaxis] + self.bias_item_F[np.newaxis:, ] \
                            + self.user_F.dot(self.item_F.T)
        return factorized_matrix, \
               self.bias + self.bias_user_F[:, np.newaxis] + self.user_F,\
               self.bias + self.bias_item_F.T[np.newaxis:, ]+self.item_F.T


def read_input_file(input_file):    # read u#.base data
    user_num = 0
    item_num = 0
    user_info = []
    input_data = []
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
    for _ in range(user_num):
        tmp = [0 for _ in range(item_num)]
        user_info.append(tmp)
    for row in input_data:
        user_info[row[0]-1][row[1]-1] = row[2]

    return user_info


def write_factorized_matrix(output_file_name, matrix):
    f = open(output_file_name, "w")
    for row in matrix:
        line = ''
        for i in range(len(row)):
            line += str(round(row[i], 2)) + ' '
        f.write(line)
        f.write('\n')
    f.close()

def main():
    # M is user-object rating matrix
    for i in range(1, 6):
        input_file_name = 'data\\u' + str(i) + '.base'
        output_user_file = 'trained_u_matrix\\u' + str(i) + '_user_matrix.txt'
        output_item_file = 'trained_u_matrix\\u' + str(i) + '_item_matrix.txt'
        output_file = 'trained_u_matrix\\u' + str(i) + '_matrix.txt'
        M = np.array(read_input_file(input_file_name))
        print(M.shape)
        M_factorizer = MatrixFactorization(M, K=170, learning_rate=0.01, reg_param=0.01, epochs=500)
        M_factorizer.factorize_training()
        factorized_matrix, user_matrix, item_matrix = M_factorizer.get_result_matrix()

        factorized_matrix = np.ndarray.tolist(factorized_matrix)
        write_factorized_matrix(output_user_file, user_matrix)
        write_factorized_matrix(output_item_file, item_matrix)
        write_factorized_matrix(output_file, factorized_matrix)


if __name__ == "__main__":
    main()
