N = int(input())
art_list = []

for _ in range(N):
    graph = [[""] * 7 for i in range(5)]
    for i in range(5):
        row = input()
        for j in range(7):
            graph[i][j] = row[j]
    art_list.append(graph)
answer_list = {}
for a in range(len(art_list)):
    for b in range(a + 1, len(art_list)):
        answer_list[a + 1, b + 1] = 0
        for i in range(5):
            for j in range(7):
                if art_list[a][i][j] != art_list[b][i][j]:
                    answer_list[a + 1, b + 1] += 1

for i in answer_list.keys():
    if answer_list[i] == min(answer_list.values()):
        for n in i:
            print(n, end=" ")
