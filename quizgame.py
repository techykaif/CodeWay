def quiz():
    global marks
    global total
    global correct
    global incorrect
    global answers
    global correctanswers
    global correctnum
    correctanswers=['DELHI','GOLD','CHARLES BABBAGE','CPU','STAR']
    correctnum=['1','2','3','3','4']
    answers=[]
    marks=0
    total=0
    correct=0
    incorrect=0
    global Name
    name=input("Enter Your Name : ")
    Name=name.upper()
    print("\nWhat's the Capital of India")
    print("1.Delhi\n2.Gujrat\n3.Lucknow\n4.Tamilnadu")
    answer=input("Enter Your Answer : ")
    answer=answer.upper()
    answers.append(answer)
    if(answer=="1" or answer=="DELHI" or answer=="delhi"):
        marks+=1
        total+=1
        correct+=1
        incorrect+=0
    else:
        marks+=0
        total+=1
        correct+=0
        incorrect+=1 
    print("\nWhich is the heavier metal of these two? Gold or Silver?")
    print("1.Silver\n2.Gold")
    answer=input("Enter Your Answer : ")
    answer=answer.upper()
    answers.append(answer)
    if(answer=="2" or answer=="GOLD" or answer=="gold"):
        marks+=1
        total+=1
        correct+=1
        incorrect+=0
    else:
        marks+=0
        total+=1
        correct+=0
        incorrect+=1
    print("\nWho invented Computer?")
    print("1.J.Frankley\n2.Ada Augusta\n3.Charles Babbage\n4.Tim Berner Lee")
    answer=input("Enter Your Answer : ")
    answer=answer.upper()
    answers.append(answer)
    if(answer=="3" or answer=="CHARLES BABBAGE" or answer=="charles babbage"):
        marks+=1
        total+=1
        correct+=1
        incorrect+=0
    else:
        marks+=0
        total+=1
        correct+=0
        incorrect+=1
    print("\nBrain of computer is?")
    print("1.Motherboard\n2.Power Supply\n3.CPU\n4.RAM")
    answer=input("Enter Your Answer : ")
    answer=answer.upper()
    answers.append(answer)
    if(answer=="3" or answer=="CPU" or answer=="cpu"):
        marks+=1
        total+=1
        correct+=1
        incorrect+=0
    else:
        marks+=0
        total+=1
        correct+=0
        incorrect+=1
    print("\nSun is a?")
    print("1.Celestial Body\n2.Solar Power\n3.Planet\n4.Star")
    answer=input("Enter Your Answer : ")
    answer=answer.upper()
    answers.append(answer)
    if(answer=="4" or answer=="STAR" or answer=="star"):
        marks+=1
        total+=1
        correct+=1
        incorrect+=0
    else:
        marks+=0
        total+=1
        correct+=0
        incorrect+=1
    print("*****************************Stats ****************************")
    print("\tName = ",name+"\n")
    print("\tTotal Marks = ",marks)
    print("\tTotal Questions = ",total)
    print("\tCorrect Answers = ",correct)
    print("\tIncorrect Answers = ",incorrect,end="\n")
    if marks==3:
        print("You Passed")
    elif marks==4:
        print("Wow Remarkable")
    elif marks==5:
        print("Wow Perfect Score")
    else:
        print("You Failed Need to Improve")
    checkAnswer = int(input("\nPress 1 to Match Answers or Press 2 to See the Answer Key :"))
    if(checkAnswer==1):
        print("\nEntered Responses are :\n")
        num=1
        for i in range(0,len(correctanswers)):
            if answers[i]==correctanswers[i] or answers[i]==correctnum[i]:
                print(num,". ",correctanswers[i],end="")
                print(" Correct Answer")
                num+=1
            else:
                print("Wrong Answer","Right Answer for Question ",end=" ")
                print(num,". is ",correctanswers[i])
                num+=1
    if(checkAnswer==2):
        print("Answer Key is :\n")
        num=1
        for j in correctanswers:
                print(num,". ",j)
                num+=1
quiz()