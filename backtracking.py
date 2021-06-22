import math
import sys


def readfile():
    filename = sys.argv[1]
    variables = []
    for line in open(filename):
        variables.append([int(i) for i in line.strip().split(' ')])
    points = []
    i = 0
    while i < variables[0][0]:
        points.append(variables[i + 1])
        i += 1
    variables[0].append(points)
    return variables[0]


def cost(height, x):
    return alpha * height + beta * x


def impossible():
    print("impossible")
    exit()


def permutation(lst, points_perm):
    if len(lst) == 0:
        return []
    if len(lst) == 2:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        s = permutation(remLst, points_perm)
        for p in s:
            if m < p[0] and p.count(points_perm[-1]):
                l.append([m] + p)
            if not l.count(p) and p.count(points_perm[0]) and p.count(points_perm[-1]):
                l.append(p)
    return l


def possible(points_pos, dist_x):
    radius = dist_x / 2
    span_point = [radius + points_pos[0][0], h - radius]
    return wrong_cases(points_pos, radius, span_point)


def wrong_cases(points_wrong, radius, span_point):
    if radius > h:
        return False
    i = 0
    while i < 2:
        if points_wrong[i][1] > span_point[1] and math.dist(span_point, points_wrong[i]) >= radius:
            return False
        i += 1
    return True


def sum_values(result, height, width):
    result[0] += height
    result[1] += width
    return result


def optimum_aqueduct(ground):
    ind = list(range(len(ground)))
    comb = permutation(ind, ind)
    result = [0, 0]
    solution = backtracking(ground, comb, result)
    if not solution:
        impossible()
    return solution


def backtracking(points_back, comb, result):
    if len(comb) < 1:
        return None
    s = backtracking(points_back, comb[1:], result)
    result = [0, 0]
    pos = comb[0]
    for cur in list(range(len(pos)-1)):
        now = points_back[pos[cur]]
        after = points_back[pos[cur + 1]]
        dist_x = after[0] - now[0]
        if not possible([now, after], dist_x):
            result = None
            break
        if len(pos) - cur == 2:
            result = sum_values(result, h * 2 - now[1] - after[1], dist_x ** 2)
        else:
            result = sum_values(result, h - now[1], dist_x ** 2)
    if result is not None:
        result = cost(result[0], result[1])
    if result is None or s is not None and result > s:
        result = s
    return result


if __name__ == "__main__":
    n, h, alpha, beta, points = readfile()
    sys.setrecursionlimit(sys.getrecursionlimit() + len(points))
    print(optimum_aqueduct(points))
