def createDictOfWords(fileName):
    specialSymbols =['#','*','http','@']
    digits =['0','1','2','3','4','5','6','7','8','9']
    symbols =['/',',','?','!','…','.','–','"',':','ffs','_','—','"','«','»',
              ';','-','+','-','_',')','(','=']
    words = ['в','про','и','за','из','но','к','на','c','как','что-то',
             'такая','кем','каков''по','без','от', 'со','перед','во',
             'еще','ну','то','или','бы','че','до','да','мы','ним','такую',
             'этот','такой','мое','нам','вас','о','у', 'они','этой','я',
             'над','для','а','если','же','даже', 'какие','также','чё','уже',
             'b','g','h','п','г','й','f','мой','это','это','что','моего',
             'меня','нас','наших','себя', 'она','всю','свой','всего','такому',
             'всем','вы','эти','ней','этом','себе','эту','тот','нашим','их',
             'такое','са','н','ар','d','д','рт','с','ег','наши','вам','мне',
             'вся','ваш','там','так','какая', 'какое','которые','тоже',
              'все','моему','какую','который','ктото','них', 'ещё','ни','a','по']
    with open(fileName, encoding='utf-8') as file:
      line = file.read()
      file.close()
    newLine=line.lower()
    tweetLines = (newLine).split()

   
    flag =1
    while(flag==1):
     flag=0
     for symbol in specialSymbols:
        for word in tweetLines:
           if symbol in word:
              flag=1
              tweetLines.remove(word)
    flag =1
    while(flag==1):
     flag=0
     for symbol in symbols:
        for i in range(len(tweetLines)):
            if symbol in tweetLines[i]:
               flag=1
               keyWord=tweetLines[i].replace(symbol,'')
               tweetLines[i]=keyWord
    flag =1
    while(flag==1):
     flag=0
     for digit in digits:
        for i in range(len(tweetLines)):
                if digit in tweetLines[i]:
                 flag=1
                 keyWord=tweetLines[i].replace(digit,'')
                 tweetLines[i]=keyWord
    flag =1
    while(flag==1):
     flag=0
     for w in words:
        for word in tweetLines:
           if w == word:
              flag=1
              tweetLines.remove(word)
    flag =1
    while(flag==1):
     flag=0
     for word in tweetLines:
          if len(word)==0:
                 tweetLines.remove(word)  
                 flag=1

    wordSet=set(tweetLines)
    wordDict = dict.fromkeys(wordSet)
    f = open('estimations.txt', 'w')
    f.close()
    f = open('estimations.txt', 'a')
    for key in   wordDict.keys(): f.write(str(key) + " : " + str(wordDict[key]) + "\n"); 
    f.close()


def createListOfTweets(fileName):
    with open(fileName, encoding='utf-8') as file:
      tweetLine = file.read()
      file.close()
      digits =['0','1','2','3','4','5','6','7','8','9']
      specialSymbols = ['#','*','@','https','ffs']
      symbols =['/',',','?','!','…','.','–','"',':','ffs','_','—','"','«','»',
              ';','-','+','-','_',')','(','=']
      words = ['в','про','и','за','из','но','к','на','c','как','что-то',
             'такая','кем','каков''по','без','от', 'со','перед','во',
             'еще','ну','то','или','бы','че','до','да','мы','ним','такую',
             'этот','такой','мое','нам','вас','о','у', 'они','этой','я',
             'над','для','а','если','же','даже', 'какие','также','чё','уже',
             'b','g','h','п','г','й','f','мой','это','это','что','моего',
             'меня','нас','наших','себя', 'она','всю','свой','всего','такому',
             'всем','вы','эти','ней','этом','себе','эту','тот','нашим','их',
             'такое','са','н','ар','d','д','рт','с','ег','наши','вам','мне',
             'вся','ваш','там','так','какая', 'какое','которые','тоже',
              'все','моему','какую','который','ктото','них', 'ещё','ни','a','по']
      newTweetLine =tweetLine.lower()
      tweetLines = newTweetLine.split('**********\n')
      newTweetLines =[]
      for i in range(len(tweetLines)): newTweetLines.append((tweetLines[i]).split())
 
    flag =1
    while(flag==1):
        flag=0
        for tweet in  newTweetLines:
          if (len(newTweetLines[newTweetLines.index(tweet)])<3):
              x=newTweetLines.index(tweet)
              del  newTweetLines[x]
              flag =1
     
    flag =1
    while(flag==1):
     flag=0
     for symbol in specialSymbols:
        for tweet in  newTweetLines:
         for j in tweet:
            if symbol in j:
                 flag=1
                 x=newTweetLines.index(tweet)
                 newTweetLines[x].remove(j)
    
    flag =1
    while(flag==1):
     flag=0
     for symbol in symbols:
        for i in range(len(newTweetLines)):
          for j in range(2,len( newTweetLines[i])):
                if symbol in newTweetLines[i][j]:
                     flag=1
                     newTweetLines[i][j]=newTweetLines[i][j].replace(symbol,'')

    flag =1
    while(flag==1):
     flag=0
     for word in words:
        for tweet in  newTweetLines:
         for j in tweet:
            if j== word:
                 flag=1
                 newTweetLines[newTweetLines.index(tweet)].remove(j)
    
    flag =True
    while(flag==True):
        flag=False
        for tweet in newTweetLines:
         for j in tweet:
            if len(j)==0:
                 flag=True
                 newTweetLines[newTweetLines.index(tweet)].remove(j)
    flag =1
    while(flag==1):
        flag=0
        for tweet in newTweetLines:
          if (len(newTweetLines[newTweetLines.index(tweet)])<3):
              x=newTweetLines.index(tweet)
              del  newTweetLines[x]
              flag =1
    #print(newTweetLines)
    return  newTweetLines

def createFileOfWordsFrequency():
    from collections import defaultdict
    f = open('frequency.txt', 'w')
    f.close()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)):
        print(i)
        str_parts = lines[i].split(" : ")
        wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    newTweetLines=createListOfTweets('tweets.txt')
    dictFrequency = defaultdict(float)
    for key in wordDict.keys():
        for tweet in newTweetLines:
         if key in tweet:
             dictFrequency[key]+=1
    f = open('frequency.txt', 'a')
    n= len(newTweetLines)
    for w in sorted(dictFrequency, key=dictFrequency.get, reverse = True):
            f.write(str(w) + ' - ' + str(dictFrequency[w]) + 
                    ' - '+ str(("{:.3}".format((dictFrequency[w]/n)*100))) +'%'+'\n')
    f.close()

def createClassificationOfTweetsPlot():
    from collections import defaultdict
    f = open("classifications.txt","w")
    f.close()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)):
        str_parts = lines[i].split(" : ")
        wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    f.close()
    tweetLines=createListOfTweets('tweets.txt')
    d = defaultdict(float)
    sum=0
    flag = 0
    for i in range(len(tweetLines)):
        for j in range(len(tweetLines[i])):
            dum=float(wordDict.get(tweetLines[i][j],0))
            if tweetLines[i][j]=='не':
                flag =1
                continue
            if flag==1:
                if dum==1:
                    sum+=-1
                elif dum==-1:
                    sum+=1
            else:
                sum+=dum
            flag = 0
        if(sum==0):
            d["neutral"]+=1
            tweetLines[i].insert(0,0)
        elif(sum>0):
            d["good"]+=1
            tweetLines[i].insert(0,1)
        else:
            d["bad"]+=1
            tweetLines[i].insert(0,-1)
        sum=0
    f = open("classifications.txt","a")
    f.write("Summ rule:\n")
    n=len(tweetLines)
    for w in d:
       f.write(str(w) + ' - ' + str(d[w])+ ' - '
               + str("{:.3}".format((d[w]/n)*100)) +'%'+'\n')
    flag=0
    d2 = defaultdict(float)
    for i in range(len(tweetLines)):
        for j in range(len(tweetLines[i])):
            good =0
            bad =0
            neutral=0
            dum=int(wordDict.get(tweetLines[i][j],8))
            if dum==8:
                flag=0
                continue
            if tweetLines[i][j]=='не':
                flag =1
                continue
            if flag==1:
                if dum==1:
                    bad+=1
                elif dum==-1:
                    good+=1
                else:
                    neutral+=1
            else:
                if dum==-1:
                    bad+=1
                elif dum==1:
                    good+=1
                else:
                    neutral+=1
            flag = 0
        if(bad>good and bad>neutral):
            d2["bad"]+=1
            tweetLines[i].insert(1,-1)
        elif(neutral>bad and neutral>good):
            d2["neutral"]+=1
            tweetLines[i].insert(1,0)
        else:
            d2["good"]+=1
            tweetLines[i].insert(1,1)
        summ=0
    f.write("\nProcent rule:\n")
    for w in d2:
       f.write(str(w) + ' - ' + str(d2[w])+ ' - '
               + str("{:.3}".format((d2[w]/n)*100)) +'%'+'\n')
    f.close()

    import pylab
    x1list =[]
    for w in d:
        x1list.append(w)
    y1list =[]
    for w in d:
        y1list.append(d[w]/len(tweetLines)*100)
    colors=['yellow','orange','red']
    pylab.bar(x1list,y1list,align='center',color=colors)
    pylab.title("Summ rule")
    pylab.ylabel("Procents")
    pylab.show()
    x2list =[]
    for w in d2:
        x2list.append(w)
    y2list =[]
    for w in d2:
        y2list.append(d2[w]/len(tweetLines)*100)
    colors=['yellow','orange','red']
    pylab.bar(x2list,y2list,align='center',color=colors)
    pylab.title("Procent rule")
    pylab.ylabel("Procents")
    pylab.show()

def createClassificationOfTweets():
    from collections import defaultdict
    f = open("classifications.txt","w")
    f.close()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)):
        str_parts = lines[i].split(" : ")
        wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    f.close()
    tweetLines=createListOfTweets('tweets.txt')
    d = defaultdict(float)
    sum=0
    flag = 0
    for i in range(len(tweetLines)):
        for j in range(len(tweetLines[i])):
            dum=float(wordDict.get(tweetLines[i][j],0))
            if tweetLines[i][j]=='не':
                flag =1
                continue
            if flag==1:
                if dum==1:
                    sum+=-1
                elif dum==-1:
                    sum+=1
            else:
                sum+=dum
            flag = 0
        if(sum==0):
            d["neutral"]+=1
            tweetLines[i].insert(0,0)
        elif(sum>0):
            d["good"]+=1
            tweetLines[i].insert(0,1)
        else:
            d["bad"]+=1
            tweetLines[i].insert(0,-1)
        sum=0
    f = open("classifications.txt","a")
    f.write("Summ rule:\n")
    n=len(tweetLines)
    for w in d:
       f.write(str(w) + ' - ' + str(d[w])+ ' - '
               + str("{:.3}".format((d[w]/n)*100)) +'%'+'\n')
    flag=0
    d2 = defaultdict(float)
    for i in range(len(tweetLines)):
        for j in range(len(tweetLines[i])):
            good =0
            bad =0
            neutral=0
            dum=int(wordDict.get(tweetLines[i][j],8))
            if dum==8:
                flag=0
                continue
            if tweetLines[i][j]=='не':
                flag =1
                continue
            if flag==1:
                if dum==1:
                    bad+=1
                elif dum==-1:
                    good+=1
                else:
                    neutral+=1
            else:
                if dum==-1:
                    bad+=1
                elif dum==1:
                    good+=1
                else:
                    neutral+=1
            flag = 0
        if(bad>good and bad>neutral):
            d2["bad"]+=1
            tweetLines[i].insert(1,-1)
        elif(neutral>bad and neutral>good):
            d2["neutral"]+=1
            tweetLines[i].insert(1,0)
        else:
            d2["good"]+=1
            tweetLines[i].insert(1,1)
        summ=0
    f.write("\nProcent rule:\n")
    for w in d2:
       f.write(str(w) + ' - ' + str(d2[w])+ ' - '
               + str("{:.3}".format((d2[w]/n)*100)) +'%'+'\n')
    f.close()
    return(tweetLines)

def createTopFiveAdj():
    import pymorphy2
    from collections import defaultdict
    morph = pymorphy2.MorphAnalyzer()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)-1):
         str_parts = lines[i].split(" : ")
         wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    f.close()
    d = defaultdict(float)
    tweetLines=createListOfTweets('tweets.txt')
    f=open("adjectives.txt","w")
    f.close()
    f=open("adjectives.txt","a")
    for key in wordDict.keys():
        for tweet in tweetLines:
         if key in tweet:
            p = morph.parse(key)[0]
            if (p.tag.POS=='ADJF'):
               if wordDict[key]=='1':
                d[str(p.normal_form)]+=1
    f.write("Top-5 Positive:\n")
    count=5
    for w in sorted(d, key=d.get, reverse = True):
       if count>0:
            f.write(str(w) + ' - ' + str(d[w]) + ' - '
                    + str(("{:.3}".format((d[w]/len(tweetLines))*100))) +'%'+'\n')
            count-=1
    d2 = defaultdict(float)
    for key in wordDict.keys():
        for tweet in tweetLines:
         if key in tweet:
            p = morph.parse(key)[0]
            if (p.tag.POS=='ADJF'):
               if wordDict[key]=='-1':
                d2[str(p.normal_form)]+=1
    f.write("\nTop-5 Negative:\n")
    count=5
    for w in sorted(d2, key=d2.get, reverse = True):
       if count>0:
            f.write(str(w) + ' - ' + str(d2[w]) + ' - '
                    + str(("{:.3}".format(d2[w]/len(tweetLines)*100))) +'%'+'\n')
            count-=1  
    import pylab
    count=5
    x1list=[]
    y1list=[]
    for w in sorted(d, key=d.get, reverse = True):
       if count>0:
           x1list.append(w)
           count-=1 
    count=5
    for w in sorted(d, key=d.get, reverse = True):
       if count>0:
           y1list.append(d[w])
           count-=1 
    colors=['orange','red','blue','green','violet']
    pylab.subplot(1,2,1)
    pylab.bar(x1list,y1list,align='center',color=colors)
    pylab.title("Top-5 Positive")
    pylab.ylabel("Number")
    count=5
    x2list=[]
    y2list=[]
    for w in sorted(d2, key=d2.get, reverse = True):
       if count>0:
           x2list.append(w)
           count-=1 
    count=5
    for w in sorted(d2, key=d2.get, reverse = True):
       if count>0:
           y2list.append(d2[w])
           count-=1 
    colors=['orange','red','blue','green','violet']
    pylab.subplot(1,2,2)
    pylab.bar(x2list,y2list,align='center',color=colors)
    pylab.title("Top-5 Negative")
    pylab.show()

def createHoursFile(numberOfRule):
    from datetime import datetime, date, time
    import pylab
    f =open("hours.txt","w")
    f.close()
    tweetLines=createClassificationOfTweets()
    timeList=[]
    for i in range(len(tweetLines)):
        dt=datetime.strptime(tweetLines[i][3],'%H:%M')
        timeList.append(dt)
    startTime=datetime.strptime('16:00','%H:%M')
    endTime=datetime.strptime('16:30','%H:%M')
   
    f=open("hours.txt","a")
    count =0
    badCount=0
    goodCount=0
    neutralCount=0
    xlist =[]
    y2list=[]
    badList=[]
    goodList=[]
    neutralList=[]
    timeListForPlot=[]
    while(endTime.hour!=21):
        for i in range(len(timeList)):
            if (timeList[i].hour==endTime.hour and timeList[i].minute<=endTime.minute) or (timeList[i].hour<endTime.hour):
                count+=1
                if tweetLines[i][numberOfRule-1]==0:
                    neutralCount+=1
                elif tweetLines[i][numberOfRule-1]==1:
                    goodCount+=1
                else:
                    badCount+=1
        if(len(str(endTime.minute)))==1:
            endTimeMinute='0'+str(endTime.minute)
        else:
            endTimeMinute=str(endTime.minute)
        xlist.append(str(endTime.hour)+":"+ endTimeMinute)
        y2list.append(count)
        List = list((str(goodCount)+','+str(badCount)+','+str(neutralCount)).split(','))
        timeListForPlot.append(List)       
        f.write(str(startTime.hour)+":"+str(startTime.minute)+'0'+
        ' - '+ str(endTime.hour)+":"+str(endTimeMinute)+" : "+str(count)+
        " " + str("{:.2}".format(goodCount/count))+"/"+ str("{:.2}".format(neutralCount/count))+'/'
        +str("{:.2}".format(badCount/count))+'\n')
        if endTime.minute==50:
            endTime=time(endTime.hour+1,00)
        else:
            endTime=time(endTime.hour,endTime.minute+10)
        count =0
        badCount=0
        goodCount=0
        neutralCount=0

    for time in timeListForPlot: 
        goodList.append(int(time[0]) / (int(time[0]) + int(time[1]) + int(time[2])))
    for time in timeListForPlot: 
        badList.append(int(time[1]) / (int(time[0]) + int(time[1]) + int(time[2])))
    for time in timeListForPlot: 
        neutralList.append(int(time[2]) / (int(time[0]) + int(time[1]) + int(time[2])))
    pylab.subplot(2,1,1)
    pylab.plot(xlist,goodList)
    pylab.plot(xlist,badList)
    pylab.plot(xlist,neutralList)
    pylab.subplot(2, 1, 1) 
    pylab.title('Distributes of tweets classes in time') 
    pylab.plot(xlist, [0.9 for i in range(len(xlist))], color='white') 
    pylab.plot(goodList, label='positive',color='red') 
    pylab.plot(neutralList, label='neutral',color='orange') 
    pylab.plot(badList, label='negative',color='green') 
    pylab.plot(goodList, 'o',color='red') 
    pylab.plot(neutralList, 'o',color='orange') 
    pylab.plot(badList, 'o',color='green') 
    pylab.ylabel('Fraction') 
    pylab.legend(loc=u'upper center', mode='expand', borderaxespad=0, ncol=3)
    pylab.grid()

    pylab.subplot(2,1,2)
    pylab.bar(xlist,y2list,align='center',width =0.1,color='grey')
    pylab.plot(xlist,y2list,'o',color='grey')
    pylab.xlabel("Time Window")
    pylab.ylabel("Number of tweets")
    pylab.grid()
    pylab.show()

def createEstimationCheckFile(numberOfRule):
    from collections import defaultdict
    import pylab
    tweetLines=createClassificationOfTweets()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)):
        str_parts = lines[i].split(" : ")
        wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    d = defaultdict(int)
    count =0
    for key in wordDict.keys():
        for i in range(len(tweetLines)):
            for j in range(len(tweetLines[i])):
                if key==tweetLines[i][j]:
                    d[key]+=int(tweetLines[i][numberOfRule-1])
                    count+=1
        if count!=0:
            d[key]=float(d[key]/count)
        count=0
    min=0.25
    dClosest=defaultdict(float)
    dFurthest=defaultdict(float)
    for key in wordDict.keys():
        for key2 in d.keys():
            if key==key2:
                if abs(float(wordDict[key])-float(d[key2]))<=(min):
                    dClosest[key]=abs(float(wordDict[key])-float(d[key2]))
                else:
                    dFurthest[key]=abs(float(wordDict[key])-float(d[key2]))
    f= open("estimation_check.txt",'w')
    f.close()
    f = open("estimation_check.txt",'a')
    f.write("Top-5 Closest:\n")
    count=5
    '''for w in dClosest:
       if count>0:
        if float(wordDict[w])-float(d[w])==0:
             f.write(str(w) + ' ' + str(wordDict[w]) + ' '+ str(("{:.3}".format(d[w])))+'\n')
             count-=1
       else:
           break'''
    for w in sorted(dClosest, key=dClosest.get):
       if count>0:
            f.write(str(w) + ' ' + str(wordDict[w]) + ' '+ str(("{:.3}".format(d[w])))+'\n')
            count-=1
       else:
           break
    f.write("\nTop-5 Furthest:\n")
    count=5
    for w in sorted(dFurthest, key=dFurthest.get, reverse = True):
       if count>0:
            f.write(str(w) + ' ' + str(wordDict[w]) + ' '+ str(("{:.3}".format(d[w])))+'\n')
            count-=1
       else:
           break
    sum=0
    for w in wordDict:
        sum+=abs(float(wordDict[w])-float(d[w]))
    estAccuracy= (1 -sum/len(wordDict))*100
    f.write("\nEstimation accuracy: "+ str("{:.3}".format(estAccuracy)) +"%"+'\n')
    f.close()
    x1list=[]
    y1list=[]
    count=5
    '''for w in dClosest:
       if count>0:
        if float(wordDict[w])-float(d[w])==0:
             x1list.append(w)
             count-=1
       else:
           break'''
    for w in sorted(dClosest, key=dClosest.get):
       if count>0:
            x1list.append(w)
            count-=1
       else:
           break
    count=5
    '''for w in dClosest:
       if count>0:
        if float(wordDict[w])-float(d[w])==0:
             y1list.append(abs(float(dClosest[w])))
             count-=1
       else:
           break'''
    for w in sorted(dClosest, key=dClosest.get):
       if count>0:
            y1list.append(abs(float(dClosest[w])))
            count-=1
       else:
           break
    colors=['red','orange','green','yellow','violet']
    pylab.subplot(1,2,1)
    pylab.bar(x1list,y1list,align='center',color=colors)
    pylab.title("Top-5 Closest")
    pylab.ylabel("Absolutely deviation")
   
    x2list=[]
    y2list=[]
    count=5
    for w in sorted(dFurthest, key=dFurthest.get, reverse = True):
       if count>0:
            x2list.append(w)
            count-=1
       else:
           break
    count=5
    for w in sorted(dFurthest, key=dFurthest.get, reverse = True):
       if count>0:
            y2list.append(abs(float(dFurthest[w])))
            count-=1
       else:
           break
    colors=['red','orange','green','yellow','violet']
    pylab.subplot(1,2,2)
    pylab.bar(x2list,y2list,align='center',color=colors)
    pylab.title("Top-5 Furthest")
    pylab.show()


def createBestWorstFile(numberOfRule):
    from collections import defaultdict
    d = defaultdict(float)
    tweetLines=createClassificationOfTweets()
    f=open('best_worst.txt','w')
    f.close()
    wordDict = {}
    f = open('estimations.txt', 'r')
    lines = f.readlines() 
    for i in range(len(lines)):
        str_parts = lines[i].split(" : ")
        wordDict[str_parts[0]]=(str(str_parts[1]).replace('\n',''))
    f = open('best_worst.txt','a')
    f.write('Top-5 Most Positive:\n')
    count =0
    for key in wordDict.keys():
        for i in range(len(tweetLines)):
            for j in range(len(tweetLines[i])):
                if key==tweetLines[i][j]:
                    d[key]+=float(tweetLines[i][numberOfRule-1])
                    count+=1
        if count==0:
                continue
        else:
            d[key]=float(d[key]/count)
        count=0
    count =5
    for w in sorted(d, key=d.get, reverse = True):
        if count>0:
            f.write(str(w) + ' '+str(d[w])+'\n')
        count-=1
    f.write('\nTop-5 Most Negative:\n')
    count =5
    for w in sorted(d, key=d.get):
        if count>0:
            f.write(str(w) + ' '+str(d[w])+'\n')
        count-=1
    import pylab
    count=5
    x=[]
    y=[]
    for w in sorted(d, key=d.get, reverse = True):
       if count>0:
           x.append(w)
           count-=1 
    count=5
    for w in sorted(d, key=d.get, reverse = True):
       if count>0:
           y.append(d[w])
           count-=1 
    colors=['red','orange','green','blue','violet']
    pylab.subplot(1,2,1)
    pylab.bar(x,y,align='center',color=colors)
    pylab.title("Top-5 Positive")
    pylab.ylabel("Value")
    count=5
    x2=[]
    y2=[]
    for w in sorted(d, key=d.get):
       if count>0:
           x2.append(w)
           count-=1 
    count=5
    for w in sorted(d, key=d.get):
       if count>0:
           y2.append(d[w])
           count-=1 
    colors=['red','orange','green','blue','violet']
    pylab.subplot(1,2,2)
    pylab.bar(x2,y2,align='center',color=colors)
    pylab.title("Top-5 Negative")
    pylab.show()



#createListOfTweets("tweets.txt")
#createFileOfWordsFrequency()
#createClassificationOfTweetsPlot()
#createTopFiveAdj()
#createHoursFile(1)
#createEstimationCheckFile(1)
#createDictOfWords("tweets.txt")
#createBestWorstFile(1)

