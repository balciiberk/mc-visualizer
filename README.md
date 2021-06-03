# Monte Carlo pi calculator visualisation

This code visualizes one of the most basic usages of Monte Carlo (MC) methods which is calculating pi. This is one of the most basic and easy-to-understand way of calculating pi with MC. It is done by placing the biggest possible circle inside a square. Then generating pseudorandom coordinates inside the square and calculating the ratio of the coordinates inside the circle to all cooirdinates which is equal to pi over 4.

I used this visualization for explaining MC to people who are learning it for the first time. 

It may generate slow animations for explaining the process like:
![slow animation](/images/slow.gif)

It may also generate faster animations like:
![fast animation](/images/fast.gif)

While generating the animations it prints out the value of pi calculated by the points generated so far.

Lastly at the end of the animation it plots the graph of calculated pi against iterations for showing its convergence:
![graph](/images/graph.png)
