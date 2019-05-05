# Stockprice Prediction
## Test Results
Predictions on real stock values. Duration: Half-year. Company: Apple
1. CNN
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN%20prediction.png" width="500"/>
2. LSTM
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/LSTM%20prediction.png" width="500"/>
3. CNN + LSTM
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN-LSTM%20prediction.png" width="500"/>


## Training Results
Model | Loss | Validation loss 
--- | --- | ---
CNN | 4.3936e-04 | 1.0628e-04
LSTM | 1.6276e-04 | 1.2779e-04
CNN + LSTM | 1.3624e-04 | 1.0638e-04


## CNN model
- Training loss vs Validation loss (50 epochs)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN.50ep.lr.0head.png" width="500"/>


## LSTM model
- Training loss vs Validation loss (50 epochs)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/LSTM.50ep.1e-05lr.0head.png" width="500"/>


## CNN + LSTM model
- Training loss vs Validation loss (50 epochs) (half-year)
<img src="https://github.com/Isabella-Ko/stockprice_prediction/blob/master/figures/CNN%20%2B%20LSTM.50ep.1e-05lr.0head.png" width="500"/>

This project is inspired by VivekPa.
His project can be found here:
[IntroNeuralNetworks](https://github.com/VivekPa/IntroNeuralNetworks)

The reference of CNN+LSTM model:[Reference of CNN+LSTM model](http://www.naun.org/main/NAUN/neural/2018/a162016-062.pdf)
