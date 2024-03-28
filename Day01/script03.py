# Swap two numbers without using third variable

def swap_values(value_1 = 1 , valaue_2 = 2):
    value_1 , valaue_2 = valaue_2 , value_1
    print(f"Value 1: {value_1} \nValue 2: {valaue_2}")

swap_values()

# Output: 
  
# Value 1: 2 
# Value 2: 1