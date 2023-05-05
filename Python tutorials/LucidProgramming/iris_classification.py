# Iris Classification Model: Machine learning model that will allow us to
# classify species of iris flowers. This application will introduce many
# rudimentary features and concepts of machine learning and is a good use case
# for these types of models.

# Use case: Botanist wants to determine the species of an iris flower based on
# characteristics of that flower. For instance attributes including petal
# length, width, etc. are the "features" that determine the classification of a
# given iris flower.

from sklearn.datasets import load_iris

iris = load_iris()

#print(iris.keys())
#print(iris)

print(iris["DESCR"])
