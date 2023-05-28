import pickle
import pandas as pd
from explainerdashboard import ExplainerDashboard, ClassifierExplainer, ExplainerHub
from xaipreprocessing import preprocess_data

# Load the models
with open("../Models/logistic_regression_model.pkl", "rb") as file:
    log_reg_model = pickle.load(file)

with open("../Models/random_forest_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Load and preprocess the data
df = pd.read_csv('../data/airlines_delay_cleaned.csv')

X_train, X_test, y_train, y_test = preprocess_data(df)

# Convert sparse matrix to DataFrame
X_train_df = pd.DataFrame.sparse.from_spmatrix(X_train)
X_test_df = pd.DataFrame.sparse.from_spmatrix(X_test)

# Create Explainer instances for each model
explainer1 = ClassifierExplainer(log_reg_model, X_test_df, y_test)
explainer2 = ClassifierExplainer(rf_model, X_test_df, y_test)

db1 = ExplainerDashboard(explainer1)
db2 = ExplainerDashboard(explainer2)
hub = ExplainerHub([db1, db2])
hub.run()
