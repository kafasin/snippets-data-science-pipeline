from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scores = scaler.fit_transform(df["a"].values.reshape(-1,1))
