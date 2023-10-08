def ms_to_degree(ms):
    if ms < 0.4:
        return -45
    elif ms < 1:
        return (ms - 0.4) * (0 - (-45)) / (1 - 0.4) + (-45)
    elif ms < 2:
        return (ms - 1) * (90 - 0) / (2 - 1) + 0
    elif ms <= 3:
        return (ms - 2) * (120 - 90) / (3 - 2) + 90
    else:
        raise ValueError("Milliseconds value is not in the provided data.")

def degree_to_ms(degrees):
    if degrees < -45:
        return 0.4
    elif degrees < 0:
        return (degrees - (-45)) * (1 - 0.4) / (0 - (-45)) + 0.4  
    elif degrees < 90:
        return (degrees - 0) * (2 - 1) / (90 - 0) + 1
    elif degrees <= 120:
        return (degrees - 90) * (3 - 2) / (120 - 90) + 2
    else:
        raise ValueError("Degrees value is not in the provided data.")