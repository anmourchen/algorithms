import math


def distance(p1, p2):
    """
    calculate the Euclidean distance between two points
    :param p1: point 1 with (x, y) coordinate
    :param p2: point 2 with (x, y) coordinate
    :return: distance
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(points):
    """
    brute force approach to find the closet pair among a list of points with (x, y) coordinates
    :param points: a list of tuple
    :return: two tuples and distance
    """
    assert len(points) > 1

    p1 = points[0]
    p2 = points[1]
    min_distance = distance(points[0], points[1])
    if len(points) == 2:
        return p1, p2, min_distance

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if i == 0 and j == 1:
                continue
            d = distance(points[i], points[j])
            if d < min_distance:
                p1, p2, min_distance = points[i], points[j], d

    return p1, p2, min_distance


def closet_pair(px, py):
    """
    find the closet pair with O(nlog(n)) time
    :param px: a list of points sorted by x coordinates
    :param py: a list of points sorted by y coordinates
    :return: two tuples and distance
    """
    if len(px) <= 3:
        return brute_force(px)

    Qx = px[:len(px) // 2]
    Rx = px[len(px) // 2:]
    midx = px[len(px) // 2][0]

    Qy = [qy for qy in py if qy[0] <= midx]
    Ry = [ry for ry in py if ry[0] > midx]

    q1, q2, dist1 = closet_pair(Qx, Qy)
    r1, r2, dist2 = closet_pair(Rx, Ry)

    (p1, p2, delta) = (q1, q2, dist1) if dist1 < dist2 else (r1, r2, dist2)

    (t1, t2, dist) = closet_split_pair(px, py, delta, p1, p2)

    if dist < delta:
        return t1, t2, dist
    else:
        return p1, p2, delta


def closet_split_pair(px, py, delta, p1, p2):
    """
    find the closet split pair
    :param px: a list of points sorted by x coordinates
    :param py: a list of points sorted by y coordinates
    :param delta: minimal distance returned from two split regions Q and R
    :param p1: first point returned from two split regions Q and R
    :param p2: second point returned from two split regions Q and R
    :return: two tuples and distance
    """
    midx = px[len(px) // 2][0]
    Sy = [p for p in py if midx - delta <= p[0] <= midx + delta]
    best = delta
    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 7, len(Sy))):
            if distance(Sy[i], Sy[j]) < best:
                p1, p2, best = Sy[i], Sy[j], distance(Sy[i], Sy[j])

    return p1, p2, best


def find_closet_pair(points):
    """
    call the `closet_pair()` to find the closet pair after sorting the points by x and y coordinates
    :param points: a list of points in (x, y) coordinates
    :return: two tuples and distance
    """
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closet_pair(px, py)


def main():
    points = [(1, 2), (2, 9), (3, 4), (12, 9), (3, 8)]
    # Using brute force
    p1, p2, min_dist = brute_force(points)
    print(p1, p2, min_dist)
    # Using divide and conquer
    p1, p2, min_dist = find_closet_pair(points)
    print(p1, p2, min_dist)


if __name__ == '__main__':
    main()
