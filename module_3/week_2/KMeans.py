import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_dataset = load_iris()
data = iris_dataset.data[:, :2]

class KMeans():
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
        self.clusters = None

    def initalCentroids(self, data):
        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]
        print(f'Inital centroid function: {self.centroids}')

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum(np.power(x1-x2, 2)))
    
    def assign_clusters(self, data):
        distances = []
        for x in data:
            print(f'Inital centroid: {self.centroids}')

            for centroid in self.centroids:
                distance = self.euclidean_distance(x, centroid)
                print(f"Distance = {distance}")
                distances.append(distance)
        distances = np.array(distances)
        print(distances)
        print(np.argmin(distances, axis=1))
        return np.argmin(distances, axis=1)
    
    def update_centroids(self, data):
        return np.array([data[self.clusters==i].mean(axis=0) for i in range(self.k)])
    
    def fit(self, data):
        self.initalCentroids(data)
        self.plot_cluster(data, 0)
        for i in range(self.max_iters):
            self.clusters = self.assign_clusters(data)
            self.plot_cluster(data, i)
            new_centroid = self.update_centroids(data)

            if np.all(self.centroids == new_centroid):
                break

            self.centroids = new_centroid

        self.plot_final_clusters(data)

    def plot_cluster(self, data, interation):
        # plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap="viridis", marker="o", alpha=0.6)
        # plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c="red", marker="x")
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title(f"Interation {interation+1}")
        plt.xlabel("Spetal lenght")
        plt.ylabel("Spetal width")
        plt.show()

    def plot_final_clusters(self, data):
        # plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap="viridis", marker="o", alpha=0.6)
        # plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c="red", marker="x")
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title("Final Clusters and Centroids Point")
        plt.xlabel("Spetal lenght")
        plt.ylabel("Spetal width")
        plt.show()
feature_1 =np.array([2.0, 3.0, 3.5, 8.0, 8.5, 9.0, 1.0, 1.5])
feature_2 =np.array([3.0, 3.5, 3.0, 8.0, 8.5, 8.0, 2.0, 2.5])
feature_3 =np.array([1.5, 2.0, 2.5, 7.5, 8.0, 8.5, 1.0, 1.5])

data = np.stack((feature_1, feature_2, feature_3), axis=1)
kmean = KMeans(k=2)
kmean.fit(data)