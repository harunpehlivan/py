import numpy as np

def gradient_descent(x,y,epochs):
    m_curr = b_curr = 0
    n = len(x)
    learning_rate = 0.08

    for i in range(epochs):
        y_predicted = m_curr * x + b_curr
        cost = 1/n * sum(val**2 for val in (y-y_predicted))
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f"m {m_curr}, b {b_curr}, cost {cost} iteration {i}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y, 500)