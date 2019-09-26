# JumpCloud Take Home Assignment
This project is a take home assignment from JumpCloud. The project is a class that implements two functions, 
`add_action` and `get_stats`. 

`add_action` accepts a json serialized string of the form `{"action":"jump", "time":100}`. It is assumed 
that an end user will be making concurrent calls to this function.

`get_stats` accepts no input and returns a serialized json array of the average time for each action that has
been provided to the `add_action` function. It is assumed that an end user will be making concurrent calls to 
this function.

A reader-writer lock is used to synchronize the use of the functions. Implementation of the reader-writer lock is taken 
from Tyler Neylon at Unbox Research, as it is assumed the implementation of the lock is not the focus of this 
assignment.

# Setup
Clone this repository:
`git clone https://github.com/dnguyen22/JumpCloud.git`

# Running the Code
  1. After cloning the repository, activate the virtualenv `. venv/bin/activate` 
  2. Install the libraries needed with `pip install -r requirements.txt`
  3. The tests for the code can be run with `pytest tests.py`
  
# Future Considerations
Additional tests can be written to further test the multithreaded use cases of the solution.
  