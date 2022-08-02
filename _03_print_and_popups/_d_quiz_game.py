from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    Score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer=simpledialog.askstring("Question 1", " When did the Roman Civilization begin?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer =='753 BCE':
        Score+=1
        print(Score)
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer=simpledialog.askstring("Question 2", "Who was the greatest Roman Emperor?")
    if answer=="Augustus":
       Score+=1
       print(Score)
    answer=simpledialog.askstring("Question 3", "Why was the Roman Empire split into two in 200 BCE?")
    if answer=="It was too big to manage":
       Score+=2
       print(Score)
    answer=simpledialog.askstring("Question 4", "Who moved Rome's capital to  Byzantine when Rome was collasping?")
    if answer=="Emperor Constantine":
        Score+=3
        print(Score)
    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo("title",str(Score))
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()