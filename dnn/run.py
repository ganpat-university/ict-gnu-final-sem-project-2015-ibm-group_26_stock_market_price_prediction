import os
import preprocess as prep
import RNN as dl

model_type_file = ""
model_type = "RNN"
stock_name = "BAJAJ-AUTO.NS"
path = "../data/"+"{}/"
epochs_num_to_determin_model = 25
epochs_num = 25
op = "test"

path = path.format(stock_name)
model_type_file = path + "model.txt"
print(path)

if not os.path.exists(path):
    error = "error: '{}' Not Found".format(path)
    print(error)
    exit()
print("Reading csv file... ")
csv_path = path + "{}.csv".format(stock_name)

print("Dataset preprocessing...")
scaler, x_train, x_test, y_train, y_test = prep.preprocess(csv_path)

if op=="train":
    regressor = dl.train(x_train, y_train, epochs= epochs_num)
    dl.save_model(stock_name, regressor, path=path)
elif op=='retrain':
    old_model = path + "{}-{}.h5".format(stock_name, model_type)
    regressor = dl.retrain(old_model, x_train, y_train, epochs = epochs_num)
    dl.save_model(stock_name, regressor, path=path)
elif op=='test':
    model_path = path + "{}-{}.h5".format(stock_name, model_type)
    _mse, _mape = dl.test(model_path, scaler, x_test)
    print("Mse:", _mse,"\n mean absolute percentage error:",  _mape)
    
x = x_test[len(x_test)-1]
print("Prediction...")
model_path = path + "{}-{}.h5".format(stock_name, model_type)
prediction = dl.predict(model_path, scaler, x)
print(str(prediction[1]))
