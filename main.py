# # процесс создания графа ---------------------------------------
# graph = {
#     'q0': [['q1', 'e'], ['q2', 'b']],
#     'q1': [['q0', 'c'], ['q2', 'a']],
#     'q2': [['q1', 'c']]
# }
# веса
weights = ('a', 'b', 'c')

graph = {
    'q0': [['q1', 'e'], ['q1', 'b'], ['q2', 'e'], ['q2', 'c']],
    'q1': [['q0', 'a'], ['q0', 'c'], ['q1', 'c'], ['q2', 'b']],
    'q2': []

}


# веса


# --------------------------------------------------------------

def is_sublist(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i + len(list2)] == list2:
            return True
    return False


if __name__ == '__main__':
    print('e-замыкания-----------------------')
    table_first = {}
    for vertex, i in zip(graph, range(len(graph))):
        table_first[f's{i}'] = [vertex]
        # print(vertex, i)
        for edge in graph.get(vertex):
            if edge[1] == 'e':
                table_first.get(f's{i}').append(edge[0])
    print(table_first)
    print('таблица №2')
    table_second = {}
    # def find_all_weight(weight, vertex):
    for vertex in table_first:  # проход по S
        table_second[vertex] = []
        for weight in weights:  # проход по буквам a,b,c.......
            list_ver = []
            for value in table_first.get(vertex):  # проход по множествам каждого S
                if graph.get(value) is None:
                    continue
                for e in graph.get(value):  # рассматриваем все возможные пути у q
                    # bol = False
                    if weight in e:
                        # bol = True
                        list_ver.append(e[0])
                        if graph.get(e[0]) is None:
                            continue
                        else:
                            for e_2 in graph.get(e[0]):  # если есть данная буква то смотрим дальше
                                if weight in e_2 or 'e' in e_2:
                                    list_ver.append(e_2[0])
                    elif 'e' in e:  # если есть эпсилон то смотрим дальше
                        if graph.get(e[0]) is None:
                            continue
                        else:
                            for e_2 in graph.get(e[0]):
                                if weight in e_2:
                                    list_ver.append(e_2[0])
            copy_list = list_ver.copy()
            list_ver.clear()
            [list_ver.append(x) for x in copy_list if x not in list_ver]

            table_second.get(vertex).append([])

            for s in table_first:
                if is_sublist(list_ver, table_first.get(s)):
                    table_second.get(vertex)[-1].append(s)
    print(table_second)

    print('таблица №3')
    table_p = {}
    table_third = {}
    list_for_p0 = []
    for s in table_first:
        if is_sublist(table_first.get('s0'), table_first.get(s)):
            list_for_p0.append(s)
    table_p['p0'] = list_for_p0
    print(table_p)
    while not len(table_p) == len(table_third):
        ind = 'p0'
        while not len(table_p) == len(table_third):
            list_abc = [[] for _ in range(len(weights))]
            for weight, i in zip(weights, range(len(weights))):
                list_ver = []
                for s in table_p.get(ind):
                    list_ver.append(table_second.get(s)[i])
                copy_list = list_ver.copy()
                list_ver.clear()
                [list_ver.append(x) for x in copy_list if x not in list_ver]
                if any(list_ver):
                    list_ver.sort()
                    if not list_ver[0]:
                        list_ver.pop(0)
                # if not list_ver:
                #     list_ver.append([])
                for p in table_p:
                    if not list_ver[0]:
                        list_abc[i] = 'oo'
                        break
                    if table_p.get(p) == list_ver[0]:
                        list_abc[i] = p
                        break
                else:
                    new_p = f'p{len(table_p)}'
                    table_p[new_p] = list_ver[0]
                    list_abc[i] = new_p
            table_third[ind] = list_abc
            ind = f'p{len(table_third)}'
    print(table_third)
    # for p in table_p:
    #     list_final_p = [[] for _ in range(len(weights))]
    #     for weight, i in zip(weights, range(len(weights))):
    #         list_ver = []
    #         for s in table_p.get(p):
    #             list_ver.append(table_second.get(s)[i])
    #         copy_list = list_ver.copy()
    #         list_ver.clear()
    #         [list_ver.append(x) for x in copy_list if x not in list_ver]
    #         if any(list_ver):
    #             list_ver.sort()
    #             if not list_ver[0]:
    #                 list_ver.pop(0)
    #         # print(list_ver)
    #         for p_2 in table_p:
    #             if table_p.get(p_2) == list_ver:
    #                 break
    #         else:
    #             table_p[f'p{i+1}'] = list_ver
    # l = [[] for _ in range(3)]
    # print(any(l))
