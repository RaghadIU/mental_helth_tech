
# src/clustering.py
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

def run_kmeans(df, n_clusters=4, random_state=42):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(df)
    return labels, kmeans

def run_dbscan(df, eps=0.5, min_samples=5):
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(df)
    return labels, db

def evaluate_silhouette(df, labels):
    if len(set(labels)) > 1:  # Need at least 2 clusters
        score = silhouette_score(df, labels)
        return score
    else:
        return None