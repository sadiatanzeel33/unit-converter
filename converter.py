import streamlit as st

def main():
    st.title("Unit Converter")
    st.write("Use this unit converter to convert Length, Temperature, Weight")
    st.write("Created by Sadia Tanzeel")

    converter_type = st.selectbox("Choose the type of conversion", ["Length", "Temperature", "Weight"])

    if converter_type == "Length":
        length_converter()
    elif converter_type == "Temperature":
        temperature_converter()
    elif converter_type == "Weight":
        weight_converter()

def length_converter():
    units = ["Meters", "Kilometers", "Miles", "Yards"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)

    if st.button("Convert"):
        conversion_factor = get_length_conversion_factor(from_unit, to_unit)
        result = value * conversion_factor
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

def get_length_conversion_factor(from_unit, to_unit):
    factors = {
        "Meters": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361},
        "Kilometers": {"Meters": 1000, "Kilometers": 1, "Miles": 0.621371, "Yards": 1093.61},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Miles": 1, "Yards": 1760},
        "Yards": {"Meters": 0.9144, "Kilometers": 0.0009144, "Miles": 0.000568182, "Yards": 1}
    }
    return factors[from_unit][to_unit]

def temperature_converter():
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", step=0.1)

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67
    return value

def weight_converter():
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0, step=0.1)

    if st.button("Convert"):
        conversion_factor = get_weight_conversion_factor(from_unit, to_unit)
        result = value * conversion_factor
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

def get_weight_conversion_factor(from_unit, to_unit):
    factors = {
        "Grams": {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Kilograms": {"Grams": 1000, "Kilograms": 1, "Pounds": 2.20462, "Ounces": 35.274},
        "Pounds": {"Grams": 453.592, "Kilograms": 0.453592, "Pounds": 1, "Ounces": 16},
        "Ounces": {"Grams": 28.3495, "Kilograms": 0.0283495, "Pounds": 0.0625, "Ounces": 1}
    }
    return factors[from_unit][to_unit]

if __name__ == "__main__":
    main()
