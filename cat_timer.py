import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageTk

# Default end time for the workday
END_HOUR = 18
END_MINUTE = 0

blink_state = 0
cat_images = []


def create_cat_image(blink=False):
    """Return a detailed pixel cat image.``blink`` toggles the eyes."""
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # tail
    draw.rectangle([48, 40, 60, 48], fill="gray")

    # body
    draw.rectangle([16, 32, 48, 56], fill="gray")
    draw.rectangle([24, 56, 40, 60], fill="gray")  # paws
    draw.rectangle([12, 28, 52, 32], fill="gray")  # neck

    # stripes on body
    for x in range(20, 44, 6):
        draw.rectangle([x, 40, x + 2, 52], fill="darkgray")

    # head
    draw.rectangle([16, 8, 48, 32], fill="gray")
    draw.polygon([(16, 8), (24, 0), (32, 8)], fill="gray")  # left ear
    draw.polygon([(48, 8), (40, 0), (32, 8)], fill="gray")  # right ear

    if blink:
        draw.rectangle([24, 16, 28, 18], fill="black")
        draw.rectangle([36, 16, 40, 18], fill="black")
    else:
        draw.rectangle([24, 16, 28, 20], fill="black")
        draw.rectangle([36, 16, 40, 20], fill="black")

    # muzzle
    draw.rectangle([30, 22, 34, 24], fill="pink")  # nose
    draw.line([(20, 22), (12, 22)], fill="black")  # whiskers
    draw.line([(44, 22), (52, 22)], fill="black")

    return ImageTk.PhotoImage(img)




def update_timer():
    global blink_state
    now = datetime.now()
    end_time = now.replace(hour=END_HOUR, minute=END_MINUTE, second=0, microsecond=0)
    if now > end_time:
        end_time += timedelta(days=1)
    remaining = end_time - now
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    blink_state = 1 - blink_state
    cat_label.config(image=cat_images[blink_state])
    root.after(1000, update_timer)


def set_end_time():
    """Apply values from entry widgets as new end-of-day time."""
    global END_HOUR, END_MINUTE
    try:
        h = int(hour_entry.get())
        m = int(min_entry.get())
    except ValueError:
        return
    if 0 <= h < 24 and 0 <= m < 60:
        END_HOUR = h
        END_MINUTE = m



root = tk.Tk()
root.title("Котиковый таймер")
root.geometry("350x300")
root.configure(bg="#FFB6C1")  # light pink

cat_images = [create_cat_image(False), create_cat_image(True)]

time_frame = tk.Frame(root, bg="#FFB6C1")
hour_entry = tk.Entry(time_frame, width=2)
hour_entry.insert(0, str(END_HOUR))
hour_entry.pack(side="left")
tk.Label(time_frame, text=":", bg="#FFB6C1").pack(side="left")
min_entry = tk.Entry(time_frame, width=2)
min_entry.insert(0, str(END_MINUTE))
min_entry.pack(side="left")
apply_btn = tk.Button(time_frame, text="Set", command=set_end_time)
apply_btn.pack(side="left", padx=5)
time_frame.pack(pady=5)
timer_label = tk.Label(
    root, text="", font=("Arial", 40, "bold"), bg="#FFB6C1", fg="#333333"
)
timer_label.pack(pady=10)


cat_label = tk.Label(root, image=cat_images[0], bg="#FFB6C1")
cat_label.pack(pady=5)

update_timer()
root.mainloop()
