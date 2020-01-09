#This problem was asked by Twitter.

#You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

#record(order_id): adds the order_id to the log
#get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
#You should be as efficient with time and space as possible.

class problem_16:
    def __init__(self):
        self.log_arr = []

    # Adds the order_id to the log
    def record(self, order_id):
        self.log_arr.append(order_id)

    # Gets the ith last element from the log. i is guaranteed to be smaller than or equal to N
    def get_last(self, i):
        return self.log_arr[-1 * i]
    
prob = problem_16()

# Adding data to the array
for i in range(0, 1000):
    prob.record(i)

# last order_id added to log should be 999
print(prob.get_last(1))

# first order_id added to log should be 0
print(prob.get_last(1000))

# mid order_id added to log should be 500
print(prob.get_last(500))

