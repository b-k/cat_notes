#! python

# Set the topics you want to work on here. This part made more sense when this was
# embedded in a clone of https://github.com/jasonu/flashcards
Files=["category-theory"]

import subprocess

def go(dothis):
    print(dothis)
    return subprocess.getoutput(dothis)

go("xelatex cat_cards")

Count=go("egrep '(\\\\[Cc]ard|begin.flashcard)' " + " cat_cards.tex | wc -l")
Count=int(Count)-1 #strip the first copyright/attribution card
print("--------------------\n\t"+str(Count)+" cards.\n--------------------")

go("rm counts; for i in `seq 1 2 " + str(2*Count-2) + "`; do echo $i >> counts; done")
Pages=go("shuf counts | awk '{print $1 \",\" $1+1}'| tr '\n' ','|sed 's/,$//'")

go("rm -f mid.pdf mid1.pdf")
go("pdfjam cat_cards.pdf 3- -o mid1.pdf")
go("pdfjam mid1.pdf \"" + Pages + "\" --no-tidy -o mid.pdf")
go("pdfcrop --clip mid.pdf cards.pdf")
