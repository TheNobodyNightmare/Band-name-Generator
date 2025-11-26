from sklearn.cluster import KMeans

marks = [[35],[78],[52],[90],[20]]
k = KMeans(n_clusters=3)
k.fit(marks)

print(k.labels_)
