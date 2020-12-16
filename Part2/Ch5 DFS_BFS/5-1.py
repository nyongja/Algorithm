# 음료수 얼려 먹기(p.149)

def dfs(ice_tray, x, y, n, m) :
 
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    if ice_tray[x][y] == 0 :
        ice_tray[x][y] = 1
        dfs(ice_tray, x-1, y, n, m)
        dfs(ice_tray, x+1, y, n, m)
        dfs(ice_tray, x, y+1, n, m)
        dfs(ice_tray, x, y-1, n, m)
        return True
    else : return False

if __name__ == "__main__" :
    n, m = map(int, input().split())
    ice_tray = []
    for i in range(n) :
        ice_tray.append(list(map(int, input())))
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(ice_tray, i, j, n, m) == True:
                result += 1
    print(result)