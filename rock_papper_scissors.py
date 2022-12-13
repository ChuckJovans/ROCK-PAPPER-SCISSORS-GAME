from tkinter import*
from PIL import Image,ImageTk
from random import randint
import pygame

# The Main Window
root = Tk()

# Window Title
root.title("Rock Papper Scissors By BOB BELLS KATUMBIRE")
# Window Background
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
papper_img = ImageTk.PhotoImage(Image.open("papper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
papper_img_comp = ImageTk.PhotoImage(Image.open("papper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture  setting the pics to grid
user_label = Label(root,image=scissors_img, bg="#9b59b6")
comp_label = Label(root,image=scissors_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#insert the scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicator
user_indicator = Label(root, font=50,text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50,text="COMPUTER" , bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

#messages
msg = Label(root, font=50, bg="#9b59b6")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg["text"] = x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score +=1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score +=1
    computerScore["text"] = str(score)

#check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a Tie!!")
    elif player == "rock":
        if computer == "papper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    elif player == "papper":
        if computer == "scissors":
            updateMessage("You loose")
            updateCompScore() 
        else:
            updateMessage("You win")
            updateUserScore() 
    elif player == "scissors":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You win")
            updateUserScore()
    else:
        pass



#update choices 
choices = ["rock","papper","scissors"]
def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "papper":
        comp_label.configure(image=papper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)

#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="papper":
        user_label.configure(image=papper_img)
    else:
        user_label.configure(image=scissors_img)
    
    checkWin(x, compChoice)

#buttons
rock= Button(root,width=20, height=2, text="Rock", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2,column=1)
papper= Button(root,width=20, height=2, text="Papper", bg="#FAD02E", fg="white", command=lambda: updateChoice("papper")).grid(row=2,column=2)
scissors= Button(root,width=20, height=2, text="Scissors", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissors")).grid(row=2,column=3)


root.mainloop()
