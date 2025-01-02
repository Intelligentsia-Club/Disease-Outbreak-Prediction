import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


def train_model():
    # Load dataset
    data = pd.read_csv('C:/Users/kudal/PycharmProjects/DiseaseOutbreakPrediction/dataset/flu_data.csv')
    X = data[['Temperature', 'Humidity', 'Population_Density']]
    y = data['Flu_Cases']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print metrics
    print("Model Evaluation Metrics:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared (R2): {r2}")

    # Save the trained model
    joblib.dump(model, 'model/flu_predictor.pkl')


if __name__ == "__main__":
    train_model()
