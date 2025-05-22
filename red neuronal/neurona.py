import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.feature_extraction.text import CountVectorizer

# Datos
nombres = ["Leonardo", "Leonardo", "Leonardo", "Maria", "Juan", "Carlos", "Pedro", "Ana", "Luis", "Elena"]
etiquetas = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]  # 1=Leonardo, 0=Otro

# Vectorizar texto
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,3))  # usa caracteres y n-gramas
X = vectorizer.fit_transform(nombres).toarray()

y = np.array(etiquetas)

# Crear modelo
model = Sequential([
    Dense(32, input_dim=X.shape[1], activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=400, verbose=1)

# Probar predicciones
test_nombres = ["Leonardo", "Maria", "Laura", "Pedro", "Luis"]
X_test = vectorizer.transform(test_nombres).toarray()

preds = model.predict(X_test)
print("\nPredicciones:")
for nombre, pred in zip(test_nombres, preds):
    print(f"{nombre}: {'Leonardo' if pred > 0.5 else 'Otro'}")
