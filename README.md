# Stockprice Prediction
## Results
Model | Loss | Validation loss 
--- | --- | ---
CNN | 4.3936e-04 | 1.0628e-04
LSTM | 1.6276e-04 | 1.2779e-04
ConvLSTM | 1.3624e-04 | 1.0638e-04


## CNN model
1. Training loss vs Validation loss (50 epochs)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN.50ep.lr.0head.png" width="500"/>

2. Prediction stock values vs Real stock values (half-year)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN%20prediction.png" width="500"/>


## LSTM model
1. Training loss vs Validation loss (50 epochs)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/LSTM.50ep.1e-05lr.0head.png" width="500"/>

2. Prediction stock values vs Real stock values (half-year)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/LSTM%20prediction.png" width="500"/>

## CNN-LSTM model
1. Training loss vs Validation loss (50 epochs) (half-year)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN%20%2B%20LSTM.50ep.1e-05lr.0head.png" width="500"/>

2. Prediction stock values vs Real stock values (half-year)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN-LSTM%20prediction.png" width="500"/>
