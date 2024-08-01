from tkinter import*
import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize game variables
playerX = "player 1"
playerY = "player 2"
playerX_score = playerY_score = loop_no = counter = 0
previous_playerX = previous_playerY = toggle = 1
position = 0
game = []
available = []
num = [3, 7, 11, 15]

# Create the main GUI window
root = tk.Tk()
root.title("LOLGame")
root.geometry("300x300")
root.configure(bg="pink")

frame1=Frame(root)
frame1.pack(pady=15)

label = Label(frame1, text="L O L", font=("TimesNewRoman", 16), bg="skyblue", fg="black")
label.pack()

# Create the game grid
grid_frame = tk.Frame(root)
grid_frame.pack()


def display():
    global game
    global grid_frame



    for i in range(16):
        if i in num:
            if game[i] == "L" or game[i] == "O":
                if i >= 9:
                    label = tk.Label(grid_frame, text=f"  {game[i]}  ",bg="blue",fg="white")
                else:
                    label = tk.Label(grid_frame, text=f"  {game[i]}  ",bg="blue",fg="white")
            else:
                if i >= 9:
                    label = tk.Label(grid_frame, text=f"  {game[i]}  ",bg="blue",fg="white")
                else:
                    label = tk.Label(grid_frame, text=f"  {game[i]}  ",bg="blue",fg="white")
        else:
            if game[i] == "L" or game[i] == "O":
                if i >= 9:
                    label = tk.Label(grid_frame, text=f"   {game[i]}   ",bg="blue",fg="white")
                else:
                    label = tk.Label(grid_frame, text=f"   {game[i]}   ",bg="blue",fg="white")
            else:
                if i >= 9:
                    label = tk.Label(grid_frame, text=f"  {game[i]}  ",bg="blue",fg="white")
                else:
                    label = tk.Label(grid_frame, text=f"   {game[i]}  ",bg="blue",fg="white")
        label.grid(row=i // 4, column=i % 4, padx=5, pady=5)



def inputa():
    global position
    global available

    # Prompt for player input
    if toggle == 1:
        player = playerX
    else:
        player = playerY

    value = messagebox.askquestion("Enter Value", f"{player}, choose 'Yes' for 'L' and 'No' for 'O'")
    position = simpledialog.askinteger("Enter Position", "Enter a number between 1 and 16")
    
    if available[position - 1] == 0:
        messagebox.showwarning("Warning", "This position is already assigned. Please choose another position.")
        inputa()
    else:
        write(value)


def switch_player():
    global toggle
    global playerX_score
    global playerY_score
    global previous_playerX
    global previous_playerY
    global loop_no
    
    

    if loop_no == 0:
        return f">>>>>> next player turn >>>>>>>"
    else:
        if toggle == 1:
            if playerX_score > previous_playerX:
                toggle = 2
                return f">>>>>> next player turn >>>>>>>"
            else:
                toggle = 1
                return f">>>>>> next player turn >>>>>>>"
        elif toggle == 2:
            if playerY_score > previous_playerY:
                toggle = 1
                return f">>>>>> next player turn >>>>>>>"
            else:
                toggle = 2
                return f">>>>>>next player turn >>>>>>>"



def write(value):
    global position
    global game
    global available

    game[position - 1] = "L" if value == "yes" else "O"
    available[position - 1] = 0
    display()
    judge()
    inputa()  # Prompt the next player for input

def judge():
    global position
    global playerX_score
    global playerY_score
    global previous_playerX
    global previous_playerY
    global game

    Z = position - 1;
    previous_playerY = playerY_score
    previous_playerX = playerX_score

    if game[Z] == "O":
        look = "L"
        if position != 16 and game[Z - 1] == game[Z + 1]:
            if game[Z - 1] == look and position % 4 != 0:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1

        elif position <= (len(game) - 4) and game[Z + 4] == game[Z - 4]:
            if game[Z - 4] == look:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1

        elif position < (len(game) - 4) and position > 5 and game[Z + 5] == game[Z - 5]:
            if game[Z - 5] == look and position % 4 != 0:
                if (position - 5) % 4 != 0:
                    if toggle == 1:
                        playerX_score += 1
                    else:
                        playerY_score += 1

        elif position < 12 and game[Z + 3] == game[Z - 3]:
            if game[Z - 3] == look and position % 4 != 0:
                if (position + 3) % 4 != 0:
                    if toggle == 1:
                        playerX_score += 1
                    else:
                        playerY_score += 1

    elif game[Z] == "L":
        if position <= (len(game) - 2) and game[Z + 1] == "O" and game[Z + 2] == "L":
            if (position + 1) % 4 != 0 and position % 4 != 0:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1

        elif position >= 3 and game[Z - 1] == "O" and game[Z - 2] == "L":
            if (position - 1) % 4 != 0 and (position - 2) % 4 != 0:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1

        elif position <= (len(game) - 8) and game[Z + 4] == "O" and game[Z + 8] == "L":
            if toggle == 1:
                playerX_score += 1
            else:
                playerY_score += 1

        elif position > (len(game) - 8) and game[Z - 4] == "O" and game[Z - 8] == "L":
            if toggle == 1:
                playerX_score += 1
            else:
                playerY_score += 1
        elif(position <= 6 and position and game[Z+5] ==  "O" and game[Z+10] ==  "L" and (position+5)%4 !=0 and position%4 != 0):
            if(toggle == 1):
               playerX_score+=1
            else:
               playerY_score+=1
    
        elif(position > (len(game)-8) and game[Z-5] ==  "O" and game[Z-10] ==  "L" and (position-5)%4 !=0 and (position-10)%4 !=0 ):
            if(toggle == 1):
               playerX_score+=1
            else:
               playerY_score+=1
        elif position <= 8 and game[Z + 3] == "O" and game[Z + 6] == "L":
            if (position + 3) % 4 != 0:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1

        elif position > 8 and game[Z - 3] == "O" and game[Z - 6] == "L":
            if (position - 3) % 4 != 0:
                if toggle == 1:
                    playerX_score += 1
                else:
                    playerY_score += 1
        else:
                playerX_score=playerX_score
                playerY_score=playerY_score
                messagebox.showinfo("P1 S: "+str(playerX_score)+"\n")
                messagebox.showinfo("P2 S: "+str(playerY_score)+"\n")
                

    loop()

def loop():
    global loop_no
    global counter
    global toggle

    counter += 1

    if counter == 16:
        result = f"{playerX}'s score: {playerX_score}\n{playerY}'s score: {playerY_score}"
        if playerX_score > playerY_score:
            result += f"\n{playerX} wins!"
        elif playerY_score > playerX_score:
            result += f"\n{playerY} wins!"
        else:
            result += "\nIt's a tie!"

        messagebox.showinfo("Game Over", result)

        reset_game()

    loop_no += 1
    toggle = 1 - toggle  # Switch players

    result = switch_player()

    messagebox.showinfo("Next Turn", result)


# Reset the game
def reset_game():
    global playerX_score
    global playerY_score
    global loop_no
    global counter
    global previous_playerX
    global previous_playerY
    global toggle
    global position
    global game
    global available

    playerX_score = playerY_score = loop_no = counter = 0
    previous_playerX = previous_playerY = toggle = 1
    position = 0
    game = []
    available = []

    for i in range(16):
        game.append(" ")
        available.append(1)

    display()

# Initialize the game grid
for i in range(16):
    game.append(" ")
    available.append(1)

display()

# Start the game
inputa()

# Add a loop to keep the game running until the user closes the window
root.mainloop()
