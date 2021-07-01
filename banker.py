

while(1):   ###infinite loop


    #######safety algorithm function ######
    def safe(available, m, n,need,alloc):
        ##### safety algorithm #####
        finish = []
        work = []
        for i in range(0, m):
            work.append(available[i])

        temp1 = []
        need_new = []  ###change in its values and not affect the origional one
        for i in range(0, n):
            for j in range(0, m):
                temp1.append(need[i][j])
            need_new.append(temp1)
            temp1 = []


        sequence = []
        for i in range(0, n):
            finish.append("false")

        #print(f'finish: {finish}')

        i = 0
        y = False
        done =0
        while i < n + i and i < n * n:
            # for i in range(0, n+i):
            if finish[i % n] == "false":
                for j in range(0, m):
                    if (need_new[i % n][j] <= work[j]):
                        done+=1
                if done==m:
                    for j in range(0, m):
                        work[j] += alloc[i % n][j]
                        need_new[i % n][j] = 0
                done=0
                    # elif (need[i%n][j] > work[j])
                for j in range(0, m):
                    if need_new[i % n][j] == 0:
                        x = 0
                    else:
                        x = 1
                        break
                if x == 0:
                    finish[i % n] = "true"
                    sequence.append(f'P{i % n}')

                # check for more
                sum = 0
                for a in range(0, n):
                    if finish[a] == "true":
                        sum += 1

                if sum == n:
                    #print("safe")
                    #print(f'sequence: {sequence}')
                    y = True
                    return True,sequence
                    break
                # if sum<n and i==n:
                #     y=False
                #     break
                else:
                    y = False

            i += 1
        if y == False:
            #print("not safe")
            return False,[]
        #print(f'finish: {finish}')



####### request resource algorithm function #########
    def request(m,n,available,alloc,need,r,p):
        ##### resource request algorithm #####

        flag = 0
        msg = ""
        available_new = []
        for i in range(0, m):
            available_new.append(available[i])
        temp1=[]
        temp2=[]
        alloc_new=[]
        need_new=[]
        for i in range(0,n):
            for j in range(0,m):
                temp1.append(alloc[i][j])
                temp2.append(need[i][j])
            alloc_new.append(temp1)
            need_new.append(temp2)
            temp1=[]
            temp2=[]
        done=0
        for i in range(0, m):
            if r[i] <= need_new[p][i]:  # accepted
                if r[i] <= available_new[i]:
                    done+=1
                    flag = 1
                else:
                    flag = 0
                    msg = "No, it can't be granted. There are not enough resources."
                    return msg, False, []
                    break
            else:
                flag = 0
                msg = "ERROR. The request exceeded the need."
                return msg, False, []
                break

        if done==m:
            for i in range(0, m):
                #### pretend allocation
                available_new[i] -= r[i]
                alloc_new[p][i] += r[i]
                need_new[p][i] -= r[i]
        done=0

        #print(f'need: {need}, available: {available}, request: {r}')
        if flag == 1:
            msg = "check safe"
            #print(msg)
            safety, sequence = safe(available_new, m, n, need_new,alloc_new)
            #print(safety)
            #print(sequence)
            return msg, safety, sequence



#########main##########


    #     ####inputs#####
    n=int(input("Please Enter number of Processes: "))
    m=int(input("Please Enter number of Resources: "))
    print(f'The system have {n} Processes and {m} Resources.')

    alloc=[]
    max=[]
    available=[]
    need=[]

    print("Please Enter the resource allocation matrix.")
    print("(enter all the resources of 1 process in 1 line separated by space)")
    for i in range(0, m):
        if i == 0:
            print("  ", end=" ")
        print(f' R{i}', end=" ")
    print(" ")
    for i in range(0, n):
        print(f'P{i}', end=" ")
        alloc.append(input().split(" "))
    print(" ")

    print("Please Enter the Max resources needed by each process.")
    print("(enter all the resources of 1 process in 1 line separated by space)")
    for i in range(0, m):
        if i == 0:
            print("  ", end=" ")
        print(f' R{i}', end=" ")
    print(" ")
    for i in range(0, n):
        print(f'P{i}', end=" ")
        max.append(input().split(" "))
    print(" ")

    print("Please Enter the Available resources in the system.")
    print("(enter all the resources in 1 line separated by space)")
    for i in range(0, m):
        print(f'R{i}', end=" ")
    print(" ")
    available=(input().split(" "))
    print(" ")


    #########change to int ######
    for i in range(0,n):
        for j in range(0,m):
            alloc[i][j]=int(alloc[i][j])
            max[i][j]=int(max[i][j])
    for i in range(0,m):
        available[i]=int(available[i])

    # available = [1, 5, 2, 0]
    # alloc = [[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
    # max = [[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]]
    # m = 4
    # n = 5

    # m = 3
    # n = 5
    # available = [3, 3, 2]
    # alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    # max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]

        #####need matrix####
    temp=[]
    need=[]
    print("The Need matrix is: ")
    for i in range(0,n):
        for j in range(0,m):
            x = max[i][j] - alloc[i][j]
            #print(f'{max[i][j]}-{alloc[i][j]}={x}')
            temp.append(x)

        need.append(temp)
        temp = []

    for i in range(0, m):
        if i == 0:
            print("  ", end=" ")
        print(f' R{i}', end=" ")
    print(" ")
    for i in range(0, n):
        print(f'P{i}', end=" ")
        for j in range(0, m):
            print(f'  {need[i][j]}', end=" ")
        print(" ")

    print(" ")
    #print(f'The Need matrix is: {need}')


##### safe or request enquiry #######
    press=0
    press2=1
    enter=0
    while press != 1 or press != 2 or press !=3 or enter==1:
        print("If you want: ")
        print("1- check for the safety of the system --> Press 1 ")
        print("2- check if immediate request by a process could be granted --> Press 2 ")
        print("3- If you want to exit --> Press 3 ")
        press=int(input())
        if press == 3:
            break
        safety=False
        r = []
        #sequence=[]
        if press==1:  ### safety algorithm ####
            enter=1
            safety,sequence=safe(available,m,n,need,alloc)
            if safety:
                print(f"Yes, it's a safe state. The safe sequence is: ", end=" ")
                print("<", end="")
                i=0
                for s in sequence:
                    if i == len(sequence)-1:
                        print(f' {s} ', end=" ")
                    else:
                        print(f' {s} ,', end=" ")
                    i+=1
                print(">")
                print(" ")
            elif not safety:
                print(f"No, it's not a safe state.")
                print(" ")
            enter=1
        elif press == 2:  ##### imediate request algorihm ####
            enter=1
            press2==1
            while 1:
                p = int(input("Please enter the number of the process that requests resources (0 for P0, 1 for P1 ... etc): "))
                print("Please enter your request: ")
                for i in range(0, m):
                    print(f'R{i}', end=" ")
                print(" ")
                r=(input().split(" "))
                for i in range(0, m):
                    r[i]=int(r[i])

                msg,safety,sequence=request(m,n,available,alloc,need,r,p)
                print(msg)

                if msg=="check safe":
                    if safety:
                        print(f"Yes, The request will be granted with a safe state.", end=" ")
                        print("The safe sequence:", end=" ")
                        print(f"< P{p} request, ", end="")
                        i = 0
                        for s in sequence:
                            if i == len(sequence) - 1:
                                print(f' {s} ', end=" ")
                            else:
                                print(f' {s} ,', end=" ")
                            i += 1
                        print(">")
                        print(" ")
                    elif not safety:
                        print(f"No, The request can't be granted. It's not a safe state.")
                    print(" ")
                print("If you want to check for another resource request for the same matrix --> press 1")
                print("If you want to exit resorce request --> press 2")
                press2=int(input())
                if press2==2:
                    break
                enter=1

        else:
            print("Please enter only 1 or 2 to be able to answer your enquiry.")




    print("If you want to enquiry for a new system --> press 0")
    print("If you want to exit --> press 1")
    press=int(input())
    if press==1:
        break