conversion_to_meter = {
    "KM": 1000,
    "M": 1,
    "CM": 0.01,
    "MM": 0.001
}

def convert(value, from_unit, to_unit):
    """
    Convert a number from one unit to another.

    Steps:
    1. Convert the input value into meters.
    2. Convert the meters into the desired unit.
    """

    # Convert input to uppercase to avoid problems with lowercase
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Step 1: Convert from the original unit → meters
    value_in_meters = value * conversion_to_meter[from_unit]

    # Step 2: Convert meters → desired unit
    result = value_in_meters / conversion_to_meter[to_unit]

    return result


# =========================
# MAIN PROGRAM
# =========================
print("=== UNIT CONVERTER (KM, M, CM, MM) ===")

# Get user input
value = float(input("Enter a value to convert: "))
from_unit = input("Convert FROM (KM / M / CM / MM): ")
to_unit = input("Convert TO (KM / M / CM / MM): ")

# Perform conversion
result = convert(value, from_unit, to_unit)

# Output
print(f"\n{value} {from_unit.upper()} = {result} {to_unit.upper()}")
