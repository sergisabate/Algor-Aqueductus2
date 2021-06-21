import math
import sys
import threading


def readfile():
    filename = "secret-03.in"
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


def cost(data):
    return alpha * data[0] + beta * data[1]


def impossible():
    print("impossible")
    exit()


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
    result = [0, 0]
    solution = dynamic(ground, result)
    if not solution:
        impossible()
    return solution


def dynamic(points_dyn, result):
    if len(points_dyn) == 1:
        return cost([10000, 10000])
    for i in list(range(1, len(points_dyn))):
        now = points_dyn[0]
        after = points_dyn[1]
        after_pos = 1
        dist_x = after[0] - now[0]
        if possible([now, after], dist_x):
            if len(points_dyn) == 2:
                return cost(sum_values(result, h * 2 - now[1] - after[1], dist_x ** 2))
            else:
                result = sum_values(result, h - now[1], dist_x ** 2)
        else:
            if len(points_dyn) == 2:
                impossible()
            for j in list(range(2, len(points_dyn))):
                after = points_dyn[j]
                after_pos = j
                dist_x = after[0] - now[0]
                if possible([now, after], dist_x):
                    break
            result = sum_values(result, h - now[1], dist_x ** 2)
        return min((dynamic(points_dyn[after_pos:], result), dynamic(points_dyn[i:], result)))
    return result


if __name__ == "__main__":
    n, h, alpha, beta, points = readfile()
    print(optimum_aqueduct(points))
