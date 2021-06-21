import math
import sys


def readfile():
    filename = "secret-01.in"
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
    solution = greedy(ground, [0, 0, 0])
    if not solution:
        impossible()
    return solution


def greedy(points_greed, result):
    if len(points_greed) == 0:
        return [0, 0, 0]
    now = points_greed[0]
    error = False
    s = [0, 0, 0]
    minimum = [0, 0, 0]
    for i in list(range(1, len(points_greed))):
        after = points_greed[i]
        dist_x = after[0] - now[0]
        if not possible([now, after], dist_x):
            error = True
        elif len(points_greed) == 2:
            s = sum_values(s, h * 2 - now[1] - after[1], dist_x ** 2)
            s[2] = i
        else:
            s = sum_values(s, h - now[1], dist_x ** 2)
            s[2] = i
        if i == 1 and not error:
            minimum = s
        elif cost(minimum[0], minimum[1]) > cost(s[0], s[1]) and not error:
            minimum = s
    if error and minimum == [0, 0, 0]:
        impossible()
    greedy(points_greed[result[2]:], result + minimum)
    return result


if __name__ == "__main__":
    n, h, alpha, beta, points = readfile()
    print(optimum_aqueduct(points))
