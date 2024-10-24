import streamlit as st

# Configure Streamlit page settings
st.set_page_config(page_title="Chat With Jacky", page_icon=":airplane:", layout="centered")

# Title and introduction
st.title("🌍 JackBot - Your Tourism Guide")
st.write("Ask me anything related to tourism!")

# List of 20 tourism-related questions and answers
qa_pairs = {
     "What are the top tourist destinations in India?": 
        "Some popular destinations include Goa, Jaipur, Kerala, and the Himalayas.",
    "What are some must-visit places in Europe?": 
        "Paris, Rome, Barcelona, Amsterdam, and Santorini are great options.",
    "What documents do I need for international travel?": 
        "Passport, visa, travel insurance, and a return flight ticket are usually required.",
    "What is the best time to visit Japan?": 
        "March to May (spring) and October to November (autumn) are the best seasons.",
    "Do I need travel insurance?": 
        "Yes, it’s highly recommended for medical emergencies and trip cancellations.",
    "What is ecotourism?": 
        "Ecotourism focuses on sustainable travel that benefits the environment and local communities.",
    "Which cities in the world are known for shopping?": 
        "New York, Dubai, Milan, and Bangkok are famous for shopping experiences.",
    "How can I find budget-friendly travel options?": 
        "Look for discounts on flights, use public transport, and book hostels or Airbnbs.",
    "What are the essentials to pack for a trip?": 
        "Clothing, toiletries, a first-aid kit, power bank, and travel documents.",
    "What are some famous food destinations around the world?": 
        "Italy for pizza, Japan for sushi, Thailand for street food, and Mexico for tacos.",
    "What are the safety tips for solo travelers?": 
        "Stay aware of your surroundings, share your itinerary, and avoid risky areas at night.",
    "What are some romantic destinations for honeymoons?": 
        "Maldives, Bali, Santorini, and Paris are popular for romantic getaways.",
    "How can I avoid travel scams?": 
        "Research common scams, avoid unsolicited offers, and use trusted services only.",
    "What are some fun activities for family vacations?": 
        "Amusement parks, zoo visits, and sightseeing tours are great for families.",
    "What is cultural tourism?": 
        "It involves exploring a place’s culture, traditions, festivals, and heritage.",
    "What are the visa-free countries for Indian passport holders?": 
        "Thailand, Nepal, Maldives, and Bhutan offer visa-free or visa-on-arrival options.",
    "How can I reduce my carbon footprint while traveling?": 
        "Use public transport, avoid plastic, and support eco-friendly accommodations.",
    "What are some adventure tourism destinations?": 
        "Rishikesh for rafting, New Zealand for bungee jumping, and Switzerland for skiing.",
    "What are some travel tips during COVID-19?": 
        "Check entry requirements, carry masks, and stay updated with travel advisories.",
    "How do I plan a road trip?": 
        "Pick a route, ensure your vehicle is in good condition, and plan rest stops ahead."
}

# Initialize session state to store chat data
if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = []  # Store the questions asked

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None  # Track the selected question from sidebar

if "answer_to_display" not in st.session_state:  # Initialize answer_to_display
    st.session_state.answer_to_display = None

# Function to get the chatbot's response
def chatbot_response(user_query):
    for question, answer in qa_pairs.items():
        if user_query.lower() in question.lower():
            return answer
    return "I'm sorry, I don't have an answer for that. Please ask something else!"

# Sidebar to display and manage questions
with st.sidebar:
    st.header("📝 Questions Asked")
    
    # Display each question with a remove button
    for idx, question in enumerate(st.session_state.questions_asked):
        col1, col2 = st.columns([0.85, 0.15])
        
        with col1:
            if st.button(question, key=f"select_{idx}"):
                st.session_state.selected_question = question  # Update selected question
                # Show the answer immediately when a question is clicked
                answer = chatbot_response(question)
                st.session_state.answer_to_display = answer  # Store the answer for display
                
        with col2:
            if st.button("❌", key=f"remove_{idx}"):  # Remove question button
                st.session_state.questions_asked.pop(idx)  # Remove from the list
                if st.session_state.selected_question == question:
                    st.session_state.selected_question = None  # Clear selection
                    st.session_state.answer_to_display = None  # Clear displayed answer
                st.experimental_rerun()  # Refresh the app

# Input field for user's question
user_input = st.text_input("Ask your tourism-related question:")

# Process the user's input
if user_input:
    response = chatbot_response(user_input)
    st.session_state.questions_asked.append(user_input)
    st.session_state.selected_question = user_input  # Update the selected question
    st.session_state.answer_to_display = response  # Store the answer for display

# Display the selected question's answer (if any)
if st.session_state.answer_to_display:
    st.write(f"**Chatbot:** {st.session_state.answer_to_display}")

