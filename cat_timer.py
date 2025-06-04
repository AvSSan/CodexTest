import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageTk

END_HOUR = 17
END_MINUTE = 0


def update_timer():
    now = datetime.now()
    end_time = now.replace(hour=END_HOUR, minute=END_MINUTE, second=0, microsecond=0)
    if now > end_time:
        end_time += timedelta(days=1)
    remaining = end_time - now
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    root.after(1000, update_timer)


def create_cat_image():
    size = 32
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rectangle([8, 10, 24, 25], fill="gray")
    draw.polygon([(8, 10), (12, 2), (16, 10)], fill="gray")
    draw.polygon([(24, 10), (20, 2), (16, 10)], fill="gray")
    draw.rectangle([12, 16, 14, 18], fill="black")
    draw.rectangle([18, 16, 20, 18], fill="black")
    draw.rectangle([15, 20, 17, 22], fill="pink")

    return ImageTk.PhotoImage(img)


root = tk.Tk()
root.title("Котиковый таймер")
root.geometry("300x200")
root.configure(bg="#FFB6C1")  # light pink

cat_image = create_cat_image()
cat_label = tk.Label(root, image=cat_image, bg="#FFB6C1")
cat_label.pack(pady=5)

timer_label = tk.Label(root, text="", font=("Arial", 40, "bold"), bg="#FFB6C1", fg="white")
timer_label.pack(pady=10)

update_timer()
root.mainloop()
