import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def preprocess(path):
    ds = pd.read_csv(path)
    ds.dropna(how='any',axis=0)
    dataset = ds.iloc[:, [2, 5]].values
    x = ds.iloc[:, 2].values
    y = ds.iloc[:, 5].values
    
    ## feature scalling
    
    scaler = MinMaxScaler(feature_range=(0,1))
    dataset_scaled = scaler.fit_transform(dataset)
    
    x = dataset_scaled[:, 0]
    y = dataset_scaled[:, 1]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 73)
    
    return scaler, x_train, x_test, y_train, y_test