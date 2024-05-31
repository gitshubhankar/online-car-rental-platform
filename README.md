# online-car-rental-platform
<h2>Project Title: Online Car Rental Platform</h2>

<b><h4>Project Objective: </h4></b>
Build an online car rental platform using Object-Oriented Programming in Python.

<b><h4>Problem Statement:</h4></b>
A car rental company has requested you to build an online car rental platform where customers should be able to view the available cars that can be rented on an hourly, daily, or weekly basis. The company can display the available inventory and confirm requests by checking the available stock. Customers will receive an auto-generated bill when they return the car.

For simplicity, let’s assume that:
1.	Customers can rent cars from any one of the following options—hourly, daily, or weekly rental.
2.	Customers are free to choose any number of cars they want, provided the number of available cars is more than the number of requested cars.


<b><h4>You must use the following tools:</h4></b>
Jupyter Notebook: To create the module and main project files

<b><h4>Instructions to Perform:</h4></b>

1.	Create a module (.py file) for car rental and import the built-in module DateTime to handle the rental time and bill.
2.	Create a class for renting the cars and define a constructor in it.
3.	Define a method for displaying the available cars. Also, define methods for renting cars on an hourly, daily and weekly basis, respectively.
4.	Inside these methods, make sure that the number of requested cars is positive and lesser than the total available cars.
5.	Store the time of renting a car in a variable, which can later be used in the bill while returning the car. 
6.	Define a method to return the cars using rental time, rental mode (hourly, daily, or weekly), and the number of cars rented.
7.	Inside the return method; update the inventory stock, calculate the rental period, and generate the final bill.
8.	Create a class for customers and define a constructor in it.
9.	Define methods for requesting the cars and returning them. 
10.	Next, create the main project (.ipynb) file and import the car rental module in it.
11.	Define the main method and create objects for both car rental and customer classes.
12.	Inside the main method, take the customer’s input as a choice for displaying car availability, rental modes, or returning the cars.
13.	Use the relevant method for the customer’s input and print relevant messages.
14.	Run the main method to start your project.
