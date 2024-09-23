import tkinter as tk

def update_image():
    global frame_index  
    canvas.itemconfig(image_item, image=frames[frame_index])
    window.after(100, update_image)  # Change image every 100ms
    frame_index = (frame_index + 1) % len(frames)  # Move to the next frame

# Create a tkinter window
window = tk.Tk()
window.title("Animated GIF")

# Load the GIF frames
frames = [tk.PhotoImage(file=f"frame_{i}_delay-0.03s.gif") for i in range(14)]

# Create a canvas widget
canvas = tk.Canvas(window, width=frames[0].width(), height=frames[0].height())
canvas.pack()

# Display the initial frame
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=frames[0])

# Initialize frame index and start animation
frame_index = 0
update_image()

# Start the tkinter main loop
window.mainloop()
