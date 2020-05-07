from ctypes import *
import numpy as np

lib = np.ctypeslib.load_library("libSimpleMC.so", ".")
lib.SimpleMonteCarloCall.argtypes = [c_double, c_double,
                                     c_double, c_double,
                                     c_double, c_ulong]
lib.SimpleMonteCarloCall.restype = c_double

expiry = c_double(1.0)
strike = c_double(100.0)
spot = c_double(100.0)
vol = c_double(0.20)
r = c_double(0.01)
N = c_ulong(1000000)

result = lib.SimpleMonteCarloCall(expiry, strike, spot, vol, r, N)
print(result)
