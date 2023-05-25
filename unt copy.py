#Basically, in order to use this code, all you have to do is run it in the terminal as the command "python unt.py" and then enter the name of the tex file which has to be 
#in the same directory as this file 


print("\n\nBibSort_v1\nSorts LaTeX 'thebibliography' in order of first citation in text\nDave Williams 26Mar2017\nRun the code in the same directory as your LaTeX source file\nUsing Python 2.x")
filename = input("\n\nEnter LaTeX source filename (e.g. 'input.tex'): ")
fileobject = (open(filename, 'r'))
rawtext = fileobject.read()
fileobject.close()
start = '\\begin{document}'
end = '\\begin{thebibliography}'
bodytext = rawtext[rawtext.find(start)+len(start):rawtext.rfind(end)]
start = '\\begin{thebibliography}'
end = '\\end{thebibliography}'
bibliography = rawtext[rawtext.find(start)+len(start):rawtext.rfind(end)]
authorlist = []
for char in range(0,len(bodytext) - 10):
    if bodytext[char:char+6] == '\\cite{':
        author = ''
        char +=6
        while (bodytext[char] != '}'):
            if (bodytext[char] == ' '):
                char+=1
            elif(bodytext[char] == ','):
                char +=1 
                if author in authorlist:
                    author = ''
                else:
                    authorlist.append(author)
                    author=''
            else:
                author += (bodytext[char])
                char +=1    
        if author in authorlist:
            pass
        else:
            authorlist.append(author) 

labellist = []
reflist = []
for char in range(0,len(bibliography) - 7):
    ref =''
    if bibliography[char:char+9] == '\\bibitem{':
        char+=9
        label =''
        while(bibliography[char] != '}'): 
            label += bibliography[char] 
            char+=1 
        labellist.append(label)
        char+=1
        while (bibliography[char:char+9] != '\\bibitem{'):
            if char == len(bibliography) -1:
                break
            elif (bibliography[char]) == '\n':
                char +=1
            else:
                ref += (bibliography[char])
                char +=1
        reflist.append(ref) 

dictionary = dict(list(zip(labellist, reflist)))
output =''
orphanlist =''
try:
    for name in authorlist:
        output += '\\bibitem{' + name + '}\n' + dictionary[name] + '\n\n'
    if len(authorlist) < len(labellist):
        output+="%" + "-"*80 + "\n"
        output+= "%"+ " The following %d references are in thebibliography but not cited in the text:\n\n" % (len(reflist) - len(authorlist)) 
        orphanlist = list(set(labellist)-set(authorlist))
        for name in range(0, len(orphanlist)-1):
            output += '\\bibitem{' + orphanlist[name] + '}\n' + dictionary[orphanlist[name]] + '\n\n'
    print(("\n\n%d unique references were found in the text and sorted in order of appearance in the text" % (len(authorlist))))
    print(("%d additional references were found in \\thebibliography which were not used in the text" % (len(orphanlist))))
    print(("\nNew bibliography saved as:\n%s\n\nUsing a text editor, Copy all contents of this file,\nand Paste over the existing mybibliography in your LaTeX source file:\n%s\n" % (filename[:-4]+'_NewBib.txt',filename)))
    fileobject = open(filename[:-4]+'_NewBib.txt', 'w')
    fileobject.write(output)
    fileobject.close
except (TypeError, ValueError) as e:
    print(e)
    print("\nThere may be a mis-match between the labels in your bibliography\n and one or more labels in your in-text citations.\nPerhaps there is a typo, or you've used a capital letter in one\nbut not the other.\nPlease check your the flagged citation using 'find' in your\n Latex editor and run this Python script again.")