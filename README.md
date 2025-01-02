# Disease Outbreak Prediction

This repository contains a Flask-based web application for predicting disease outbreaks using machine learning. The model predicts flu cases based on three input features: temperature, humidity, and population density.

## Project Structure

The project consists of the following main components:

```
Intelligentsia-Club-Disease-Outbreak-Prediction/
├── LICENSE
├── run.py
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── __pycache__/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   └── templates/
│       └── predict.html
├── dataset/
│   └── flu_data.csv
└── model/
    ├── flu_predictor.pkl
    └── train_model.py
```

### Files:
- **LICENSE**: The project is licensed under the MIT License.
- **run.py**: The entry point for the Flask application.
- **app/**: Contains the Flask app with routes and templates.
- **dataset/**: Contains the dataset used for training the model.
- **model/**: Contains the trained model and code for training.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Intelligentsia-Club/Disease-Outbreak-Prediction.git
   cd Disease-Outbreak-Prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. To train the model, run:
   ```bash
   python model/train_model.py
   ```

## Usage

1. To run the Flask application, execute:
   ```bash
   python run.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`.

3. The homepage will display a form asking for:
   - Temperature (°C)
   - Humidity (%)
   - Population Density (per km²)

   After submitting the form, the model will predict the flu cases and display the result.

4. The predictions will be stored in the session and visualized in a line chart.

## Dataset

The dataset `flu_data.csv` contains historical data for flu cases along with features such as temperature, humidity, and population density. It is used to train the machine learning model.

Example data columns:

- **Temperature**: Temperature in degrees Celsius
- **Humidity**: Humidity percentage
- **Population_Density**: Population density in per km²
- **Flu_Cases**: Number of flu cases in the region

## Model

The machine learning model (`flu_predictor.pkl`) is trained using the data from `flu_data.csv`. The model is built using [scikit-learn](https://scikit-learn.org/) and saved as a `.pkl` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The dataset used in this project is available in the `dataset/flu_data.csv` file.
- The model is implemented using [scikit-learn](https://scikit-learn.org/).
- The web interface is built with [Flask](https://flask.palletsprojects.com/).

## Contact

For more information or inquiries, please contact [intelligentsia.techclub@gmail.com
](mailto:intelligentsia.techclub@gmail.com
).
