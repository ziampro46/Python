import streamlit as st
# title() -- it will display a big title in web page
st.title("My First Streamlit App")
#write()--> it will normal text on the web page
st.write("Hello world")
st.write("Learning streamlit is fun")

st.title("😎 Exploring Streamlit Widget")
st.header("Another section")
st.write("This is **Bold Text** and this is an *Italic Text*")

st.header("Number Slider")
age = st.slider("Select Your Age",1,100,30) # min max defaultValue
st.write("Your Age is 🧑‍🦳: ", age)
st.header("taking an user input:")
name = st.text_input("What's Your Name ?")
if name:
    st.success(f"Nice To Meet You {name} 😍")

st.header("Streamlit Button")
if st.button("Click Me!"):
    st.balloons() # pops balloon animation

st.header("Markdown")
st.markdown("Hi I am **Markdown** method of *Streamlit*")

# markdown can be used for HTML content
st.markdown("""
<h3>HTML Tag</h3>
<p>This is a paragraph</p>
""",unsafe_allow_html=True)

st.markdown("""
<p>Learn More About Streamlit Using :  
            <a href="https://streamlit.io/" title="Streamlit Official Docs">Streamlit</a> Link</p>
""",unsafe_allow_html=True)

st.header("Streamlit Code")
code1 = '''
def hello():
    print('I am the function')
'''
 
st.code(code1,language="python")
 
# latex() --> used to show ML Formula's
st.latex("(a+b)^2 = a^2 + b^2 + 2*a*b")
st.latex(r"\frac {1}{1+e^-score}")

# to stop ctrl + c
# to start streamlit run firstapp.py