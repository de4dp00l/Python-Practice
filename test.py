def get_sec_lowest(values):
    sorting_value = sorted(values, key= lambda x: x[1])
    get_lowest_value = min(sorting_value, key= lambda x: x[1])[1]
    remove_first_lowest_value = [i for i in sorting_value if i[1] > get_lowest_value]

    if remove_first_lowest_value:
        sec_lowest = [i for i in remove_first_lowest_value if i[1] == remove_first_lowest_value[0][1]]
        return [z[0] for z in sec_lowest]
    else:
        return []

if __name__ == '__main__':
    lists = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lists.append([name, score])
    
    results = get_sec_lowest(lists)
    print('\n'.join(sorted(results)))