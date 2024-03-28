# ridge regression interactive demo
# Creted by: Dimitrios Bouzoulas (dimitrios.bouzoulas@novia.fi)

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

global x, y, lambda_val

Range_of_points= [2, 100]
lambda_range = [0.0, 10.0]

lambda_val = 0 			# initial value 



def update_n(*args):
	global n, x, y
	n = int(args[0])
	return

def update_lambda(*args):
	global lambda_val
	lambda_val = float(args[0])
	return


def generate_data(n_samples, noise=1.0):
    """
    Generates a dataset with a linear relationship + noise.

    Parameters:
    - n_samples: int - The number of data points.
    - noise: float - The standard deviation of the Gaussian noise added to the output.

    Returns:
    - X: numpy array, shape (n_samples, 1) - The input features.
    - y: numpy array, shape (n_samples,) - The target values.
    """
    np.random.seed(42)  # For reproducible results
    X = np.random.rand(n_samples, 1) * 10  # Random values in [0, 10)
    y = 2 * X.squeeze() + 1 + np.random.randn(n_samples) * noise  # Linear relation with noise
    return X, y



def ridge_regression(X, y):
	"""
	Perform ridge regression using the normal equation.

	Parameters:
	- X: numpy array, shape (n_samples, n_features) - Input features.
	- y: numpy array, shape (n_samples,) - Target values.
	- alpha: float - Regularization strength.

	Returns:
	- coefficients: numpy array - Coefficients for the regression model.
	"""
	global lambda_val

	n_features = X.shape[1]
	X_with_intercept = np.hstack([np.ones((X.shape[0], 1)), X])  # Add column of ones for intercept

	I = np.eye(n_features + 1)
	I[0, 0] = 0  # Do not regularize the intercept term

	coefficients = np.linalg.inv(X_with_intercept.T @ X_with_intercept + lambda_val * I) @ X_with_intercept.T @ y

	return coefficients  # First element is intercept, rest are slopes





def update_datapoints(*args):
	global n

	x, y = generate_data(n_samples=n)
      
	print(type(x), " ", type(y))
	
	a, b = ridge_regression(x, y)

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


buttoncalculate_ridge_regression = tk.Button(master=button_frame,
					   text="calculate ridge regression",
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

slider_lambda = tk.Scale(slider_frame,
					   label='lambda value',
					   length=length,
					   repeatinterval=refresh_interval,
					   from_=lambda_range[0], to=lambda_range[1], resolution=0.1,
					   orient=tk.HORIZONTAL,
					   command=update_lambda)
# Set initial values
slider_volume.set(2)
slider_lambda.set(1)

# Pack all elements onto the GUI
button_frame.pack(side=tk.BOTTOM)
button_quit.pack(padx=5, side=tk.LEFT)
buttoncalculate_ridge_regression.pack(padx=5, side=tk.LEFT)
slider_frame.pack(side=tk.BOTTOM)
slider_volume.pack(padx=5, side=tk.LEFT)
slider_lambda.pack(padx=5, side=tk.LEFT)

checkbox_frame.pack(side=tk.BOTTOM)

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


tk.mainloop()








