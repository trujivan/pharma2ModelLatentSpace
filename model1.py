import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense

# Define the model architecture
num_features = 10  # Replace with the actual number of features
model1 = tf.keras.Sequential([
    LSTM(128, input_shape=(None, num_features), return_sequences=True),
    Dense(num_features, activation='softmax')
])

# Compile the model
model1.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model on molecular data
# ...

# Generate a new molecular structure (assuming you have a valid 'seed_input')
new_molecule = model1.predict(seed_input)
print("Generated molecule:", new_molecule)

from rdkit import Chem
from rdkit.Chem import Draw

# Read a molecule from SMILES (e.g., glucose)
smiles = 'C1CC2=C3C(=CC=C2)C(=CN3C1)[C@H]4C@@HNC4=O'
mol = Chem.MolFromSmiles(smiles)

# Display the molecule with atom indices
def mol_with_atom_index(mol):
    for atom in mol.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx())
    return mol

img = Draw.MolToImage(mol_with_atom_index(mol))
img.show()
