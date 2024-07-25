# appointment_handler.py
import datetime
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import simpledialog

class Appointment:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def display_appointment(self):
        print(f"Appointment Date: {self.date}, Time: {self.time}")

def get_appointment():
    # Create a simple GUI for date selection
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    date_str = simpledialog.askstring("Input", "Enter appointment date (YYYY-MM-DD):")
    time_str = simpledialog.askstring("Input", "Enter appointment time (HH:MM):")
    
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        time = datetime.datetime.strptime(time_str, "%H:%M").time()
        if date < datetime.date.today() or date > datetime.date.today() + datetime.timedelta(days=365):
            raise ValueError("Date must be within the next year.")
        return Appointment(date, time)
    except ValueError as e:
        print(f"Invalid date or time format: {e}. Please try again.")
        return None
