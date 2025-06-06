import pandas as pd
import joblib

# Load the crop recommendation model
crop_model = joblib.load('./models/crop_rotation_recommendation_model.pkl')

# Define mappings

soil_type_mapping = {
    'Loamy': 1,
    'Clayey': 2,
    'Sandy': 3,
    'Saline': 4,
}

crop_mapping = {
    'Corn': 0,
    'Rice': 1,
    'Maize': 2,
    'Peach': 3,
    'Bell Pepper': 4,
    'Potato': 5,
    'Soybean': 6,
    'Tomato': 7,
    'Chilli': 8
}

def recommend_crop(data):
    try:
        # Extract features from the data
        previous_crop = data.get('Previous Crop')
        soil_type = data.get('Soil Type')
        moisture_level = data.get('Moisture Level')
        nitrogen = data.get('Nitrogen (N)')
        phosphorus = data.get('Phosphorus (P)')
        potassium = data.get('Potassium (K)')

        # Prepare data for prediction
        input_data = pd.DataFrame([{
            "Previous Crop": crop_mapping.get(previous_crop, -1),  # Map to integer
            "Soil Type": soil_type_mapping.get(soil_type, -1),  # Map to integer
            "Moisture Level": moisture_level,
            "Nitrogen (N)": nitrogen,
            "Phosphorus (P)": phosphorus,
            "Potassium (K)": potassium
        }])

        # Make prediction
        print(f"Input Data: {input_data}")
        prediction = crop_model.predict(input_data)
        print(prediction)
        if prediction[0] in crop_mapping.values():
            recommended_crop = list(crop_mapping.keys())[int(prediction[0])]
        else:
            return {'Recommended Crop': 'No prediction available'}

        return {'Recommended Crop': str(recommended_crop)}

    except Exception as e:
        return {'error': str(e)}
