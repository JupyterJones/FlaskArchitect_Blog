:import "fmt"

:import "github.com/sjwhitworth/golearn/base"

:import "github.com/sjwhitworth/golearn/evaluation"

:import "github.com/sjwhitworth/golearn/knn"

// Load in a dataset, with headers. Header attributes will be stored.
// Think of instances as a Data Frame structure in R or Pandas.
// You can also create instances from scratch.
rawData, err := base.ParseCSVToInstances("/usr/local/lib/python2.7/dist-packages/pandas/io/tests/data/iris.csv
", false)

//Initialises a new KNN classifier
cls := knn.NewKnnClassifier("euclidean", 2)

//Do a training-test split
trainData, testData := base.InstancesTrainTestSplit(rawData, 0.50)
cls.Fit(trainData)

//Calculates the Euclidean distance and returns the most popular label
predictions := cls.Predict(testData)

// Calculate precision/recall metrics, and summarize results
confusionMat, err := evaluation.GetConfusionMatrix(testData, predictions)
fmt.Println(evaluation.GetSummary(confusionMat))



