"""
    so function use test in python
"""
from time import time
from ctypes import *
import numpy as np


def calcu_BS_call_with_MC(expiry, strike, spot, vol, r, N):
    # calculae BS call price by simple MC in python
    # this function is for the comparison to C++ function
    variance = vol * vol * expiry
    root_variance = np.sqrt(variance)
    ito_correction = -0.5 * variance

    moved_spot = spot * np.exp(r * expiry + ito_correction)
    this_spot = 0.0
    running_sum = 0.0

    for i in range(N):
        this_gaussian = np.random.randn()
        this_spot = moved_spot * np.exp(root_variance * this_gaussian)
        this_payoff = this_spot - strike
        this_Payoff = max(this_payoff, 0)
        running_sum += this_Payoff

    mean = running_sum / N
    mean *= np.exp(-r * expiry)
    return mean


def main():
    # so file function preparation
    lib = np.ctypeslib.load_library("libSimpleMC.so", ".")
    lib.SimpleMonteCarloCall.argtypes = [c_double, c_double,
                                         c_double, c_double,
                                         c_double, c_ulong]
    lib.SimpleMonteCarloCall.restype = c_double

    # don't have to covert c_*
    # expiry = c_double(1.0)
    # strike = c_double(100.0)
    # spot = c_double(100.0)
    # vol = c_double(0.20)
    # r = c_double(0.01)
    # N = c_ulong(1000000)

    expiry = 1.0
    strike = 100.0
    spot = 100.0
    vol = 0.20
    r = 0.01
    N = 1000000

    # simple comparison between so and py MC function
    test_num = 10
    start_time = time()
    for i in range(test_num):
        result = lib.SimpleMonteCarloCall(expiry, strike, spot, vol, r, N)
        # print(result)
    print('so func({} times): {} sec.'.format(test_num, time() - start_time))

    start_time = time()
    for i in range(test_num):
        result = calcu_BS_call_with_MC(expiry, strike, spot, vol, r, N)
        # print(result)
    print('py func({} times): {} sec.'.format(test_num, time() - start_time))


if __name__ == '__main__':
    main()
