f_temp_sun = 27000

f_temp_outside = 67

print(f'The temperature is {f_temp_sun} degrees')

#1 decimal place
print(f'The temperature is {f_temp_sun - 32 / 1.8:,.1f} degrees Celsius')

#create 15 characters wide
print(f'The temperature is {f_temp_sun - 32 / 1.8:15,.1f} degrees Celsius')

#1 left allign given 15 character wide space
print(f'The temperature is {f_temp_sun - 32 / 1.8:<15,.1f} degrees Celsius')
