def solution(schedules, timelogs, startday):
    answer = 0
    
    # 출근 인정 시각 구하기
    for index, schedule in enumerate(schedules):
        flag = True
        
        t = schedule + 10
        if int(str(t)[1:]) >= 60:
            t += 40
        print(t)
            
        # 날짜 계산
        for i in range(7):
            day = startday + i
            if day >= 8:
                day = day % 7
            
            if day == 6 or day == 7:
                continue
                
            if timelogs[index][i] > t:
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer