# Vending machine implementation using Python

During the first semester of my [MSc Advanced Computer Science](https://www.keele.ac.uk/pgtcourses/advancedcomputersciencemsc/) degree, I took a module called System Design and Programming.

Outcomes from this module included:

- Developed an understanding of the requirements gathering process
- Introduced to systems design concepts such as use cases/sequence diagrams/class diagrams
- Created basic UML diagrams
- Introduced to programming fundamentals using Python

For the programming aspect of the module, we were tasked with producing a vending machine program.

This document details the requirements and objectives of the program. In the repository, you will find the files used to run the program as well as the full program (given in Python 2.7 and Python 3).

- [Specification](#specification)
- [Usage](#usage)
- [Example](#example)

--------------------------------------------------------------------------------

## Specification

You will be given the following files:

**`dstock.csv`**

Denomination | Stock
------------ | -----
2.00         | 50
1.00         | 50
0.50         | 50
0.20         | 50
0.10         | 50
0.05         | 50
0.02         | 50
0.01         | 50

**`products.csv`**

Code | Name                    | Stock
---- | ----------------------- | -----
01   | Mars bar                | 50
02   | Cheese and Onion crisps | 50
03   | Yorkie Plain            | 50
04   | Oat Flapjack            | 50

--------------------------------------------------------------------------------

**Produce a program that till read the two files from the current directory, and then repeatedly allow purchases to occur.**

- For each purchase, permit the user to enter a `product code` and `monetary value` (representing the coins placed into the machine)

- For each purchase, output the `product code`, `amount entered` and a sequential list of `coins` produced, as a separate line in a file entitled `change.txt`. Change produced must use the least amount of coins possible.

    **Example `change.txt` file**
    <br>
    ```
    01, 1.03, 0.20, 0.02, 0.01

    04, 1.53, 0.50, 0.20, 0.20, 0.02, 0.01

    Insufficient funds
    ```
- If an error occurs, output an appropriate message as a single line in the same file.

- Update the `dstock.csv` and `products.csv` files stock counts after each purchase

--------------------------------------------------------------------------------

## Usage

In order to run the program on your own machine, Python 2.7 or Python 3 needs to be installed.<br>
Once the repository is downloaded, running `full_vending_program.py` will produce the required files.<br>

To make sure it works:

1. Check the `dstock.csv` and `products.csv` files for their contents
2. Run the program
3. Check the `dstock.csv` and `products.csv` and `change.txt` files for their contents (the input files will have changed according to the simulation).

--------------------------------------------------------------------------------

At the bottom of the `full_vending_program.py` file, I have created a simulation that produces 100 separate purchases. So running the file as it comes will use the purchases from this.

This is the simulation code.

```python
"""

test method - runs the specified number of purchases with a random amount between 0.5 - 2.00

main method - Represents a single purchase

"""
def test(num):
    for i in range(0, num):
        main(randint(1, 4), round(uniform(0.5, 2) / 0.01) * 0.01)


test(100)
```

## Example

**Input files**

**`dstock.csv`**

Denomination | Stock
------------ | -----
2.00         | 50
1.00         | 50
0.50         | 50
0.20         | 50
0.10         | 50
0.05         | 50
0.02         | 50
0.01         | 50

--------------------------------------------------------------------

**`products.csv`**

Code | Name                    | Stock
---- | ----------------------- | -----
01   | Mars bar                | 20
02   | Cheese and Onion crisps | 20
03   | Yorkie Plain            | 20
04   | Oat Flapjack            | 20

--------------------------------------------------------------------------------

Running `full_vending_program.py` with the following simulation (this can be modified the bottom of the file)

```python
"""
    test method - runs the specified number of purchases with a random amount between 0.5 - 2.00
    main method - Represents a single purchase
"""
def test(num):
    for i in range(0, num):
        main(randint(1, 4), round(uniform(0.5, 2) / 0.01) * 0.01)


test(10)
```

--------------------------------------------------------------------------------

**Output files**

**`dstock.csv`**

Denomination | Stock
------------ | -----
2.00         | 50
1.00         | 48
0.50         | 49
0.20         | 43
0.10         | 48
0.05         | 46
0.02         | 44
0.01         | 49

------------------------------------------------------------------------

**`products.csv`**

Code | Name                    | Stock
---- | ----------------------- | -----
01   | Mars bar                | 19
02   | Cheese and Onion crisps | 18
03   | Yorkie Plain            | 19
04   | Oat Flapjack            | 17

------------------------------------------------------------------------

**`changes.txt`**

02, 1.34, 0.20, 0.20, 0.05, 0.02, 0.02<br>
04, 1.05, 0.20, 0.20, 0.05<br>
03, 1.23, 0.20, 0.20, 0.05, 0.02, 0.01<br>
Insufficient funds<br>
01, 1.95, 1.00, 0.10, 0.02, 0.02<br>
04, 1.72, 1.00, 0.10, 0.02<br>
Insufficient funds<br>
04, 0.6<br>
Insufficient funds<br>
02, 1.6, 0.50, 0.20, 0.05<br>

------------------------------------------------------------------------

**`simulations.txt`**

2,1.34<br>
4,1.05<br>
3,1.23<br>
3,0.53<br>
1,1.95<br>
4,1.72<br>
3,0.58<br>
4,0.60<br>
1,0.65<br>
2,1.60<br>

**NOTE**

I decided to add a `simulations.txt` file which represents the product code and monetary value for each purchase. As you can see, 3/10 attempts were made with insufficient funds. Appropriate messages are displayed in `changes.txt` and counting the difference between the input/output files confirms this.

--------------------------------------------------------------------------------

**NOTE**

This was my my first experience of programming (outside of self taught HTML/CSS/Javascript), therefore does not represent my current skill level.

Since the time of this project, I have improved massively and gained much more experience (and hours programming).

Other repositories will give a better reflection of where I am currently at. I'm aware that the program is highly inefficient and would have been much better if it utilised an object oriented approach, however at the time this was beyond my capabilities. I preceded to complete the program using a procedural approach (since it was the only way I knew how).
