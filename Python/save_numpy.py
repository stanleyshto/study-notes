import numpy as np

test_sample = np.array([[
                            [1,2,3],
                            [4,5,6],
                            [5,6,7],
                            [7,8,9]
                        ],[
                            [11,12,13],
                            [14,15,16],
                            [15,16,17],
                            [17,18,19]
                        ]])
print(test_sample)
np.savetxt('test_sample.csv',test_sample,delimiter=',')
