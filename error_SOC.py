import math

def error_calc(E1, E2, E3, E4, N):
    sigma_E1 = math.sqrt((1 - E1**2) / N)
    sigma_E2 = math.sqrt((1 - E2**2) / N)
    sigma_E3 = math.sqrt((1 - E3**2) / N)
    sigma_E4 = math.sqrt((1 - E4**2) / N)

    S = E1 - E2 + E3 + E4

    sigma_S = math.sqrt(
        sigma_E1**2 +
        sigma_E2**2 +
        sigma_E3**2 +
        sigma_E4**2
    )

    S_min = S - sigma_S
    S_max = S + sigma_S

    print(f"{sigma_S}")
    return S, sigma_S, S_min, S_max



N = 100000

print("Double / Torino")
error_calc(0.2426, -0.2197, 0.1189, 0.1547, N)

print("Double / Kingston")
error_calc(0.3921, -0.4130, 0.6589, 0.6305, N)

print("Double / Pittsburgh")
error_calc(0.6131, -0.6076, 0.6092, 0.6313, N)

print("Double / Marrakesh")
error_calc(0.4206, -0.3624, 0.4639, 0.5065, N)

print("Double / Fez")
error_calc(0.4389, -0.4753, -0.0734, -0.0417, N)

print("Single / Torino")
error_calc(0.3066, -0.3065, 0.0273, 0.0469, N)

print("Single / Kingston")
error_calc(0.5138, -0.5217, 0.6447, 0.6433, N)

print("Single / Pittsburgh")
error_calc(0.4881, -0.4789, 0.6247, 0.6600, N)

print("Single / Marrakesh")
error_calc(0.3921, -0.4130, 0.6589, 0.6305, N)

print("Single / Fez")
error_calc(0.3985, -0.4263, 0.6765, 0.6506, N)

print("No protocol / Torino")
error_calc(0.49422, 0.5433, 0.6014, 0.53674, N)

print("No protocol / Kingston")
error_calc(0.49414, -0.6544, 0.63466, 0.44586, N)

print("No protocol / Pittsburgh")
error_calc(0.44226, -0.65338, 0.62372, 0.42996, N)

print("No protocol / Marrakesh")
error_calc(0.4536, -0.60614, 0.61068, 0.44562, N)

print("No protocol / Fez")
error_calc(0.5363, -0.46606, 0.53518, 0.63774, N)

