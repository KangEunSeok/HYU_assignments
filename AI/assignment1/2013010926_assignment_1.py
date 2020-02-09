import queue
import sys,os


def first_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2
    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- first_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time)


def second_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2

    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- second_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time)


def third_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2
    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- thrid_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time)


def fourth_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2
    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- fourth_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time)


def fifth_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2
    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- fifth_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time)


def test_floor(floor_name, search_algorithm):
    floor_info, floor_map = read_input_files(floor_name)
    if search_algorithm == "astar" or search_algorithm == "greedy":
        length1, time1, optimal_path1 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = heuristic_search_algorithm(floor_info, floor_map, search_algorithm,
                                                                   floor_info[4], floor_info[5])
    elif search_algorithm == "DFS":
        length1, time1, optimal_path1 = DFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = DFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "BFS":
        length1, time1, optimal_path1 = BFS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = BFS(floor_info, floor_map, floor_info[4], floor_info[5])
    elif search_algorithm == "IDS":
        length1, time1, optimal_path1 = IDS(floor_info, floor_map, floor_info[3], floor_info[4])
        length2, time2, optimal_path2 = IDS(floor_info, floor_map, floor_info[4], floor_info[5])

    length = length1+length2
    time = time1+time2
    write_output_file(floor_name, floor_info, floor_map, optimal_path1, optimal_path2, length, time)
    print("----- test_floor -----")
    print("algorithm = ", search_algorithm)
    print("length = ", length)
    print("time = ", time1+time2)


def read_input_files(floor):
    cur_path = os.getcwd()
    os.chdir(cur_path)
    input_path = floor + '_input' + '.txt'
    floor_map = []
    with open(input_path, 'r') as f:
        floor_data = f.readlines()
        for floor_row in floor_data:
            floor_row = floor_row.split()
            floor_row = list(map(int, floor_row))
            floor_map.append(floor_row)

    f.close()
    floor_info = floor_map[0]
    floor_map = floor_map[1:]
    # save start_point, key_point, end_point
    for row in range(len(floor_map)):
        for col in range(int(floor_info[1])):
            if floor_map[row][col] == 3:
                floor_info.append([row, col])
            if floor_map[row][col] == 4:
                floor_info.append([row, col])
            if floor_map[row][col] == 6:
                floor_info.append([row, col])

    return floor_info, floor_map


def write_output_file(floor, floor_info, floor_map, path1, path2, length, time):
    cur_path = os.getcwd()
    os.chdir(cur_path)
    if path1[0] == floor_info[3]:   # remove start_point
        path1.pop(0)
    if path2[-1] == floor_info[5]:  # remove end_point
        path2.pop(-1)
    for i in range(len(path1)):
        floor_map[path1[i][0]][path1[i][1]] = 5

    for i in range(len(path2)):
        floor_map[path2[i][0]][path2[i][1]] = 5

    output_path = floor + '_output' + '.txt'
    
    with open(output_path, 'w') as f:
        for floor_row in floor_map:
            for point in floor_row:
                f.write(str(point)+' ')
            f.write('\n')
        f.write("------------------------\n")
        f.write("length = " + str(length) + "\n")
        f.write("time = " + str(time))

    f.close()

def heuristic_search_algorithm(floor_info, floor_map, algorithm, start_point, end_point):
    length = 0          # check length from start_point
    time = 0            # count all search node
    visited_points = []   # save already searched point
    heuristic_search_queue = queue.PriorityQueue()
    can_go_point = [2, 4, 5, 6]

    cur_point = start_point
    visited_points.append(cur_point)
    save_path = [cur_point]
    # find start_point from end_point
    while cur_point != end_point:
        next_points = []
        # find all next_point from cur_point
        if cur_point[0]-1 > -1:  # move up from cur_point
            if floor_map[cur_point[0]-1][cur_point[1]] in can_go_point \
                    and [cur_point[0]-1, cur_point[1]] not in visited_points:  # check next_point is not in visited points and can move
                next_points.append([cur_point[0]-1, cur_point[1]])       # save next_point
                visited_points.append([cur_point[0]-1, cur_point[1]])    # add to visited_points

        if cur_point[0]+1 < floor_info[1]:  # move down from cur_point
            if floor_map[cur_point[0]+1][cur_point[1]] in can_go_point \
                    and [cur_point[0]+1, cur_point[1]] not in visited_points:  # check next_point is not in visited_point and can move
                next_points.append([cur_point[0]+1, cur_point[1]])       # save next_point
                visited_points.append([cur_point[0]+1, cur_point[1]])    # add to visited_points

        if cur_point[1]-1 > -1:   # move left from cur_point
            if floor_map[cur_point[0]][cur_point[1]-1] in can_go_point \
                    and [cur_point[0], cur_point[1]-1] not in visited_points:  # check next_point is not in visited_point and can move
                next_points.append([cur_point[0], cur_point[1]-1])       # save next_point
                visited_points.append([cur_point[0], cur_point[1]-1])    # add to visited_points

        if cur_point[1]+1 < floor_info[2]:  # move right from cur_point
            if floor_map[cur_point[0]][cur_point[1]+1] in can_go_point \
                    and [cur_point[0], cur_point[1]+1] not in visited_points:  # check next_point is not in visitied_point and can move
                next_points.append([cur_point[0], cur_point[1]+1])       # save next_point
                visited_points.append([cur_point[0], cur_point[1]+1])    # add to visited_points

        for i in range(len(next_points)):
            if algorithm == "greedy":      # calculate eval function = heuristic function
                eval = abs(end_point[0]-next_points[i][0]) + abs(end_point[1]-next_points[i][1])
            elif algorithm == "astar":     # calculate eval function = length from start_point + heuristic function
                eval = (length+1) + abs(end_point[0]-next_points[i][0]) + abs(end_point[1]-next_points[i][1])
            heuristic_search_queue.put((eval, length+1, next_points[i], save_path+[next_points[i]]))

        # find min eval_score and update info
        min_eval_data = heuristic_search_queue.get()
        length = min_eval_data[1]
        cur_point = min_eval_data[2]
        save_path = min_eval_data[3]

        time += 1

    optimal_path = save_path

    return length, time, optimal_path


def DFS(floor_info, floor_map, start_point, end_point):  # Depth first search
    length = 0
    time = 0
    stack = queue.LifoQueue()       # DFS stack save point, point's parent, length
    path_stack = queue.LifoQueue()  # save path stack
    save_path = [start_point]       # save_path
    visited_points = []
    stack.put([start_point, length])
    path_stack.put(save_path)
    cur_point = start_point
    if end_point == floor_info[4]:
        can_go_point = [2, 6]
    elif end_point == floor_info[5]:
        can_go_point = [2, 4]
    while 1:
        count = 0
        if cur_point == end_point:
            break
        # move down from cur_point
        if cur_point not in visited_points:
            if floor_map[cur_point[0]+1][cur_point[1]] in can_go_point and \
                    [cur_point[0]+1, cur_point[1]] not in visited_points:
                count += 1
            if floor_map[cur_point[0]][cur_point[1]+1] in can_go_point and \
                    [cur_point[0], cur_point[1]+1] not in visited_points:
                count += 1
            if floor_map[cur_point[0]][cur_point[1]-1] in can_go_point and \
                    [cur_point[0], cur_point[1]-1] not in visited_points:
                count += 1
            if floor_map[cur_point[0]-1][cur_point[1]] in can_go_point and \
                    [cur_point[0]-1, cur_point[1]] not in visited_points:
                count += 1
            if count > 1:
                stack.put([[cur_point[0], cur_point[1]], length])
                path_stack.put(save_path + [cur_point])

        visited_points.append(cur_point)
        if floor_map[cur_point[0]+1][cur_point[1]] in can_go_point and \
                [cur_point[0] + 1, cur_point[1]] not in visited_points:  # check next_point is not parent and can move
            stack.put([[cur_point[0] + 1, cur_point[1]], length + 1])  # save next_point, parent, length
            save_path = path_stack.get()
            path_stack.put(save_path)
            path_stack.put(save_path + [[cur_point[0] + 1, cur_point[1]]])  # save path from start_point
            cur_point = [cur_point[0]+1, cur_point[1]]
            save_path = save_path + [cur_point]
            length += 1

        # move right from cur_point
        elif floor_map[cur_point[0]][cur_point[1] + 1] in can_go_point and \
                [cur_point[0], cur_point[1] + 1] not in visited_points:  # check next_point is not parent and can move
            stack.put([[cur_point[0], cur_point[1] + 1], length + 1])  # save next_point, parent, length
            save_path = path_stack.get()
            path_stack.put(save_path)
            path_stack.put(save_path + [[cur_point[0], cur_point[1] + 1]])  # save path from start_point
            cur_point = [cur_point[0], cur_point[1]+1]
            save_path = save_path + [cur_point]
            length += 1

        # move left from cur_point
        elif floor_map[cur_point[0]][cur_point[1] - 1] in can_go_point and \
                [cur_point[0], cur_point[1] - 1] not in visited_points:  # check next_point is not parent and can_move
            stack.put([[cur_point[0], cur_point[1] - 1], length + 1])  # save next_point, parent, length
            save_path = path_stack.get()
            path_stack.put(save_path)
            path_stack.put(save_path + [[cur_point[0], cur_point[1]-1]])  # save path from start_point
            cur_point = [cur_point[0], cur_point[1]-1]
            save_path = save_path + [cur_point]
            length += 1

        # move up from cur_point
        elif floor_map[cur_point[0] - 1][cur_point[1]] in can_go_point and \
                [cur_point[0] - 1, cur_point[1]] not in visited_points:  # check next_point is not parent and can move
            stack.put([[cur_point[0] - 1, cur_point[1]], length + 1])  # save next_point, parent, length
            save_path = path_stack.get()
            path_stack.put(save_path)
            path_stack.put(save_path + [[cur_point[0] - 1, cur_point[1]]])  # save path from start_point
            cur_point = [cur_point[0]-1, cur_point[1]]
            save_path = save_path + [cur_point]
            length += 1
        else:
            save_path = path_stack.get()
            stack_factor = stack.get()
            cur_point = stack_factor[0]
            length = stack_factor[1]

        time += 1

    return length, time, save_path


def BFS(floor_info, floor_map, start_point, end_point):  # Breadth first search
    length = 0
    time = 0
    q = queue.Queue()               # BFS queue
    save_parent_q = queue.Queue()   # save parent point
    optimal_path_q = queue.Queue()  # save optimal_path
    can_go_point = [2, 4, 5, 6]
    save_path = [start_point]       # save paths from start_point
    cur_point = [start_point, 0]    # save point and deep

    q.put(cur_point)
    save_parent_q.put(start_point)
    optimal_path_q.put(save_path)

    while cur_point != end_point:
        cur_point = q.get()
        parent_point = save_parent_q.get()
        save_path = optimal_path_q.get()

        length = cur_point[1]
        cur_point = cur_point[0]

        if cur_point[0]+1 < floor_info[1]:  # move down from cur_point
            if floor_map[cur_point[0]+1][cur_point[1]] in can_go_point \
                    and [cur_point[0]+1, cur_point[1]] != parent_point:  # check next_point is not parent and can move
                q.put([[cur_point[0]+1, cur_point[1]], length+1])        # save next_point and length
                optimal_path_q.put(save_path + [[cur_point[0]+1, cur_point[1]]])  # save path from start_point
                save_parent_q.put(cur_point)

        if cur_point[1]+1 < floor_info[2]:  # move right from cur_point
            if floor_map[cur_point[0]][cur_point[1]+1] in can_go_point \
                    and [cur_point[0], cur_point[1]+1] != parent_point:  # check next_point is not parent and can move
                q.put([[cur_point[0], cur_point[1]+1], length+1])        # save next_point and length
                optimal_path_q.put(save_path + [[cur_point[0], cur_point[1]+1]])   # save path from start_point
                save_parent_q.put(cur_point)

        if cur_point[0]-1 > -1:  # move up from cur_point
            if floor_map[cur_point[0]-1][cur_point[1]] in can_go_point \
                    and [cur_point[0]-1, cur_point[1]] != parent_point:  # check next_point is not parent and can move
                q.put([[cur_point[0]-1, cur_point[1]], length+1])        # save next_point and length
                optimal_path_q.put(save_path + [[cur_point[0]-1, cur_point[1]]])  # save path from start_point
                save_parent_q.put(cur_point)

        if cur_point[1]-1 > -1:  # move left from cur_point
            if floor_map[cur_point[0]][cur_point[1]-1] in can_go_point \
                    and [cur_point[0], cur_point[1]-1] != parent_point:  # check next_point is not parent and can_move
                q.put([[cur_point[0], cur_point[1]-1], length+1])        # save next_point and length
                optimal_path_q.put(save_path + [[cur_point[0], cur_point[1]-1]])  # save path from start_point
                save_parent_q.put(cur_point)

        time += 1

    optimal_path = save_path

    return length, time, optimal_path


def IDS(floor_info, floor_map, start_point, end_point):  # Iterative deepening search
    time = 0
    deep = 5          # start deepening search deep
    optimal_path = []
    cur_point = start_point
    if end_point == floor_info[4]:
        can_go_point = [2, 6]
    elif end_point == floor_info[5]:
        can_go_point = [2, 4]
    while cur_point != end_point:
        length = 0
        visited_points = []    # save visited points
        cur_point = start_point
        visited_points.append(cur_point)

        stack = queue.LifoQueue()            # IDS stack
        save_path_stack = queue.LifoQueue()  # save paths from start_point
        stack.put([cur_point, length])       # save cur_point and length
        save_path_stack.put([cur_point])
        deep += 1
        while True:
            cur_point = stack.get()
            save_path = save_path_stack.get()
            length = cur_point[1]
            cur_point = cur_point[0]

            if cur_point == end_point:  # end_point
                optimal_path = save_path
                break
            if length == deep and stack.qsize() != 0:  # IDS length reaches to deep stack pop
                continue

            # move down from cur_point
            if floor_map[cur_point[0]+1][cur_point[1]] in can_go_point \
                    and [cur_point[0]+1, cur_point[1]] not in visited_points:  # check next_point is not in visitied_points and can move
                stack.put([[cur_point[0]+1, cur_point[1]], length+1])          # save next_point
                save_path_stack.put(save_path + [[cur_point[0]+1, cur_point[1]]])  # save path from start_point
                visited_points.append([cur_point[0]+1, cur_point[1]])

            # move right from cur_point
            if floor_map[cur_point[0]][cur_point[1]+1] in can_go_point \
                    and [cur_point[0], cur_point[1]+1] not in visited_points:  # check next_point is not in visitied_points and can move
                stack.put([[cur_point[0], cur_point[1]+1], length+1])          # save next_point
                save_path_stack.put(save_path + [[cur_point[0], cur_point[1]+1]])  # save path from start_point
                visited_points.append([cur_point[0], cur_point[1]+1])

            # move up from cur_point
            if floor_map[cur_point[0]-1][cur_point[1]] in can_go_point \
                    and [cur_point[0]-1, cur_point[1]] not in visited_points:  # check next_point is not in visited_points and can move
                stack.put([[cur_point[0]-1, cur_point[1]], length+1])          # save next_point
                save_path_stack.put(save_path + [[cur_point[0]-1, cur_point[1]]])  # save path from start_point
                visited_points.append([cur_point[0]-1, cur_point[1]])

            # move left from cur_point
            if floor_map[cur_point[0]][cur_point[1]-1] in can_go_point \
                    and [cur_point[0], cur_point[1]-1] not in visited_points:  # check next_point is not in visited_points and can move
                stack.put([[cur_point[0], cur_point[1]-1], length+1])          # save next_point
                save_path_stack.put(save_path + [[cur_point[0], cur_point[1]-1]])  # save path from start_point
                visited_points.append([cur_point[0], cur_point[1]-1])

            if stack.qsize() == 0:
                break
            time += 1

    return length, time, optimal_path


if __name__ == '__main__':
    floors = ['test_floor', 'first_floor', 'second_floor', 'third_floor', 'fourth_floor', 'fifth_floor','best_result']
    algorithm = ['DFS', 'BFS', 'IDS','astar', 'greedy']
    print("Floor list : [ first_floor, second_floor, third_floor, fourth_floor, fifth_floor, test_floor ]")
    print("If you want to show best result each floor.  Input floor_name to [ best_result ]")
    floor_name = input("input floor name : ")
    if floor_name not in floors:
        print("Wrong floor_name input!!")
        exit(1)
    if floor_name != "best_result":
        print("Algorithm list : [DFS, BFS, IDS, astar, greedy]")
        algorithm_name = input("input algorithm name : ")
        if algorithm_name not in algorithm:
            print("Wrong algorithm name input!!!")
            exit(1)

    if floor_name == "first_floor":
        first_floor(floor_name, algorithm_name)
    elif floor_name == "second_floor":
        second_floor(floor_name, algorithm_name)
    elif floor_name == "third_floor":
        third_floor(floor_name, algorithm_name)
    elif floor_name == "fourth_floor":
        fourth_floor(floor_name, algorithm_name)
    elif floor_name == "fifth_floor":
        fifth_floor(floor_name, algorithm_name)
    elif floor_name == "test_floor":
        test_floor(floor_name, algorithm_name)
    elif floor_name == "best_result":
        first_floor(floors[1], algorithm[4])
        second_floor(floors[2], algorithm[0])
        third_floor(floors[3], algorithm[4])
        fourth_floor(floors[4], algorithm[4])
        fifth_floor(floors[5], algorithm[4])


