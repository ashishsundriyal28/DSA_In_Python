# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array([ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# Complexity of creating two dimensional array?
# If doing like this, T.C. = O(MN).
# Where m is the number of columns and n is the number of rows.
# So this is very time consuming operations. We are initializing the value straight away.

# S.C. = O(N)
# because we have m number of columns and n number of rows.
# So we need this number of space in the memory.