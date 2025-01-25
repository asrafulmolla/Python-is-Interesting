def check_frequency (frequency):
    if 20 <= frequency <= 20000:
        return "Audio Frequency"
    elif 30000 <= frequency <= 300000000000:
        return "Radio Frequency"
    else:
        return "Neither Audio nor Radio Frequency"
# User input
try:
    freq=float(input("Enter the frequency in Hz: "))
    print(check_frequency(freq))
except ValueError:
    print("Please enter a valid number.")