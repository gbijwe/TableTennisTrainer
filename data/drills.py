import streamlit as st

def show_drills_page():
    st.title("Table Tennis Training Drills")
    
    st.write("""
    Training drills are essential for improving your table tennis skills. Professional players 
    spend 3-4 hours every day on drills, and they should make up at least 50% of your practice time.[5]
    
    The following drills are designed to help you develop different aspects of your game. Each drill 
    can be adjusted for different skill levels.
    """)
    
    st.header("Basic Footwork Drills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Backhand, Forehand Alternating")
        st.write("""
        **Setup**: Two players rally, with one player alternating between forehand and backhand drives/topspins.
        
        **Execution**:
        - Don't change grip between forehand and backhand strokes
        - Side shuffle into position between strokes
        - Keep a closed racket angle throughout
        - Adjust foot positioning based on target
        
        **Benefits**: Develops footwork, stroke technique, and transitions between forehand and backhand[6][16]
        """)
        
    with col2:
        st.subheader("2. Forehand (Middle), Forehand (Wide)")
        st.write("""
        **Setup**: One player plays forehand strokes from two different positions.
        
        **Execution**:
        - Play a forehand from the middle of the table
        - Move to play another forehand from the wide position
        - Continue alternating between these two positions
        
        **Benefits**: Develops footwork, particularly the challenging right-to-left movement for right-handed players[6]
        """)
    
    st.subheader("3. Random Topspin to Backhand Block")
    st.write("""
    **Setup**: One player blocks with the backhand to random locations, while the other player plays topspin shots (both forehand and backhand) always returning to the backhand side.
    
    **Execution**:
    - Blocker can block anywhere on the table
    - Topspin player must use both forehand and backhand topspin shots
    - All topspin shots must target the blocker's backhand
    
    **Benefits**: Develops footwork, switching between different topspin shots, and the ability to hit topspin from different parts of the table[16]
    """)
    
    st.header("Service and Attack Drills")
    
    st.subheader("Serve and Attack")
    st.write("""
    **Setup**: One player serves and attacks the return, while the other player focuses on service return.
    
    **Execution**:
    - Server delivers a serve (can be specified as backspin, topspin, or free choice)
    - Receiver returns the serve (can be specified as push, block, or free choice)
    - Server attacks the third ball
    
    **Benefits**:
    - Improves service quality and consistency
    - Develops recovery positioning after serving
    - Improves understanding of how your serves are returned
    - Develops the critical skill of attacking after serving
    
    This drill is essential because winning the first attack after a serve significantly increases your chances of winning the point.[16]
    """)
    
    st.header("Multiball Training")
    
    st.write("""
    Multiball training is a high-intensity form of practice where one player feeds balls continuously while the other player practices specific strokes or movements.
    
    **Basic Multiball Setup**:
    - Feeder has a basket of balls and feeds at a consistent pace
    - Player practices specific strokes or footwork patterns
    - Typically 30-50 balls per set, followed by rest
    
    **Sample Multiball Drill**: Open Up, Counter Topspin, Repeat
    - Feeder sends backspin ball to forehand
    - Player opens with a forehand loop
    - Feeder immediately sends topspin ball to backhand
    - Player counters with backhand drive/topspin
    - Pattern repeats
    
    Multiball training allows for high-volume, focused practice on specific skills and is excellent for developing technique and consistency.[5]
    """)
