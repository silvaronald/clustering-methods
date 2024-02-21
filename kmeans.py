import numpy as np

class KMeans:
    def __init__(self, k: int, data: np.array):
        self.k = k
        self.data = data
        self.clusters = np.zeros(self.data.shape[0])
        self.centroids = np.random.randint(k, self.data.shape[1])

        self.iterate()

    def iterate(self):
        