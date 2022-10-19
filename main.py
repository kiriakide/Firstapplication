# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def print_hi(Kiriaki):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {Kiriaki}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


