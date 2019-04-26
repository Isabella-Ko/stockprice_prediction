import get_prices as hist
import tensorflow as tf
from preprocessing import DataProcessing
# import pandas_datareader.data as pdr if using the single test below
import fix_yahoo_finance as fix
fix.pdr_override()

start = "2003-01-01"
end = "2018-01-01"

hist.get_stock_data("AAPL", start_date=start, end_date=end)
process = DataProcessing("stock_prices.csv", 0.9)
process.gen_test(10)
process.gen_train(10)

X_train = process.X_train / 200
Y_train = process.Y_train / 200

X_test = process.X_test / 200
Y_test = process.Y_test / 200

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))

model.compile(optimizer="adam", loss="mean_squared_error")

model.fit(X_train, Y_train, epochs=100)

print(model.evaluate(X_test, Y_test))

# If instead of a full backtest, you just want to see how accurate the model is for a particular prediction, run this:
# data = pdr.get_data_yahoo("AAPL", "2017-12-19", "2018-01-03")
# stock = data["Adj Close"]
# X_predict = np.array(stock).reshape((1, 10)) / 200
# print(model.predict(X_predict)*200)

