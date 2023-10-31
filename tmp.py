# Convert temperature to celsius and create a new column in the df

def convert(temperature_fahrenheit):
    temperature_celsius = ((temperature_fahrenheit - 32) * 5 / 9)
    return round(temperature_celsius, 1)


la_temp_1945_2022_df['temperature_c'] = (
    la_temp_1945_2022_df['temperature_f'].apply(convert)
)

la_temp_1945_2022_df