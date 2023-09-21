def solution(orders, course):
    single_menu_num = {}
    answer = []
    for order in orders:
        for menu in order:
            if menu in single_menu_num.keys():
                single_menu_num[menu] += 1
            else:
                single_menu_num[menu] = 1
    
    for num in course:
        menu_package = ""
        for i in range(num):
            for key, value in single_menu_num.items():
                if value == max(single_menu_num.values()):
                    menu_package += key
                    del single_menu_num[key]
        answer.append(menu_package)
        

    
    return answer

orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,4,5]

print(solution(orders, course))