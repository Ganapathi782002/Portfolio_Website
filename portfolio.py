import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_javascript import st_javascript


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

st.markdown(
    """
    <style>
        .reportview-container {
            background-color: #f0f0f0;  /* Replace with your desired background color */
        }
        .navbar {
            background-color: #77DD77;  /* Replace with your desired navbar background color */
            color: white;  /* Replace with your desired navbar text color */
        }
    </style>
    """,
    unsafe_allow_html=True
)


lottie_hello="https://lottie.host/85508444-ca55-4a6c-b895-63e5f6041045/bOjL8XHgBC.json"
lottie_coder="https://lottie.host/9dc20866-03a3-4cbc-b534-a26b59e6a2c4/lExjYXgWAZ.json"
lottie_python="https://lottie.host/aa4fe987-a4b0-431c-b485-f6e9c800981b/cgWJIpP1hw.json"
lottie_ai="https://lottie.host/b181d1cc-c9b8-4c4e-a9dd-c4bd5428c5f9/nWoPkEsPH5.json"
lottie_git="https://lottie.host/07cfb211-fd7d-4bcd-885c-8c7dcf6d058c/acFHjlBWPR.json"
lottie_problem="https://lottie.host/ccbd289f-f607-43f8-83c7-f0ddb2156609/IdIDgaNGLL.json"
lottie_com="https://lottie.host/da099ffc-50ac-41e4-96ea-a26bed9df275/wBCQLkHXxw.json"
lottie_some="https://lottie.host/8f44a3cf-affa-4ac1-8e71-9b5c8824ece4/gwlbbiTpP6.json"
lottie_contact="https://lottie.host/06cc27e2-d4bb-4a36-a7e4-f205d8011d74/X1DLCyBw4Q.json"

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
  <nav class="navbar navbar-expand-lg">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-home" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-about" href="## About me">About me</a>
      </li>
      <li class="nav-item">
        <a class="nav-skills" href="## Skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-education" href="## Education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-contact" href="## Contact me">Contact me</a>
      </li>
    </ul>
  </div>
</nav>
""",unsafe_allow_html=True
)

def txt1(a,b):
    cola,colb=st.columns([6,1])
    with cola:
        st.markdown(a)
    with colb:
        st.markdown(b)
def txt2(a,b):
    cola,colb=st.columns([6,1.5])
    with cola:
        st.markdown(a)
    with colb:
        st.markdown(b)

with st.container():
    col1,col2=st.columns([3,2])
    with col1:
        st.subheader("Hey, there! :wave:")
        st.title("I am Ganapathi")
        st.subheader("Upcoming Analyst at Latent view analytics")
        st.caption("A passionate Python developer, dedicated to harnessing data-driven insights for innovative solutions.")
    with col2:
        st_lottie(lottie_coder)

# js_code = """
# <script>
#     function scrollToSection(sectionId) {
#         const element = document.getElementById(sectionId);
#         if (element) {
#             element.scrollIntoView({ behavior: 'smooth' });
#         }
#     }

#     document.addEventListener('DOMContentLoaded', function() {
#         document.getElementById('nav-home').addEventListener('click', function() {
#             scrollToSection('hey-there');
#         });

#         document.getElementById('nav-about').addEventListener('click', function() {
#             scrollToSection('about-me');
#         });

#         document.getElementById('nav-skills').addEventListener('click', function() {
#             scrollToSection('skills');
#         });

#         document.getElementById('nav-education').addEventListener('click', function() {
#             scrollToSection('education');
#         });

#         document.getElementById('nav-contact').addEventListener('click', function() {
#             scrollToSection('contact-me');
#         });
#     });
# </script>
# """

# # Inject the JavaScript code
# st.markdown(js_code, unsafe_allow_html=True)
        

st.markdown("## About me")
with st.container():
    col3,col4=st.columns(2)
    with col3:
        st.write("##### I'm a dedicated towards Big data and Python developer with an insatiable curiosity for emerging technologies and Python APIs like Streamlit and Pyspark. My passion lies in the relentless pursuit of knowledge, constantly uplifting my Python skills while venturing into the exciting realms of tech exploration.")
    with col4:
        st.write("##### I have interest in competitive programming and participating in hackathons with a passion for problem-solving and a deep fascination for learning things by working in teams. I thrive on constant learning, spending hours brainstorming solutions to complex challenges.")

st.markdown("## Skills")
with st.container():
    col5,col6=st.columns([3,1])
    with col5:
        st.subheader("""
        Hard Skills
        - **Python**
            - Mastering APIs such as Streamlit and Pyspark for analyzing data to gain actionable insights and make accurate decisions
            - Using extensive libraries such as numpy and pandas to manage a lot of data and analyse the data to generate problem-solving solutions
        - **Machine Learning**
            - Using extensive data available to automate tasks and make informative solutions
            - Creating innovative ideas and increasing efficiency across various fields
        - **Git / GitHub**
            - Contributing to open-source platforms and learning to deal with problems
            - Using git to manage data, version-tracking, history management and organized data management for increased productivity
        - **Big data**
            - Using **Apache Splunk** for log analysis, monitoring, and gaining insights from large datasets, creating alerts, and integrating with various data sources
            - Using **PySpark** (a Python API for Apache Spark) with streaming capabilities are particularly useful for applications that require real-time analytics, monitoring, and decision-making based on continuously changing data.
            """)
    with col6:
        st_lottie(lottie_python )
        st_lottie("\n",lottie_python)
        st_lottie(lottie_git)
        st_lottie("\n",lottie_python)
        st_lottie(lottie_problem)
        
with st.container():
    col11,col12=st.columns([3,1])
    with col11:
        st.subheader("""
                    Soft Skills
                    - **Problem-solving**
                        - Active participation in competitive coding in platforms such as GeeksforGeeks and Leetcode
                        - Solving Sudoku on a frequent basis and puzzles such as Wordle, Crosswords
                    - **Communication**
                        - English
                        - Tamil
                    - **Content writing**
                        - Actively wrting and creating contents and posts for college clubs and events as a part of our creativity **(Fine arts Club - PSG Tech)**
                        - Writing diaries and sharing my thoughts and writing skills with others
                    - **Other activities** 
                        - Active participation in sports such as Badminton, Cricket, Football and Carrom
                        - Reading books in leisure time oftenly, Gardening, Travelling to new places
                        """)
    with col12:
        st_lottie("\n",lottie_python)
        st_lottie(lottie_some)
        st_lottie(lottie_com)
        st_lottie(lottie_ai)
        
st.markdown("## Education")
txt1("##### **PSG College of Technology**, Coimbatore","*CGPA: 8.62*")
txt2("###### *B.E in Computer Science and Engineering*","Aug'20 - Jun'24")
txt2("\n ##### **Elite Matriculation Higher Secondary School**, Chennai","*Percentage: 96.16*")
txt1("###### *Higher Secondary Education (12th)*   ","    2019-2020")
st.markdown("## Contact me")
with st.container():
    col13,col14=st.columns([1.2,2])
    with col13:
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">  <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/><path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"/></svg> Redhills, Chennai, 600052',unsafe_allow_html=True)
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-at" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 0-2 2v8.01A2 2 0 0 0 2 14h5.5a.5.5 0 0 0 0-1H2a1 1 0 0 1-.966-.741l5.64-3.471L8 9.583l7-4.2V8.5a.5.5 0 0 0 1 0V4a2 2 0 0 0-2-2H2Zm3.708 6.208L1 11.105V5.383l4.708 2.825ZM1 4.217V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v.217l-7 4.2-7-4.2Z"/><path d="M14.247 14.269c1.01 0 1.587-.857 1.587-2.025v-.21C15.834 10.43 14.64 9 12.52 9h-.035C10.42 9 9 10.36 9 12.432v.214C9 14.82 10.438 16 12.358 16h.044c.594 0 1.018-.074 1.237-.175v-.73c-.245.11-.673.18-1.18.18h-.044c-1.334 0-2.571-.788-2.571-2.655v-.157c0-1.657 1.058-2.724 2.64-2.724h.04c1.535 0 2.484 1.05 2.484 2.326v.118c0 .975-.324 1.39-.639 1.39-.232 0-.41-.148-.41-.42v-2.19h-.906v.569h-.03c-.084-.298-.368-.63-.954-.63-.778 0-1.259.555-1.259 1.4v.528c0 .892.49 1.434 1.26 1.434.471 0 .896-.227 1.014-.643h.043c.118.42.617.648 1.12.648Zm-2.453-1.588v-.227c0-.546.227-.791.573-.791.297 0 .572.192.572.708v.367c0 .573-.253.744-.564.744-.354 0-.581-.215-.581-.8Z"/></svg> ganapathikannikeswaran@gmail.com',unsafe_allow_html=True)
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-phone-fill" viewBox="0 0 16 16"><path d="M3 2a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V2zm6 11a1 1 0 1 0-2 0 1 1 0 0 0 2 0z"/></svg> Phone: +91 6383146519',unsafe_allow_html=True)
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/></svg> https://www.linkedin.com/in/ganapathi-kannikeswaran-b5356b1bb/',unsafe_allow_html=True)
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg> https://github.com/Ganapathi782002',unsafe_allow_html=True)
        st.write('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16"><path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/></svg> https://twitter.com/havoc_782002',unsafe_allow_html=True)
    with col14: 
        st_lottie(lottie_contact)
        
