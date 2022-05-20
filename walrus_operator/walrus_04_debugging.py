'''
One of the best use cases for the walrus operator
is when debugging complex expressions
'''

import numpy as np
import math

# apprx radius of Earth in km
RAD: int = 6371


# locations of Oslo and Vancouver
phi_1: float = math.radians(59.9)
lambda_1: float = math.radians(10.8)

phi_2: float = math.radians(49.3)
lambda_2: float = math.radians(-123.1)


# distance between oslo and vancouver
distance: float = 2 * RAD * math.asin(
    np.sqrt(
        np.power(np.sin((phi_2 - phi_1)/2), 2)
        + np.cos(phi_1) * np.cos(phi_2)
        * np.power(np.sin((lambda_2 - lambda_1)/2), 2)
    )
)


'''
Now, say that you need to double-check your implementation
and want to see how much the haversine terms contribute
to the final result.
'''

phi_hav = float()
distance: float = 2 * RAD * math.asin(
    np.sqrt(
        (phi_hav:= np.power(np.sin((phi_2 - phi_1)/2), 2))
        + np.cos(phi_1) * np.cos(phi_2)
        * np.power(np.sin((lambda_2 - lambda_1)/2), 2)
    )
)
print(distance)
print(phi_hav)
