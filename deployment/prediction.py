# model deployment
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open('best_model_milestone2.pkl', 'rb') as file:
    model = pickle.load(file)

# List of expected features
expected_features = [
    'blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths', 
    'blueAssists', 'blueGoldDiff', 'blueExperienceDiff', 'blueTowersDestroyed', 
    'blueTotalGold', 'blueTotalMinionsKilled', 'blueTotalJungleMinionsKilled', 'blueAvgLevel', 
    'blueDragons', 'blueHeralds', 'redWardsPlaced', 'redWardsDestroyed', 'redFirstBlood', 
    'redKills', 'redDeaths', 'redAssists', 'redGoldDiff', 'redExperienceDiff', 
    'redTowersDestroyed', 'redTotalExperience', 'redTotalJungleMinionsKilled', 
    'redDragons', 'redHeralds'
]

def run():
    st.title('League of Legends Win Prediction')
    st.write('Input match statistics from the first 10 minutes to predict if the **Blue Team will win**.')

    # Input form
    with st.form(key='form_lol_prediction'):
        st.subheader('Blue Team Statistics')
        blueWardsPlaced = st.number_input('Blue Wards Placed', min_value=0, step=1)
        blueWardsDestroyed = st.number_input('Blue Wards Destroyed', min_value=0, step=1)
        blueFirstBlood = st.radio('Blue First Blood', [0, 1])
        blueKills = st.number_input('Blue Kills', min_value=0, step=1)
        blueDeaths = st.number_input('Blue Deaths', min_value=0, step=1)
        blueAssists = st.number_input('Blue Assists', min_value=0, step=1)
        blueGoldDiff = st.number_input('Blue Gold Difference', step=1)
        blueExperienceDiff = st.number_input('Blue Experience Difference', step=1)
        blueTowersDestroyed = st.number_input('Blue Towers Destroyed', min_value=0, step=1)
        blueTotalGold = st.number_input('Blue Total Gold', min_value=0, step=1)
        blueTotalMinionsKilled = st.number_input('Blue Total Minions Killed', min_value=0, step=1)
        blueTotalJungleMinionsKilled = st.number_input('Blue Total Jungle Minions Killed', min_value=0, step=1)
        blueAvgLevel = st.number_input('Blue Average Level', min_value=0.0, step=0.1)
        blueDragons = st.number_input('Blue Dragons', min_value=0, step=1)
        blueHeralds = st.number_input('Blue Heralds', min_value=0, step=1)

        st.subheader('Red Team Statistics')
        redWardsPlaced = st.number_input('Red Wards Placed', min_value=0, step=1)
        redWardsDestroyed = st.number_input('Red Wards Destroyed', min_value=0, step=1)
        redFirstBlood = st.radio('Red First Blood', [0, 1])
        redKills = st.number_input('Red Kills', min_value=0, step=1)
        redDeaths = st.number_input('Red Deaths', min_value=0, step=1)
        redAssists = st.number_input('Red Assists', min_value=0, step=1)
        redGoldDiff = st.number_input('Red Gold Difference', step=1)
        redExperienceDiff = st.number_input('Red Experience Difference', step=1)
        redTowersDestroyed = st.number_input('Red Towers Destroyed', min_value=0, step=1)
        redTotalExperience = st.number_input('Red Total Experience', min_value=0, step=1)
        redTotalJungleMinionsKilled = st.number_input('Red Total Jungle Minions Killed', min_value=0, step=1)
        redDragons = st.number_input('Red Dragons', min_value=0, step=1)
        redHeralds = st.number_input('Red Heralds', min_value=0, step=1)

        st.markdown("---")
        submitted = st.form_submit_button('Predict')

    # Prepare input data
    input_data = pd.DataFrame([{
        'blueWardsPlaced': blueWardsPlaced,
        'blueWardsDestroyed': blueWardsDestroyed,
        'blueFirstBlood': blueFirstBlood,
        'blueKills': blueKills,
        'blueDeaths': blueDeaths,
        'blueAssists': blueAssists,
        'blueGoldDiff': blueGoldDiff,
        'blueExperienceDiff': blueExperienceDiff,
        'blueTowersDestroyed': blueTowersDestroyed,
        'blueTotalGold': blueTotalGold,
        'blueTotalMinionsKilled': blueTotalMinionsKilled,
        'blueTotalJungleMinionsKilled': blueTotalJungleMinionsKilled,
        'blueAvgLevel': blueAvgLevel,
        'blueDragons': blueDragons,
        'blueHeralds': blueHeralds,
        'redWardsPlaced': redWardsPlaced,
        'redWardsDestroyed': redWardsDestroyed,
        'redFirstBlood': redFirstBlood,
        'redKills': redKills,
        'redDeaths': redDeaths,
        'redAssists': redAssists,
        'redGoldDiff': redGoldDiff,
        'redExperienceDiff': redExperienceDiff,
        'redTowersDestroyed': redTowersDestroyed,
        'redTotalExperience': redTotalExperience,
        'redTotalJungleMinionsKilled': redTotalJungleMinionsKilled,
        'redDragons': redDragons,
        'redHeralds': redHeralds
    }])

    # Display input data
    st.write('### Input Data:')
    st.dataframe(input_data)

    # Prediction process
    if submitted:
        # Make predictions
        prediction = model.predict(input_data)

        # Display prediction
        result = "Win" if prediction[0] == 1 else "Lose"
        st.write(f'### Prediction: The Blue Team will **{result}**!')

if __name__ == '__main__':
    run()
