import pandas as pd 

class DataHandler:
    def __init__(self, filePath):
        self.filePath = filePath 
        
    def extract_data(self):
        """Load data from a CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(self.filePath)
        return self.data 
    
     #Define the path of all the data sources 
filePath = [
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/Diabetes data 1.csv',
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/insufficient physical activity.csv',
    '/Users/rlealjerak/Documents/Data-Pipeline/Python-pipeline/Data/Prevalence of obesity.csv'
]
#Check that the data has been loaded correctly 
datasets = []
for path in filePath:
    print(f"Loading data from: {path}")
    handler = DataHandler(path)
    data = handler.extract_data()
    datasets.append(data) 