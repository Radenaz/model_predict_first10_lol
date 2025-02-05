import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px

def run():
    st.title('League of Legends - First 10 Minutes EDA')
    st.write('----')
    
    st.write('This app performs Exploratory Data Analysis (EDA) on League of Legends match data to help identify features that contribute to winning.')

    # Add image
    Image1 = Image.open('League_of_Legends_Cover.jpg')
    st.image(Image1, caption='League of Legends Analysis')

    # Load dataset
    raw_csv = 'https://raw.githubusercontent.com/Radenaz/testing-one/refs/heads/main/high_diamond_ranked_10min.csv'
    data = pd.read_csv(raw_csv)
    st.write('### Raw Data')
    st.dataframe(data)

    st.write('----')
    
    # Plot - Distribution of blueWins
    st.write('## Distribution of Wins (blueWins)')
    fig1 = plt.figure(figsize=(8, 5))
    sns.countplot(x='blueWins', data=data, palette='coolwarm', hue='blueWins')
    st.pyplot(fig1)
    
    
    # Interactive Histograms
    st.write('## Interactive Histogram')
    numeric_columns = ['blueGoldDiff', 'blueKills', 'blueDeaths', 'blueAssists', 'redGoldDiff']
    selected_column = st.selectbox('Select a numerical column for histogram:', numeric_columns)

    fig2 = plt.figure(figsize=(8, 5))
    sns.histplot(data[selected_column], bins=20, kde=True, color='blue')
    st.pyplot(fig2)

    # Correlation Heatmap
    st.write('## Correlation Heatmap')
    fig3 = plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    st.pyplot(fig3)

    # Plotly scatter plot for gold difference and kills
    st.write('## Interactive Scatter Plot: Gold Difference vs Kills')
    fig4 = px.scatter(data, x='blueGoldDiff', y='blueKills', color='blueWins',
                      title='Gold Difference vs Kills',
                      hover_data=['blueWardsPlaced', 'blueTowersDestroyed'])
    st.plotly_chart(fig4)
    
    st.write('As gold difference (`blueGoldDiff`) increases, the number of kills (`blueKills`) also increases. This means that more kills comes with the advantage of more gold.')
    

    st.write('----')
    
    st.write('## Conclusion')
    st.markdown("""
    We have finished the model that can predict a win or a lost with overall accuracy score of 83%. However it still struggles to make precise prediction of class 0 or Blue Win. It sure has high score in precision to predict Red Win.

Variables that contribute to the winning, statistically, are as follow:

1. Gold Difference with enemy team :
    - The game is designed to reward fed players, especially early on, allowing them to dominate the game and winning it early.

    - HOWEVER. There are many variables that contribute to a game. From skill issues, technical ones, how easily a player is aggravated from enemies' taunts and outplays. 
2. Experience Points:
    - Fed players tend to stay in a lane/jungle longer, thus allowing them to gain more experience points from minnion kills. Itterating the previous point, the game rewards fed players, however as a game progress longer, other players may make a comeback. How? Respawn times progressively get longer as the game progress. If you can manage to isolate and take down one player at a time, you can almost certainly make a comeback.
3. Numbers of Wards placed:
    - In the last couple patch before, the dev implemented scores system that can, somewhat objectively, score players performance. One of the biggest factor is visions. Quantities and placement seems to affect your score by lots. This model proves it.

    - HOWEVER. Be mindful of the placement and how much player should spend on it.
4. Which team managed to obtain the Herald.
    - Owning a Herald will almost certainly score you a turret, providing extra golds to the whole team who manage to destroy the enemy turret.

    """)
    st.write('### Thanks for reading!. And GIT GUD!')

if __name__ == '__main__':
    run()
