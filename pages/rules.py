import streamlit as st

def show_rules_page():
    st.title("Official Table Tennis Rules")
    
    st.header("Basic Game Rules")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Scoring")
        st.write("""
        - Games are played to 11 points[1]
        - Players serve two serves each, alternating[1]
        - If a game ties at 10-10, a player must win by 2 points[1]
        - In competition, games are played best of 5 (first to win 3 games) or best of 7 (first to win 4 games)[15]
        """)
        
    with col2:
        st.subheader("Serving")
        st.write("""
        - You must throw the ball up straight, from a flat palm, at least 6 inches (16cm)[1][15]
        - Your toss and service contact must be behind the table surface (not over)[15]
        - You cannot hide the ball with any part of your body during service[15]
        - If the ball hits the net during service, it is a let, the point is replayed[15]
        """)
    
    st.header("Equipment Specifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Table Dimensions")
        st.write("""
        - Length: 2.74m (9ft)[15][20]
        - Width: 1.525m (5ft)[15][20]
        - Height: 76cm (2.5ft)[15][20]
        - Net height: 15.25cm (6 inches)[15][20]
        """)
        
    with col2:
        st.subheader("Ball Specifications")
        st.write("""
        - Diameter: 40mm[14]
        - Weight: 2.7 grams[14]
        - Material: Celluloid or plastic[14]
        - Color: Orange or white (for visibility)[14]
        """)
    
    st.header("Playing a Match")
    st.write("""
    In official competitions, matches are typically played as best of 5 or best of 7 games. 
    Each game is played to 11 points, with players serving two serves each in alternation.
    If the score reaches 10-10, players then alternate serving one serve each until one player 
    leads by 2 points and wins the game.[1][15]
    
    The winner of a match is the first player to win the majority of the maximum number of games 
    (e.g., 3 games in a best of 5, 4 games in a best of 7).[15]
    """)
