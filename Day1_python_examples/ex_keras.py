
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import make_moons


X, y = make_moons(n_samples=1000)

model = Sequential([
    Dense(10, input_dim=2, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', 
              metrics=['accuracy']
              )

model.fit(X, y, epochs=50)
score = model.evaluate(X, y)
print("loss/accuracy:", score)
