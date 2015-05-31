import tkinter as tk
from tkinter import *
from operator import itemgetter
import csv


class ListOfEvents(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.var = IntVar()
        self.var2 = IntVar()
        self.var.set(0)
        self.var2.set(1)
        self.new_value = None
        self.pack()
        self.events = []
        self.new = tk.Button(self, text="NEW EVENT", bg="black", fg="white", command=self.new_event, width='25')
        self.delete = tk.Button(self, text="DELETE EVENT", bg="black", fg="white", command=self.delete_event, width='25')
        self.prints = tk.Button(self, text="PRINT SCHEDULE", bg="black", fg="white", command=self.print_schedule, width='25')
        self.edit = tk.Button(self, text="EDIT EVENT", bg="black", fg="white", command=self.edit_event, width='25')
        self.create_widgets()

    def create_widgets(self):
        self.new.pack()
        self.delete.pack()
        self.edit.pack()
        self.prints.pack()

    def new_event(self):
        print("NEW EVENT")
        NewEventMenu(tk.Toplevel(self.master))
        return

    def delete_event(self):
        print("DELETE EVENT")
        self.delete_window = tk.Toplevel(self.master)
        Label(self.delete_window, text="Select event to delete and click done:").grid(row=0)
        i = 0
        rb = []
        for x in self.events:
            if x[1] < 10:
                rb.append(Radiobutton(self.delete_window, text=str(x[0])+":0"+str(x[1])+", "+x[2], variable=self.var, value=i))
            else:
                rb.append(Radiobutton(self.delete_window, text=str(x[0])+":"+str(x[1])+", "+x[2], variable=self.var, value=i))
            rb[i].grid(row=i+1, sticky=W)
            i += 1
        Button(self.delete_window, text="DONE", command=self.del_exit).grid(row=i+1)
        return

    def del_exit(self):
        app.events.pop(self.var.get())
        with open("DailyPlanner.txt", 'w', newline='') as csv_file:
                    temp2 = csv.writer(csv_file, delimiter=',')
                    for x in app.events:
                        temp2.writerow(x)
        self.delete_window.destroy()
        return

    def print_schedule(self):
        print("PRINT SCHEDULE")
        schedule_window = tk.Toplevel(self.master)
        Label(schedule_window, text="Your Daily Schedule is: ").grid(row=0)
        Label(schedule_window, text="Time").grid(row=1, column=0)
        Label(schedule_window, text="Memo").grid(row=1, column=1)
        i = 2
        for x in app.events:
            if x[1] < 10:
                Label(schedule_window, text=str(x[0])+':'+'0'+str(x[1])).grid(row=i, column=0)
            else:
                Label(schedule_window, text=str(x[0])+':'+str(x[1])).grid(row=i, column=0)
            Label(schedule_window, text=x[2]).grid(row=i, column=1)
            i += 1
        return

    def edit_event(self):
        print("EDIT EVENT")
        self.edit_window = tk.Toplevel(self.master)
        Label(self.edit_window, text="Select an event to edit: ").grid(row=0)
        i = 0
        rb = []
        for x in self.events:
            if x[1] < 10:
                rb.append(Radiobutton(self.edit_window, text=str(x[0])+":0"+str(x[1])+", "+x[2], variable=self.var, value=i))
            else:
                rb.append(Radiobutton(self.edit_window, text=str(x[0])+":"+str(x[1])+", "+x[2], variable=self.var, value=i))
            rb[i].grid(row=i+1, sticky=W)
            i += 1
        Label(self.edit_window, text="Also select an attribute: ").grid(row=i+1)
        Button(self.edit_window, text="DONE", command=self.edit_exit).grid(row=i+5)
        Radiobutton(self.edit_window, text="Edit Hour", variable=self.var2, value=0).grid(row=i+2, sticky=W)
        Radiobutton(self.edit_window, text="Edit Minute", variable=self.var2, value=1).grid(row=i+3, sticky=W)
        Radiobutton(self.edit_window, text="Edit Memo", variable=self.var2, value=2).grid(row=i+4, sticky=W)
        return

    def edit_exit(self):
        self.edit_window2 = tk.Toplevel(self.master)
        j = [["hour", 23], ["minute", 59], ["memo", ]]
        Label(self.edit_window2, text="Please input new value for "+str(j[self.var2.get()][0])+": ").grid(row=0)
        if app.events[self.var.get()][1] < 10:
            Label(self.edit_window2, text="for this event:    "+str(app.events[self.var.get()][0])+":0"+str(app.events[self.var.get()][1])+", "+app.events[self.var.get()][2]).grid(row=1)
        else:
            Label(self.edit_window2, text="for this event:    "+str(app.events[self.var.get()][0])+":"+str(app.events[self.var.get()][1])+", "+app.events[self.var.get()][2]).grid(row=1)
        if self.var2.get() == 2:
            self.new_value = Entry(self.edit_window2)
        elif self.var2.get() == 1:
            self.new_value = Spinbox(self.edit_window2, from_=0, to=59, wrap=True, width=2)
        else:
            self.new_value = Spinbox(self.edit_window2, from_=0, to=23, wrap=True, width=2)
        self.new_value.grid(row=2)
        Button(self.edit_window2, text="DONE", command=self.edit_exit2).grid(row=3)
        return

    def edit_exit2(self):
        print(self.var.get())
        print(self.var2.get())
        print(self.new_value.get())
        if self.var2.get() == 2:
            app.events[self.var.get()][self.var2.get()] = self.new_value.get()
        elif self.var2.get() == 1:
            try:
                if not int(self.new_value.get()) in range(0, 60):
                    print("minute error")
                else:
                    app.events[self.var.get()][self.var2.get()] = int(self.new_value.get())
                    sorted_list = sorted(app.events, key=itemgetter(0, 1))
                    app.events = sorted_list
                    with open("DailyPlanner.txt", 'w', newline='') as csv_file3:
                        temp1 = csv.writer(csv_file3, delimiter=',')
                        for x in app.events:
                            temp1.writerow(x)
            except ValueError:
                print("please input a number")
        elif self.var2.get() == 0:
            try:
                if not int(self.new_value.get()) in range(0, 24):
                    print("hour error")
                else:
                    app.events[self.var.get()][self.var2.get()] = int(self.new_value.get())
                    sorted_list = sorted(app.events, key=itemgetter(0, 1))
                    app.events = sorted_list
            except ValueError:
                print("please input a number")
        with open("DailyPlanner.txt", 'w', newline='') as csv_file2:
                    temp2 = csv.writer(csv_file2, delimiter=',')
                    for x in app.events:
                        temp2.writerow(x)
        self.edit_window2.destroy()
        self.edit_window.destroy()
        return


class NewEventMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.hour = Spinbox(master, from_=0, to=23, wrap=True, width=2)
        self.minute = Spinbox(master, from_=0, to=59, wrap=True, width=2)
        self.name = Entry(master)
        Button(master, text="DONE", command=self.quit).grid(row=4, column=0)
        Label(master, text="When is your appointment (0:00 - 23:59): ").grid(row=0, column=0)
        Label(master, text="Label your appointment: ").grid(row=2, column=0)
        Label(master, text=":").grid(row=0, column=2)
        self.name.grid(row=3, column=0)
        self.minute.grid(row=0, column=3)
        self.hour.grid(row=0, column=1)

    def quit(self):
        try:
            if not int(self.hour.get()) in range(0, 24):
                print("hour error")
            elif not int(self.minute.get()) in range(0, 60):
                print("minute error")
            else:
                app.events.append([int(self.hour.get()), int(self.minute.get()), self.name.get()])
                sorted_list = sorted(app.events, key=itemgetter(0, 1))
                app.events = sorted_list
                with open("DailyPlanner.txt", 'w', newline='') as csv_file3:
                    temp1 = csv.writer(csv_file3, delimiter=',')
                    for x in app.events:
                        temp1.writerow(x)
        except ValueError:
            print("please input a number")
        self.master.destroy()
        return


if __name__ == "__main__":
    root = tk.Tk()
    app = ListOfEvents(master=root)
    with open("DailyPlanner.txt", 'r') as csvfile:
            temp = csv.reader(csvfile, delimiter=',')
            try:
                for row in temp:
                    currow = [int(row[0]), int(row[1]), str(row[2])]
                    app.events.append(currow)
            except ValueError:
                print("COULD NOT OPEN DAILYPLANNER.TXT")
    app.mainloop()