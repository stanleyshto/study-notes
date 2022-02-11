# import package
import datetime
import tensorflow as tf
import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# prepare examples
celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

# create a layer of Dense Network
l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# assemble layers into the model
model = tf.keras.Sequential([l0])

# compile the model
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1)) 
 
# train the model
training_start_time = datetime.datetime.now()
print(f'{training_start_time} : Training started ...')
history = model.fit(celsius_q, fahrenheit_a, epochs=600, verbose=False)
training_end_time = datetime.datetime.now()
print(f"{training_end_time} : Training ended")
print(f"Training elapsed time : {training_end_time - training_start_time}")

input("Press Enter to continue...")

# display training statistics
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])

input("Press Enter to continue...")

# use the model to predict value
in_celsius = input('Degree in Celsius: ')
in_celsius_list = [int(in_celsius)]
print(model.predict(in_celsius_list)) 
input("Press Enter to continue...")

# looking at the layer weights
print("These are the layer variables: {}".format(l0.get_weights()))