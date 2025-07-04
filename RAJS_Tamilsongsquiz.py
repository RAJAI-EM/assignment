import streamlit as st

# Set page title
st.set_page_config(page_title="RAJS Tamil Song Quiz", page_icon="🎶")

st.title("🎵 RAJs Tamil Songs Quiz")
st.write("Test your knowledge of Tamil movie songs!")

# Define quiz questions
questions = [
    {
        "question": "Which movie features the song 'Munbe Vaa'?",
        "options": ["Vaaranam Aayiram", "Sillunu Oru Kaadhal", "Ghajini", "OK Kanmani"],
        "answer": "Sillunu Oru Kaadhal"
    },
    {
        "question": "Who sang the song 'Why This Kolaveri Di'?",
        "options": ["Anirudh", "Simbu", "Dhanush", "Yuvan Shankar Raja"],
        "answer": "Dhanush"
    },
    {
        "question": "Which composer created 'Enna Solla Pogirai'?",
        "options": ["A. R. Rahman", "Yuvan Shankar Raja", "Ilaiyaraaja", "Harris Jayaraj"],
        "answer": "Harris Jayaraj"
    },
    {
        "question": "The song 'Vaathi Coming' is from which movie?",
        "options": ["Master", "Bigil", "Mersal", "Sarkar"],
        "answer": "Master"
    },
    {
        "question": "Which movie has the song 'Pachai Nirame'?",
        "options": ["Alaipayuthey", "Roja", "Kaatru Veliyidai", "Vinnaithaandi Varuvaayaa"],
        "answer": "Alaipayuthey"
    },
]

score = 0
user_answers = []

# Loop through each question
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    user_answer = st.radio("Choose your answer:", q['options'], key=i)
    user_answers.append(user_answer)

# Submit button
if st.button("Submit Quiz"):
    score = sum(user_answers[i] == questions[i]['answer'] for i in range(len(questions)))
    
    st.success(f"🎉 You scored {score} out of {len(questions)}!")

    for i, q in enumerate(questions):
        result = "✅ Correct" if user_answers[i] == q['answer'] else f"❌ Wrong (Answer: {q['answer']})"
        st.write(f"**Q{i+1}:** {result}")
