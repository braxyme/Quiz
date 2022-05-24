import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser as wbb

flag = False

st.header('Quiz App')
st.subheader('Time to put on your thinking caps!')
st.markdown('''___''')

rt = False

#can - dict for all
#6 ques
#research on how to publish python website


nme = st.text_input('Enter your Name')

eml = st.text_input('Enter your Email')

if st.button('submit'):
    if nme == '':
        flag = True

st.markdown('''___''')

dict = {
    'a. Who is the founder of Apple?':['Mark Zuckerberg', 'Jeff Bezzoz', 'Steve Jobs', 'Warren Buffet'],
    'b. What is 4 to the power 4?':['234', '255', '250', '256'],
    'c. From which dynasty was Vijayalaya?': ['Mauryan', 'Cholas', 'Gupta', 'Rashtrakuta'],
    "d. Which Tense is this: 'He had been playing with his friends'":['Simple Past', 'Past Continuous', 'Past Perfect', 'Past Perfect Countinuous'],
    "e. In which language does the word 'Graias' Belong'":['Spanish', 'German', 'English', 'French'],
    'f. What does the word ajar mean':['a broken jar', 'slightly open', 'slightly cracked', 'an open door']
}

la = []

for i in dict.keys():
    if rt==True:
        flag = False
    a = st.selectbox(i, dict.get(i))
    la.append(a)

qz = 0

lst = []

a = la[0]
if a=='Steve Jobs':
    qz+=1
else:
    lst.append('a')

b = la[1]
if b=='256':
    qz+=1
else:
    lst.append('b')

c = la[2]
if c=='Cholas':
    qz+=1
else:
    lst.append('c')

d = la[3]
if d=='Past Perfect Countinuous':
    qz+=1
else:
    lst.append('d')

e = la[4]
if e=='Spanish':
    qz+=1
else:
    lst.append('e')

f = la[5]
if f=='slightly open':
    qz+=1
else:
    lst.append('f')

st.write('')
st.write('Take help from')
#Another Method with Button
webb = 'https://www.google.com/'
if st.button('Google'):
    wbb.open_new_tab(webb)

st.markdown('''___''')

if st.button('Done!'):
    st.snow()
    st.write('')
    st.info('Score: '+ str(qz))
    if len(lst)>0:
        st.write('Wrong Answers', lst)
    with st.expander('See Explanation for a'):
        st.write('Steve Jobs found Apple in 1977')
        st.markdown('''___''')
        st.image('https://th.bing.com/th/id/OIP.ZMCbWtUaD7Jv-rJfdHR93QHaFj?w=253&h=190&c=7&r=0&o=5&dpr=1.25&pid=1.7')
    with st.expander('See Explanation for b'):
        st.write('4x4 = 16, 16x4 = 64, 64x4 = 256')
        st.markdown('''___''')
        st.image('https://i.pinimg.com/originals/0b/01/f4/0b01f49f6c609fc9e03a59284303f3c2.jpg')
    with st.expander('See Explanation for c'):
        st.write('Vijayalaya(from an old family of Cholas) captured the Kaveri Delta from Muttaraiyar and his further '
                 'generations captured the neighbouring areas')
        st.markdown('''___''')
        st.image('https://1.bp.blogspot.com/-epNYUdIae7c/WWeIx2nS_WI/AAAAAAAAAj8/JJVSwOHqovg0oJSW-F5rkowsP9WqOIHtwCLcBGAs/s1600/19983995_1357551827690690_3692184353615264635_o.jpg', )
    with st.expander('See explination for d'):
        st.write('The sentence had verb+ing, been and had which makes it past perfect continuous')
        st.markdown('''___''')
        st.image('https://eslgrammar.org/wp-content/uploads/2019/05/Past-Perfect-Continuous-1.jpg', )
    with st.expander('See explination for e'):
        st.write("Gracias is a spanish word which means 'Thank You'")
        st.markdown('''___''')
        st.image('https://st3.depositphotos.com/1266988/18149/v/1600/depositphotos_181498006-stock-illustration-muchas-gracias-spanish-thank-you.jpg', )
    with st.expander('See explination for f'):
        st.write('In the oxford dictionary ajar means sligtly open')
        st.markdown('''___''')
        st.image('https://media.tenor.com/images/e4d895552f3844d1bb4c6a4c5c3105ec/tenor.gif', )

st.write('')
st.write('')
st.subheader('Comments')
st.write('')
