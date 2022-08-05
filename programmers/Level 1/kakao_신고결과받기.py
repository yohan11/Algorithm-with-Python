def solution(id_list,report,k):
    report=set(report) #한 유저가 동일한 유저 신고했을 때 중복 없애줌

    dict_report={} #report 데이터 정렬
    for a_report in report:
        a_report=a_report.split()
        if a_report[0] in dict_report.keys():
            dict_report[a_report[0]].append(a_report[1])
        else:
            dict_report[a_report[0]]=[a_report[1]]

    report_count={} #각 유저가 몇번 신고 당했는지
    for reported_user_list in dict_report.values():
        for reported_user in reported_user_list:
                if reported_user in report_count.keys():
                    report_count[reported_user]+=1
                else:
                    report_count[reported_user]=1

    frozen_user=[] #정지된 유저들
    for name,count in report_count.items():
        if int(count)>=k :
            frozen_user.append(name)

    mail_count= {id:0 for id in id_list}
    for report_user, reported_user_list in dict_report.items():
        for reported_user in reported_user_list:
            if reported_user in frozen_user:
                mail_count[report_user]+=1
    result=list(mail_count.values())

    return result
