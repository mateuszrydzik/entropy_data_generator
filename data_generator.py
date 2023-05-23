from scipy.stats import entropy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataGenerator:
    def __init__(self, entropy: float, nclass: int, weights: list = None,  dim: int = 8):
        self.entropy = entropy
        self.nclass = nclass
        self.weights = weights
        self.dim = dim
        self.iterations = None

    def get_entropy(self, labels):
        value,counts = np.unique(labels, return_counts=True)
        return entropy(counts, base=2)
    
    def flatten_matrix(self, matrix):
        df = pd.DataFrame(matrix)
        return df.values.flatten().tolist()

    def generate(self):
        i = 0
        generated_entropy = None
        while self.entropy != generated_entropy:
            i += 1
            if self.weights is None:
                used_weights = np.random.dirichlet(np.ones(self.nclass), size=1)[0]
            else:
                used_weights = self.weights
            matrix = np.random.choice(range(1, self.nclass+1), size=(self.dim, self.dim), p=used_weights)
            ent = self.get_entropy(labels = self.flatten_matrix(matrix))
            generated_entropy = round(ent, 1)
        self.iterations = i
        return matrix
    
    def plot_matrix(self, matrix):
        plt.imshow(matrix, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.title('Matrix Raster Plot')
        plt.show()