import streamlit as st

def show_mental_game_page():
    st.title("The Psychological Aspects of Table Tennis")
    
    st.write("""
    Table tennis is as much a mental game as it is physical. Beyond technical skills and physical 
    ability, the psychological aspects of the game often determine who wins matches, especially 
    between players of similar technical ability.[13]
    """)
    
    st.header("Mental Toughness")
    
    st.write("""
    Mental toughness is the ability to stay focused, confident, and resilient, especially under pressure. 
    In the fast-paced, intense environment of table tennis, mental toughness is essential.[13]
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Maintaining Focus")
        st.write("""
        Focus is about centering your attention on the present task and not letting your mind wander 
        to past mistakes or future outcomes.[13]
        
        **Tips for improving focus:**
        - Develop pre-point routines to reset your mind
        - Practice mindfulness techniques during training
        - Use visualization to prepare for matches
        - Break the match down into small segments
        - Focus on the process rather than results
        """)
        
        st.subheader("Building Confidence")
        st.write("""
        Confidence is crucial in table tennis and is built through consistent practice, positive 
        self-talk, and visualization techniques.[13]
        
        **Techniques to build confidence:**
        - Acknowledge past successes
        - Practice visualization of successful execution
        - Use positive affirmations
        - Set achievable goals and celebrate small wins
        - Identify and develop your strengths
        """)
        
    with col2:
        st.subheader("Resilience Under Pressure")
        st.write("""
        Resilience is the ability to recover quickly from setbacks. In table tennis, players often face 
        challenging situations where they might lose points in succession.[13]
        
        **Strategies for building resilience:**
        - Accept that mistakes are part of the game
        - Learn from each point rather than dwelling on it
        - Practice pressure situations during training
        - Develop breathing techniques to manage stress
        - Reframe challenges as opportunities to grow
        """)
        
        st.subheader("Managing Emotions")
        st.write("""
        Emotional control is vital in table tennis, as excessive emotions can impair decision-making 
        and technique.
        
        **Techniques for emotional management:**
        - Recognize emotional triggers
        - Develop strategies for different emotional states
        - Use controlled breathing to regulate emotions
        - Maintain consistent body language regardless of the score
        - Practice acceptance of uncontrollable factors
        """)
    
    st.header("Strategic Thinking")
    
    st.write("""
    Strategic thinking involves analyzing your opponent's strengths and weaknesses, identifying 
    patterns, and making tactical adjustments during a match.
    
    **Key elements of strategic thinking:**
    
    1. **Pre-match preparation**: Study potential opponents' playing styles and preferences
    2. **Pattern recognition**: Identify recurring patterns in your opponent's play
    3. **Tactical flexibility**: Willingness to adjust your strategy based on what's working
    4. **Time management**: Using timeouts and between-point routines strategically
    5. **Risk assessment**: Knowing when to play safe vs. when to take calculated risks
    
    Developing strong strategic thinking skills allows you to maximize your technical abilities 
    and exploit opponents' weaknesses.
    """)
