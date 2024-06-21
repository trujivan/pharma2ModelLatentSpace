import tensorflow as tf
from tensorflow.keras.layers import Dense

# Assume you have features for each compound (e.g., molecular fingerprints)
# X1 and X2 represent two compounds

# Define the model architecture
num_features = 10  # Replace with the actual number of features
model2 = tf.keras.Sequential([
    Dense(64, activation='relu', input_shape=(num_features,)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model2.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on labeled compound pairs (interactions vs. non-interactions)
# ...

# Predict interaction probability between two compounds (provide actual X1 and X2)
interaction_prob = model2.predict([[X1], [X2]])
print("Interaction probability:", interaction_prob)

import pubchempy as pcp

# Get compound by CID (Vioxx)
vioxx = pcp.Compound.from_cid(5090)

print("Molecular formula:", vioxx.molecular_formula)
print("Molecular weight:", vioxx.molecular_weight)
print("XLogP (lipophilicity):", vioxx.xlogp)
