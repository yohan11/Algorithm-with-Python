def solution(s):
    my_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
               'zero': '0'}

    answer=""
    word=""
    while len(s)>0:
        for char in s:
            word+=char
            if word in my_dict.keys():
                answer+=my_dict.get(word)
                s=s.replace(word,'')
                word=""
            elif word in my_dict.values():
                answer+=char
                s=s.replace(char,"")
                word=""
            else:
                continue

    return int(answer)
