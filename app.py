import pickle
import streamlit as st
from annotated_text import annotated_text, annotation

pickle_in = open("ModelAI","rb")
Classifier = pickle.load(pickle_in)

annotated_text(
    " Winning ",
    ("is", "fun but", "#8ef"),
    " those ",
    ("moments", "that you", "#afa"),
    " can ",
    ("touch", "someone’s", "#fea"),
    " life ",
    ("in", "a", "#1ef"),
    " very ",
    ("positive way", "are better", "#aba"),
)
expander = st.sidebar.beta_expander("ABOUT THE PROJECT")
expander.write("Sentiment analysis studies the subjective information in an expression, that is, the opinions, appraisals, emotions, or attitudes towards a topic, person or entity. Expressions can be classified as positive, negative, or neutral.")
expander.write("Sentiment Analysis (also known as opinion mining or emotion AI) is a sub-field of NLP ")
expander.write("This project predicts that the Review is Positive or Negtive")
expander.write("The project builds on M.L techniques(Uisng LogisticRegression)")
expander.write("We used Streamlit,numpy,pandas,pickle....ETC packages for the project")


try:
  def Predict_authentication(INT):
    prediction = Classifier.predict([INT])
    print(prediction)
    return prediction
  def main():
    html_temp = """
        <style>
         h2 {
        color: white ; 
        text-align:center;
         }
        body{
         background-image: url("https://media4.giphy.com/media/pcN9RH7X2Ah7G/giphy.gif");  
         border-radius:25px; 

         }
        </style>
        <body>
        <h2>Hotel Review's Prediction Application<h2>
        </body>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    if st.checkbox('AGREE TERMS AND CONDITIONS,[THIS WAS A PROTO TYPE]'):
         #INT = st.text_input("Enter The Hotel Review","")
         INT = st.text_area('Enter The Hotel Review',)
         result=""
         if st.button('Predict'):
                  result = Predict_authentication(INT)
         if (result=='not happy'):
                  st.info("It's a Negtive Review")
                  st.success('Provide a great service')
                  st.error("Add more lines of communication")
         elif (result=='happy'):
                  st.info("It's a Positive Review")
                  st.success('Well done')   
                  st.balloons()               
  if __name__=='__main__':
   main()
except:
    st.error("Enter All Values Please")
    st.info('Referesh The APP') 

if st.button('About Me'):
  st.error('SANKARANA CHAKRADHAR NAIDU')
  st.info('B.TEC-VITAP UNIVERSITY')
  """Gmail:"""
  st.code('''chakradhar2307@gmail.com''')
  '''LinkedinID'''
  st.code('''https://www.linkedin.com/in/sankarana-chakradhar-naidu-75144b18b/''')
  st.success('HAPPY CODING \U0001F600 \U0001F600 \U0001F600')
  print('')
  
  