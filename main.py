# randomly shuffle a sequence
from random import seed
from random import shuffle
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(8888780
                          )]
print(sequence)
# randomly shuffle the sequence
shuffle(sequence)
print(sequence)