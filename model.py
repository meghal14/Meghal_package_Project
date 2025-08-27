import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv(r"C:\Users\Admin\Downloads\placement (1).csv")
print(df.head(3))

X=df[["cgpa"]]
Y=df[["package"]]

model=LinearRegression()
model.fit(X,Y)

pickle.dump(model, open("prediction.pkl", "wb"))
print("Mpodle save Sucessfully!!!")
