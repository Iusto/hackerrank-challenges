if __name__ == '__main__':
    answer = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        answer.append([name,score]) 
     
    answer.sort(key = lambda x : (x[1],x[0]))  
    score_sort = list(sorted(set([i[1] for i in answer])))
    for i in range (len(answer)) :
        if answer[i][1] == score_sort[1] : 
            print(answer[i][0]) 