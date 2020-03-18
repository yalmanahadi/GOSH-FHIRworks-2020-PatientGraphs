import random
import matplotlib
from fhir_parser import FHIR
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class PatientGraphs:
    def __init__(self, master):
        self.fhir = FHIR()
        self.all_patients = self.fhir.get_all_patients()
        self.same_name_patients = []
        self.master = master
        master.title("Patient Graphs")

        self.patient_first_name = None
        self.patient_last_name = None
        self.same_name_patients = []

        self.message = "Search for a patient..."
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master)#, validate="key", validatecommand=(vcmd, '%P'))

        self.search_button = Button(master, text="Search Patient", command=self.get_patient)
        self.hr_button = Button(master, text="Heart Rate Graph", command=self.reset, state=DISABLED)
        self.bp_button = Button(master, text="Blood Pressure Graph", command=self.reset, state=DISABLED)


        self.label.grid(row=0, column=0, columnspan=3, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.search_button.grid(row=2, column=0)
        self.hr_button.grid(row=2, column=1)
        self.bp_button.grid(row=2, column=2)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False

    def get_patient(self):
        if (len(self.entry.get()) == 0):
            return
        else:
            name = self.entry.get()
        for patient in self.all_patients:
            if name in patient.full_name():
                self.same_name_patients.append(patient.uuid)
                print(patient.full_name())
        # if self.message is None:
        #     self.message = "Guess a number from 1 to 100"

        # elif self.guess == self.secret_number:
        #     suffix = '' if self.num_guesses == 1 else 'es'
        #     self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
        #     self.guess_button.configure(state=DISABLED)
        #     self.reset_button.configure(state=NORMAL)

        # elif self.guess < self.secret_number:
        #     self.message = "Too low! Guess again!"
        # else:
        #     self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = PatientGraphs(root)
root.mainloop()
