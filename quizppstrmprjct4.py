import time as t
#start = t.time()

import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser as wbb

flag = True

db = pd.read_csv('quizdbase2.csv')

st.header('Quiz App')
st.subheader('Time to put on your thinking caps!')
st.markdown('''___''')

nme = st.text_input('Enter your Name')

eml = st.text_input('Enter your Email')

nme_list = []
eml_list = []
ws_list = []

# ,Assignment for saturday: Add a security system, if the name and email are already in the data then alert the user that they have took the test.
# ,Complete this comment section.
# ,Look for dead code in your codebase.
# ,Different optimization techniques.
# Use try and except to solve the database/csv error.
# ,Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

for i in range(0, len(db)):
    nme_list.append(db['Name'][i])
    eml_list.append(db['Email'][i])
    ws_list.append(db["Score"][i])

st.markdown('''___''')

dict = {
    'a. Who is the founder of Apple?': ['Mark Zuckerberg', 'Jeff Bezzoz', 'Steve Jobs', 'Warren Buffet'],
    'b. What is 4 to the power 4?': ['234', '255', '250', '256'],
    'c. From which dynasty was Vijayalaya?': ['Mauryan', 'Cholas', 'Gupta', 'Rashtrakuta'],
    "d. Which Tense is this: 'He had been playing with his friends'": ['Simple Past', 'Past Continuous', 'Past Perfect',
                                                                       'Past Perfect Countinuous'],
    "e. In which language does the word 'Graias' Belong'": ['Spanish', 'German', 'English', 'French'],
    'f. What does the word ajar mean': ['a broken jar', 'slightly open', 'slightly cracked', 'an open door']
}

la = []

for i in dict.keys():
    a = st.selectbox(i, dict.get(i))
    la.append(a)

qz = 0

lst = []

a = la[0]
if a == 'Steve Jobs':
    qz += 1
else:
    lst.append('a')

b = la[1]
if b == '256':
    qz += 1
else:
    lst.append('b')

c = la[2]
if c == 'Cholas':
    qz += 1
else:
    lst.append('c')

d = la[3]
if d == 'Past Perfect Countinuous':
    qz += 1
else:
    lst.append('d')

e = la[4]
if e == 'Spanish':
    qz += 1
else:
    lst.append('e')

f = la[5]
if f == 'slightly open':
    qz += 1
else:
    lst.append('f')

st.write('')
st.write('Take help from')
# Another Method with Button
webb = 'https://www.google.com/'
if st.button('Google'):
    wbb.open_new_tab(webb)

st.markdown('''___''')

if st.button('Done!'):
    if nme == '':
        flag = False
    if eml == '':
        flag = False

    if flag==True:
        if nme in nme_list:
            st.error('You Have Already Taken This Test. Kindly Refrain From Doing So Again')
        else:
            scr = qz
            ws_list.append(scr)
            nme_list.append(nme)
            eml_list.append(eml)
            dict = {
                'Name': list(nme_list),
                'Email': list(eml_list),
                'Score': list(ws_list)
            }
            dtfrm = pd.DataFrame(dict)
            dtfrm.to_csv('quizdbase2.csv')
            st.snow()
            st.write('')
            st.info('Score: ' + str(qz))
            if len(lst) > 0:
                st.write('Wrong Answers', lst)
            with st.expander('See Explanation for a'):
                st.write('Steve Jobs found Apple in 1977')
                st.markdown('''___''')
                st.image(
                    'https://th.bing.com/th/id/OIP.ZMCbWtUaD7Jv-rJfdHR93QHaFj?w=253&h=190&c=7&r=0&o=5&dpr=1.25&pid=1.7')
            with st.expander('See Explanation for b'):
                st.write('4x4 = 16, 16x4 = 64, 64x4 = 256')
                st.markdown('''___''')
                st.image('https://i.pinimg.com/originals/0b/01/f4/0b01f49f6c609fc9e03a59284303f3c2.jpg')
            with st.expander('See Explanation for c'):
                st.write(
                    'Vijayalaya(from an old family of Cholas) captured the Kaveri Delta from Muttaraiyar and his further '
                    'generations captured the neighbouring areas')
                st.markdown('''___''')
                st.image(
                    'https://1.bp.blogspot.com/-epNYUdIae7c/WWeIx2nS_WI/AAAAAAAAAj8/JJVSwOHqovg0oJSW-F5rkowsP9WqOIHtwCLcBGAs/s1600/19983995_1357551827690690_3692184353615264635_o.jpg', )
            with st.expander('See explination for d'):
                st.write('The sentence had verb+ing, been and had which makes it past perfect continuous')
                st.markdown('''___''')
                st.image('https://eslgrammar.org/wp-content/uploads/2019/05/Past-Perfect-Continuous-1.jpg', )
            with st.expander('See explination for e'):
                st.write("Gracias is a spanish word which means 'Thank You'")
                st.markdown('''___''')
                st.image(
                    'https://st3.depositphotos.com/1266988/18149/v/1600/depositphotos_181498006-stock-illustration-muchas-gracias-spanish-thank-you.jpg', )
            with st.expander('See explination for f'):
                st.write('In the oxford dictionary ajar means sligtly open')
                st.markdown('''___''')
                st.image('https://media.tenor.com/images/e4d895552f3844d1bb4c6a4c5c3105ec/tenor.gif', )
    else:
        st.error('Please Enter Your Name And Email Above First')

st.write('')
st.markdown('''___''')
st.subheader('Comments')
st.write('')
read2 = pd.read_csv('quizdbase3.csv')
for i in range(0,len(read2['Name'])):
    st.markdown('**'+read2['Name'][i]+'**')
    st.write(read2['Comment'][i])
    st.write('')


with st.expander('Write Comment'):

    an,bn = st.columns(2)
    with an:
        nmecmnt = st.text_input('Enter Name')
    with bn:
        wrtcmnt = st.text_area('Enter Feedback/Opinion/Comment')

    if st.button('📨'):

        if nmecmnt == '':
            st.warning('Warning: Do Not Leave Anything Empty')

        elif wrtcmnt == '':
            st.warning('Warning: Do Not Leave Anything Empty')

        else:
            ade = list(read2['Name'])
            adf = list(read2['Comment'])

            ade.append(nmecmnt)
            adf.append(wrtcmnt)

            dictcmnt = {
                'Name': ade,
                'Comment': adf
            }

            dtfrmcmnt = pd.DataFrame(dictcmnt)
            dtfrmcmnt.to_csv('quizdbase3.csv')

            st.success('Successfully Sent The Comment')
            st.write('Reload The Page To See Your Comment')


#end = t.time()
#print("Total Runtime", end - start)
