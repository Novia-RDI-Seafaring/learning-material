

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


Range_of_points = [3, 100]
Range_of_lambda = [0, 10000]

global lambda_var, n, x

n = Range_of_points[0]
lambda_var = 100


def update_n(*args):
	global n, x
	n = int(args[0])
	x = generate_random_data(0, 100, n)
	return


def update_lambda(*args):
	global lambda_var
	lambda_var = int(args[0])
	return


def generate_random_data(min_val, max_val, num_points):
	x_points = np.random.choice(a=list(range(1,100)), size=n)
	return x_points





def generate_d_array(n):
    rows = n-2
    arr = []
    for i in range(rows):
        arr.append([0]*(n-1))
        arr[i][i:i+2] = [1,-2,1]

    return np.array(arr)







def update_datapoints(*args):
	global n, lambda_var, x

	D = generate_d_array(n)

	I = np.eye(n)
	
	T = np.linalg.inv(I + lambda_var * D.T @ D) @ x


	# visualization
	fig.clear()
	ax1 = fig.add_subplot(1,1,1)
	ax1.plot(x, color='red', label='Best Fit Line')
	ax1.plot(T, color='blue', label='Best Fit Line')
	
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.set_title('HP filter demo')
	ax1.legend(['Data', 'HP filter'], loc=2)
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


slider_lambda_var = tk.Scale(slider_frame,
					   label='lambda',
					   length=length,
					   repeatinterval=refresh_interval,
					   from_=Range_of_lambda[0], to=Range_of_lambda[1], resolution=1,
					   orient=tk.HORIZONTAL,
					   command=update_lambda)

# Set initial values
slider_volume.set(0)
slider_lambda_var.set(100)


# Pack all elements onto the GUI
button_frame.pack(side=tk.BOTTOM)
button_quit.pack(padx=5, side=tk.LEFT)
buttoncalculate_least_squares.pack(padx=5, side=tk.LEFT)
slider_frame.pack(side=tk.BOTTOM)
slider_volume.pack(padx=5, side=tk.LEFT)
slider_lambda_var.pack(padx=5, side=tk.LEFT)

checkbox_frame.pack(side=tk.BOTTOM)

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


tk.mainloop()








