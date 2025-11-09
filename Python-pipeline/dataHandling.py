import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from scipy import stats 

# TODO: Add functionality to handle duplicates in the datasets by taking the rows that contain duopicates, calculating averages and replacing the rows containing duplicates with just 1 row containing the averages. 
# TODO: Print to check that the data has been handled correctly and is ready to inserted in the master data table. 
# TODO: Add functionality to handle outliers in the datasets by eliminating the rows containing outliers. 
# TODO: Add funmctionality to handle missing values in rows. 

filePath =[
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/Diabetes data 1.csv',
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/insufficient physical activity.csv',
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/Prevalence of obesity.csv'
]

datasets = []
for path in filePath:
    print(f"Loading data from: {path}")

class DataHandler:
    
    def __init__(self, filePath):
        self.filePath = filePath 
        self.extractData()
        self.handleMv() 
        self.outlierDt()
   
    def extractData(self):
        """Load data from a CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(self.filePath)
        return self.data 
    
    def handleMv(self): 
        """Handle missing values in the dataset by removing the row containing the missing value."""
        threshold = 0.4 #Define a threshold for missing values per column 
        for i in self.data.columns:
            missingRt = self.data[i].isnull().mean()
            if missingRt >= threshold:
                self.data = self.data.drop(columns=[i])

    #def handleDp(self):
       # """Handle duplicate values in each dataset by removing the rows containing duplicates."""
        #for i in range(len(self.data.columns)):
            #if self.data.iloc[:, i].duplicated().any(): 

    def outlierDt(self):
        """Check outliers in each dataset""" 
        print(self.data.shape)
        print(self.data.head()) 

        self.numericData = self.data.select_dtypes(include=[np.number])
        plt.figure
        sns.boxplot(data=self.numericData)
        plt.xticks(rotation=45)
        plt.title(f"Boxplots for each dataset feature: {path}")
        plt.show() 

        # Using Z-score method to detect outliers
        zScores = np.abs(stats.zscore(self.numericData))
        outliersZ = np.where(zScores > 3)

        print(f"Outliers detected using Z-score method: {outliersZ}") 

  

#Create a data handler object for each dataset to extract and transform the data
for path in filePath:
        handler = DataHandler(path)
        df = handler.extractData()
        datasets.append(df) 