map = {
    'Neamt': {'Isai': 87},
    'Isai': {'Neamt': 87, 'Vaslui': 92},
    'Vaslui': {'Isai': 92, 'Urziceni': 142},
    'Urziceni': {'Vaslui': 142, 'Hirsova': 98, 'Bucharest': 85},
    'Hirsova': {'Urziceni': 98, 'Eforice': 86},
    'Eforice': {'Hirsova': 86},
    'Bucharest': {'Urziceni': 85, 'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Sibiu': {'Fagaras': 99, 'Rimnicu Vilcea': 80, 'Oradea': 151, 'Arad': 140},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisora': 118},
    'Timisora': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisora': 111, 'Mehadia': 75},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Pitesti': 138, 'Dobreta': 120, 'Rimnicu Vilcea': 146},
    'Pitesti': {'Craiova': 138, 'Bucharest': 101, 'Rimnicu Vilcea': 97},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146}
}


init = "Oradea"
goal = 'Eforice'


def BFS(init: str, goal: str):
    visited = [init]
    cost = 0
    queue = [init]
    while goal != init:
        init = queue.pop(0)
        print(f"City: {init}")
        l = list(map[init].keys())
        l.sort()
        for city in l:
            if city in visited:
                continue
            else:
                queue.append(city)
                visited.append(city)
                cost += map[init][city]
    return cost


def DFS(init: str, goal: str):
    visited = [init]
    cost = 0
    stack = [init]
    while goal != init:
        init = stack.pop()
        print(f"City: {init}")
        l = list(map[init].keys())
        l = sorted(l)
        for city in l:
            if city in visited:
                continue
            else:
                stack.append(city)
                visited.append(city)
                cost += map[init][city]
    return cost


print(f"Total cost using DFS: {DFS(init, goal)}")
print(f"Total cost using BFS: {BFS(init, goal)}")
