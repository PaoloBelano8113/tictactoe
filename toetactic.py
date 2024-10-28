import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv('tictactoe/dataset/tictactoe_win_movement.csv')

X = df['table']
y = df['table_prob_choose']

def parse_table_string(string):
    numbers = re.findall(r'\d+', string)
    numbers = np.array(numbers, dtype=int)
    return numbers

X_converted = np.array([parse_table_string(x) for x in X]) 
y_converted = np.array([parse_table_string(y_val) for y_val in y]) 

X_flattened = np.array([x.flatten() for x in X_converted])  
y_flattened = np.array([y.flatten() for y in y_converted])  


X_train, X_test, y_train, y_test = train_test_split(X_flattened, y_flattened, test_size=0.2, random_state=42)

y_train = np.array([np.argmax(y) for y in y_train])  
y_test = np.array([np.argmax(y) for y in y_test]) 

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(9, activation='softmax'))  

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=1, batch_size=32, validation_split=0.2)

accuracy = model.evaluate(X_test, y_test)
print("Model accuracy:", accuracy[1])
