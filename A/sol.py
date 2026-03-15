
# def solve(N, s):
#     n = len(s)

#     def check_valid(s):
#         n = len(s)
#         if s[0] != "M":
#             return False
#         for i in range(1, n-1, 2):
#             if s[i] != "I":
#                 return False
#         for i in range(2, n-1, 2):
#             if s[i] != "T":
#                 return False
            
#         return True
    
#     res = check_valid(s)
#     if res == True:
#         print(0)
#         return
    
#     for i in range(1,n):
#         second_part = s[-i:]    
#         first_part = s[: -i]        
#         new = second_part + first_part

#         if check_valid(new):
#             print(1)
#             return
        
#     print(-1)


def solve(N, s):

    def check_valid(s):
        n = len(s)
        if s[0] != "M":
            return False
        for i in range(1, n-1, 2):
            if s[i] != "I":
                return False
        for i in range(2, n-1, 2):
            if s[i] != "T":
                return False
            
        return True
    
    res = check_valid(s)
    if res == True:
        print(0)
        return
    
    n = len(s)
    # find M
    index = 0
    for i in range(n):
        if s[i] == "M":
            index = i
            break
        
    p2 = s[index:]
    p1 = s[:index]
    new = p2+p1
    result = check_valid(new)
    if result == True:
        print(1)
        return


        
    print(-1)



if __name__ == "__main__":
    T = int(input()) 

    for _ in range(T):
        N = int(input())
        s = input() 
        solve(N,s)
