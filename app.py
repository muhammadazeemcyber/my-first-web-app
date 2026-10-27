import streamlit as st
from collections import deque

# 1. Greeting
st.title("My Python Web App")
st.write("Hello Monday! 👋")

# 2. Number processing section
st.header("1. Number Processing")

# Let's use two distinct text inputs instead of a loop so they display nicely side-by-side
num1 = st.text_input("Enter your first number:", key="num_1")
num2 = st.text_input("Enter your second number:", key="num_2")

# Simulating your list logic safely if the user types something
gr = []
if num1 and num2:
    # Append first number
    gr.append(num1)
    st.write(f"Current list status: `{gr}`")
    
    # Remove first element as your code did
    gr.remove(gr[0])
    st.write(f"After removing first element: `{gr}`")
    
    # Append the number 45
    gr.append(45)
    st.write(f"Final state: `{gr}`")

# 3. Security Number check
st.header("2. Security Check")
security_num = st.number_input("Enter your security number:", step=1, value=0)

if security_num == 45:
    st.success("Your security number is correct! ✅")
elif security_num != 0: 
    st.error("Your security number is incorrect! ❌")

# 4. Username input
st.header("3. User Profile")
username = st.text_input("Enter your username:")
if username:
    st.info(f"Your username is: {username}")

# 5. Password Authentication
st.header("4. Authentication")
st.write("**** Enter Password ****")

password = st.text_input("Maybe need pass key, enter it:", type="password")

if password:
    if int(password) == 1234:
        st.success("Your password is correct! 🎉")
        st.code("YOUR IP address is : 123.445.3.2", language="text")
    else:
        st.error("Your password is incorrect, try again! ❌")
