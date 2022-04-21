#display 10 random numbers from interval [0,1)
import random
for i in range(10):
        print(random.random())
#output 
#0.3242484516931208
#0.10647808041150897
#0.36645114220120956
#0.13120140663038915
#0.21202274384312736
#0.6688571090627221
#0.7784418176759176
#0.1708607690512468
#0.4298147646721351
#0.3824352240277502

#generate random numbers from interval [3, 7)
import random

def my_random():
	return 4*random.random() + 3

for i in range(10):
        print(my_random())

#output 
#6.12874279589448
#4.708316567993207
#6.603551578701002
#4.768669140990533
#5.747707245530573
#6.54767487873182
#3.587203462129961
#3.973449630675757
#5.912845071240474
#3.681738043265683

#there is an easier way to generate random numbers for any interval
help(random.uniform)

import random
for i in range(10):
        print(random.uniform(3,7))

#output: 
#3.2709327811656044
#3.024959530711709
#3.4786034637681835
#4.253784666584921
#3.2933929037244516
#3.4769605435358444
#4.661609812638858
#3.765981078169061
#4.007409550266827
#5.351601303285316

# both random and uniform functions are uniform distributions

#for normal distribution, we use the normalvariate function

import random
for i in range(20):
	print(random.normalvariate(0,9))
#0 is the mean
#9 is the standard deviation

# for discrete probability distributions, for example when simulating the role of a six-sided die
# for this we use randint(min, max) function

import random
for i in range(20):
        print(random.randint(1, 6))

# when we want to make a selection of a random element from a list we use the choice() function 

import random
outcomes = ["rock", "paper", "scissors"]

for i in range(20):
        print(random.choice(outcomes))
