from tkinter import *
import settings

root = Tk()

root.title("ACC Fuel Calculator")
root.configure(bg="black")
root.geometry(f'{settings.FRAME_WIDTH}x{settings.FRAME_HEIGHT}')
root.resizable(False, False)

main_frame = Frame(
    root,
    bg="blue",
    width= settings.FRAME_WIDTH,
    height= settings.FRAME_HEIGHT
)
main_frame.place(x=0, y=0)

time_label = Label(main_frame, text="Race length")
time_in = Entry(main_frame)

lap_time_label = Label(main_frame, text="Lap Time")
lap_Time_in = Entry(main_frame)

fuel_per_lap_label = Label(main_frame, text="Fuel per Lap")
fuel_per_lap_in = Entry(main_frame)

time_label.grid(row=0, sticky=EW, padx=5, pady=5,ipady=5, ipadx=15)
time_in.grid(row=1, sticky=EW, padx=5, pady=5)
lap_time_label.grid(row=2, sticky=EW, padx=5, pady=5,ipady=5, ipadx=15)
lap_Time_in.grid(row=3, sticky=EW, padx=5, pady=5,ipady=5, ipadx=15)
fuel_per_lap_label.grid(row=4, sticky=EW, padx=5, pady=5,ipady=5, ipadx=15)
fuel_per_lap_in.grid(row=5, sticky=EW, padx=5, pady=5)

Button(main_frame, text="Calculate", command=main_frame).grid(row=6,column=0, sticky=W, pady=0)
Button(main_frame, text='Quit', command=root.quit).grid(row=6, column=0,  sticky=E, pady=4)

#run window
root.mainloop()