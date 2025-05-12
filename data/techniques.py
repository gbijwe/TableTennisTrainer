import streamlit as st

def show_techniques_page():
    st.title("Table Tennis Techniques")
    
    tab1, tab2, tab3 = st.tabs(["Grips", "Strokes", "Spins"])
    
    with tab1:
        st.header("Types of Grips")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Shakehand Grip")
            st.write("""
            The shakehand grip is the most common grip in Western countries and among professional players.[12][17]
            
            The racket rests on the V-shape created by the thumb and index finger, with the index finger lying roughly 
            parallel with the edge of the rubber at the base of the paddle.[12]
            
            **Variations:**
            - **Shallow Shakehand**: Thumb rests on the blade
            - **Deep Shakehand**: Thumb rests on the rubber[12]
            
            **Advantages:**
            - Easier to learn for beginners
            - Good balance between forehand and backhand play
            - More versatile for different playing styles[4][17]
            """)
            
        with col2:
            st.subheader("Penhold Grip")
            st.write("""
            In the penhold grip, the index finger and thumb wrap around the handle like holding a pen, with the other 
            fingers either curled or flat on the back side of the racket.[4]
            
            **Variations:**
            - **Traditional Penhold**: Fingers curled on the back for more wrist flexibility
            - **Reverse Backhand Penhold**: Fingers flat on the back for better racket control[4]
            
            **Advantages:**
            - Greater wrist flexibility for forehand shots
            - Better for close-to-table play
            - Potentially faster transitions between forehand shots[4][17]
            """)
    
    with tab2:
        st.header("Types of Strokes")
        
        st.subheader("Offensive Strokes")
        st.write("""
        **1. Speed Drive**
        - A direct hit propelling the ball forward with speed rather than spin
        - Racket is primarily perpendicular to the stroke direction
        - Creates a fast shot with minimal arc[2]
        
        **2. Loop**
        - Racket is parallel to the stroke direction to create topspin
        - Ball travels in an arc and jumps forward upon landing
        - Essential attacking stroke in modern table tennis[2]
        
        **3. Counter Drive**
        - High loop drives hit immediately after the ball bounces
        - Ball travels faster due to minimal backswing
        - Used to counter an opponent's topspin[2]
        
        **4. Flick**
        - Quick wrist action to attack short balls
        - Used when there's no room for a full backswing
        - Can resemble a drive or loop in effect[2]
        
        **5. Smash**
        - Powerful attack on high or close-to-net returns
        - Uses large backswing and rapid acceleration
        - Maximum speed with minimal spin[2]
        """)
        
        st.subheader("Defensive Strokes")
        st.write("""
        **1. Block**
        - Passive stroke that uses the opponent's power
        - Racket positioned to redirect the ball
        - Minimal movement, relies on timing and angle
        
        **2. Push**
        - Used against backspin balls
        - Creates underspin by brushing under the ball
        - Typically used to keep the ball low and prevent attacks
        
        **3. Chop**
        - Defensive backspin stroke
        - Racket moves from high to low, brushing under the ball
        - Creates heavy backspin to make attacking difficult
        """)
    
    with tab3:
        st.header("Types of Spins")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Topspin")
            st.write("""
            - Ball rotates with the top moving forward, bottom backward
            - Creates a strong arch in the trajectory
            - Makes the ball dip downward after reaching peak height
            - When it hits the table, the ball jumps forward[3]
            
            **How to create**: Brush up and over the ball in a forward motion
            """)
            
            st.subheader("Sidespin")
            st.write("""
            Two types of sidespin:
            
            **Around vertical axis:**
            - Ball curves in flight
            - Used for service and attacking strokes
            
            **Around front-to-back axis:**
            - Ball flies relatively straight
            - Bounces sharply sideways on the table[3]
            
            **How to create**: Brush the side of the ball in a horizontal motion
            """)
            
        with col2:
            st.subheader("Underspin/Backspin")
            st.write("""
            - Ball rotates with the bottom moving forward, top backward
            - Creates a flat trajectory
            - Ball tends to float and then drop downward
            - When it hits the table or racket, the ball drops down[3]
            
            **How to create**: Brush under the ball in a backward motion
            """)
            
            st.subheader("Combined Spins")
            st.write("""
            Most shots in table tennis combine different spin components:
            
            - **Topspin + Sidespin**: Ball curves and jumps forward
            - **Backspin + Sidespin**: Ball curves and stops/moves backward
            - **No-spin** (appearing like spin): Deceptive technique to confuse opponents
            
            The proportion of each spin component affects the ball's behavior on contact with the table and racket.[3]
            """)
