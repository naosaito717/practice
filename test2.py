import pandas as pd
from src.test import Cart, Item

data = {
    "A": [10, 40, 50],
    "B": [30, 20, 60],
    "C": [20, 80, 10],
    "D": ["X", "Y", "Z"]  
}

df = pd.DataFrame(data)
print(df)


print(df['A'])
cartA = Cart('A')
cartA.cago = [df["A"]]
cartB = Cart('cartB')
# print(cartA.name)


