import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageTk

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


def create_cat_image():
    """Return a tkinter-compatible pixel cat image."""
    size = 32
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # head
    draw.rectangle([8, 10, 24, 25], fill="gray")
    # ears
    draw.polygon([(8, 10), (12, 2), (16, 10)], fill="gray")
    draw.polygon([(24, 10), (20, 2), (16, 10)], fill="gray")
    # eyes
    draw.rectangle([12, 16, 14, 18], fill="black")
    draw.rectangle([18, 16, 20, 18], fill="black")
    # nose
    draw.rectangle([15, 20, 17, 22], fill="pink")

    return ImageTk.PhotoImage(img)


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

# Cute pixel cat image
cat_image = create_cat_image()
cat_label = tk.Label(root, image=cat_image, bg="yellow")
cat_label.pack(pady=5)

update_timer()
root.mainloop()
