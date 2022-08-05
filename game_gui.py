from PIL import Image, ImageTk
import tkinter

window = tkinter.Tk()
window.title('Connect Four')
window.geometry('1280x960')
window.resizable(0, 0)
board_state = []
c = tkinter.Canvas(window, width=700, height=700)


def click_event(event):
    print(event)
    idx = event.x // 100
    c.itemconfig(board_state[idx][6], fill='green')
    print(board_state)


c.bind('<Button-1>', click_event)
c.pack()


def change():
    image = Image.open("Untitled.png")
    yellow_piece = ImageTk.PhotoImage(image)
    c.itemconfig(board_state[0][0], fill="yellow")
    c.itemconfig(board_state[0][1], fill='green')
    #coords = c.coords(board_state[0][0])
    #x, y = (coords[0] + coords[2])/2, (coords[1] + coords[3])/2
    #c.delete(board_state[0][0])
    #c.create_oval(coords[0], coords[1], coords[2], coords[3], fill = "green" )


for i in range(0, 700, 100):
    column = []
    for k in range(0, 700, 100):
        column.append(c.create_oval(i, k, i+100, k+100, fill=""))
    board_state.append(column)

print(board_state)
tkinter.Button(window, text="Click", command=change).pack()


window.mainloop()
