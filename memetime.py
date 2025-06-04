import tkinter as tk
from datetime import datetime, timedelta

# End of workday (24-hour format)
END_HOUR = 17
END_MINUTE = 0


def update_timer():
    now = datetime.now()
    end_time = now.replace(hour=END_HOUR, minute=END_MINUTE, second=0, microsecond=0)
    if now > end_time:
        # If we've passed the end time, assume next day
        end_time += timedelta(days=1)
    remaining = end_time - now
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    root.after(1000, update_timer)


root = tk.Tk()
root.title("Мемный таймер до конца рабочего дня")
root.geometry("450x250")
root.configure(bg="yellow")

meme_label = tk.Label(root, text="HANG IN THERE", font=("Comic Sans MS", 16, "bold"), bg="yellow", fg="red")
meme_label.pack(pady=10)

timer_label = tk.Label(root, text="", font=("Comic Sans MS", 40, "bold"), bg="yellow", fg="blue")
timer_label.pack(pady=10)

sub_label = tk.Label(root, text="¯\\_(ツ)_/¯", font=("Comic Sans MS", 20), bg="yellow", fg="green")
sub_label.pack(pady=10)

update_timer()
root.mainloop()
