import sys, math, copy


def read_input_file(input_file):    # read input#.txt
    input_dict = dict()
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(float, line.strip().split('\t')))
            input_dict[int(line[0])] = line[1:]
        f.close()
    return input_dict


def write_out_file(n, cluster_dict, input_file):
    for i in range(n):
        f = open('test\\'+input_file[:-4]+'_cluster_'+str(i)+'.txt', "w")
        object_ids = cluster_dict[i]
        for id in object_ids:
            f.write(str(id))
            f.write('\n')
        f.close()


def find_cluster_pt(eps, minpts, objects):  # find any core point
    for key1 in objects.keys():
        pt1 = objects[key1]
        in_dist = []
        for key2 in objects.keys():  # find  point that satisfies core point condition
            pt2 = objects[key2]
            dist = math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
            if dist <= eps and dist > 0:
                in_dist.append(pt2)
        if len(in_dist) >= minpts:
            return key1


def dbscan(eps, minpts, cluster_pt, checked_pts, objects):  # DBscan algorithm
    cluster_elem = [cluster_pt]
    core_elem = [cluster_pt]
    while len(checked_pts) != len(cluster_elem):  # if check all core point, end algorithm
        in_dist = []
        for key in objects.keys():
            pt = objects[key]
            dist = math.sqrt((pt[0]-objects[cluster_pt][0])**2 + (pt[1]-objects[cluster_pt][1])**2)
            if dist <= eps and dist > 0:
                in_dist.append(key)

        if len(in_dist) >= minpts:
            core_elem.append(cluster_pt)
            no_dup_elem = list(set(in_dist) - set(cluster_elem))
            for p in no_dup_elem:
                cluster_elem.append(p)

        tmp = list(set(cluster_elem)-set(checked_pts))
        cluster_pt = tmp[0]
        checked_pts.append(cluster_pt)
    return cluster_elem, core_elem


# incoperate remain point to nearest exist cluster
def remained_pt_clustering(objects, original_objects, cluster_dict, core_dict):
    clustered_elem = []
    for key in core_dict.keys():
        clustered_elem.extend(cluster_dict[key])

    for key in objects.keys():
        min_dist = 100000000
        min_dist_pt = 0
        pt1 = objects[key]
        for key1 in clustered_elem:
            pt2 = original_objects[key1]
            dist = math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
            if dist > 0 and dist < min_dist:
                min_dist = dist
                min_dist_pt = key1
        for key1 in cluster_dict.keys():
            if min_dist_pt in cluster_dict[key1]:
                cluster_dict[key1].append(key)

    return cluster_dict



def main(input_file, n, eps, minpts):
    n = int(n)
    eps = int(eps)
    minpts = int(minpts)
    objects = read_input_file('data\\'+input_file)
    original_objects = copy.deepcopy(objects)
    cluster_dict = dict()
    core_dict = dict()

    for i in range(n):
        cluster_dict[i] = []
        core_dict[i] = []
    for i in range(n):
        cluster_pt = find_cluster_pt(eps, minpts, objects)  # find any core point
        checked_pts = []
        cluster_elem, core_elem = dbscan(eps, minpts, cluster_pt, checked_pts, objects)  # run dbscan algorithm
        cluster_dict[i] = cluster_elem  # make one cluster
        core_dict[i] = core_elem
        for id in cluster_elem:  # remove core point from all point objects
            objects.pop(id, None)

    cluster_dict = remained_pt_clustering(objects, original_objects, cluster_dict, core_dict)
    write_out_file(n, cluster_dict, input_file)


if __name__== "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

