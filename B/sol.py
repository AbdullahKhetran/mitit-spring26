def solve(N, points):
    if len(points) == 1:
        print(0)
        return 
    
    points.sort()

    def check_min(points):
        total_points= 0
        min = points[0]
        for i in range(len(points) - 1, -1, -1):
            o1 = min
            o2 = points[i]
            point = abs(o1 - o2)
            total_points += point
        return total_points
    
    def check_max(points):
        total_points= 0
        max = points[-1]
        for i in range(len(points) - 1):
            o1 = max
            o2 = points[i]
            point = abs(o1-o2)
            total_points += point
        return total_points
    
    a = check_min(points)
    b = check_max(points)

    best = max(a,b)
    print(best)

    # for i in range(len(points) - 1):
    #     point = abs(points[i] - points[len(points) - 1])
    #     max_points += point
    
    # print(max_points)


if __name__ == "__main__":
    T = int(input()) 

    for _ in range(T):
        N = int(input())
        points = list(map(int, input().split()))
        solve(N, points)
