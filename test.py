import numpy as np
import pickle

loaded_model = pickle.load(open('model.pkl', 'rb'))
inp = np.array([0, 59, 6, 1.20, 6220, 26, 22, 227, 4.75, 0.90, 96, 97, 0.02])
inp1 = inp.reshape(1,-1)
pred = loaded_model.predict(inp1)
print(pred)