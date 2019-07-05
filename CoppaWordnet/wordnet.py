from nltk.corpus import wordnet

#contains all the important words needed for matching
checklist = [
    ['personal','information','deceptive','disclosure'],
    ['operators', 'third', 'parties'],
    ['personal', 'information', 'practises'],
    ['parental'],
    ['parental'],
    ['link', 'notice', 'online'],
    ['security', 'confidentiality', 'integrity'],
    ['retention', 'deletion'],
    ['request', 'contact'],
    ['game', 'contest']
]

#filenames of all input and output files 
filenames = ['pp1-ip.txt','pp2-ip.txt','pp3-ip.txt','pp4-ip.txt','pp5-ip.txt']
opFileNames = ['pp1-op.txt','pp2-op.txt','pp3-op.txt','pp4-op.txt','pp5-op.txt']

for i in range(len(filenames)):
    f = open(opFileNames[i], "a")
    with open(filenames[i]) as fp: 
        lineCnt = 0
        checklistSet = set() #holds the checklist for each file to calculate accuracy
        for line in fp:
            lineCheckSet = set()
            lineCnt +=1
            checklistCnt=0
            foundAny = 0
            for checklistCnt in range(len(checklist)):
                foundCheck =0
                for word in (checklist[checklistCnt]):
                    synonyms = [] #synonyms will have all the synonyms of my word

                    #extracting all synonyms 
                    for syn in wordnet.synsets(word):
                        for l in syn.lemmas():
                            synonyms.append(l.name())
                        
                    # check if the word matches in the line, if matches break and go for next checklist
                    for syno in synonyms:
                        if syno in line:
                            checklistSet.add(checklistCnt+1)
                            currCheckCnt = str(checklistCnt+1)
                            lineCheckSet.add(currCheckCnt)
                            #strline = "<<"+ currCheckCnt+">>"+line
                            #f.write(strline)
                            foundCheck = 1
                            foundAny = 1
                            break # dont check the remaining synonyms 
                    if foundCheck == 1:
                        break # dont check any other words / synonyms of it in the checklist, as checklist is already found 
            if foundAny == 0:
                f.write(line)
            else:
                strline = "<<"
                for char in lineCheckSet:
                    strline += char+" "
                strline = strline+">>"+line
                f.write(strline)
            
    f.close()
    print ("File ",i," Checklists found ", checklistSet)

