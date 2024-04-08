

# Linear regression interactive demo
# Creted by: Johan Westö (johan.westo@novia.fi)

import random
import numpy as np
import tkinter as tk
from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# tkinter GUI
root = tk.Tk()
root.wm_title("Linear regression example")
fig = Figure(figsize=(12, 5), dpi=100)
fig.subplots_adjust(wspace=0.3);
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.


Range_of_points= [0, 100]

def update_n(*args):
	global n
	n = int(args[0])
	return

def generate_random_data(min_val, max_val, num_points):
    x_points = np.random.uniform(min_val, max_val, num_points)
    y_points = np.random.uniform(min_val, max_val, num_points)
    
    return x_points, y_points


def update_datapoints(*args):
	global n

	x, y = generate_random_data(0, 100, n)

	A = np.stack([x, np.ones(len(x))]).T
	a, b = np.linalg.lstsq(A, y, rcond=None)[0]
	
	y_best_fit = [a * x + b for x in x]

	fig.clear()

	ax1 = fig.add_subplot(1,1,1)
      
	ax1.scatter(x, y, color='blue', label='Data Points')
	ax1.plot(x, y_best_fit, color='red', label='Best Fit Line')
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title('Data and model')
	ax1.legend(['Data', 'Model'], loc=2)
	canvas.draw()

	canvas.get_tk_widget().pack()

	return



# Buttons
button_frame = tk.Frame()

button_quit = tk.Button(master=button_frame,
						text="Quit",
						command=root.quit)



buttoncalculate_least_squares = tk.Button(master=button_frame,
					   text="calculate least squares",
					   command=update_datapoints)

# Checkboxes
checkbox_frame = tk.Frame()
show_errors = tk.IntVar()


# Sliders
length = 150
refresh_interval = 10
slider_frame = tk.Frame()

slider_volume = tk.Scale(slider_frame,
					   label='Points num',
					   length=length,
					   repeatinterval=refresh_interval,
					   from_=Range_of_points[0], to=Range_of_points[1], resolution=1,
					   orient=tk.HORIZONTAL,
					   command=update_n)


# Set initial values
slider_volume.set(0)

# Pack all elements onto the GUI
button_frame.pack(side=tk.BOTTOM)
button_quit.pack(padx=5, side=tk.LEFT)
buttoncalculate_least_squares.pack(padx=5, side=tk.LEFT)
slider_frame.pack(side=tk.BOTTOM)
slider_volume.pack(padx=5, side=tk.LEFT)

checkbox_frame.pack(side=tk.BOTTOM)

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


tk.mainloop()








