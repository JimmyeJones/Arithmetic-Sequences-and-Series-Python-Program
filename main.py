import streamlit as st
st.title("Arithmetic Sequences & Series Python Program")
choice = st.selectbox("Select your requested calculation", ["Sequences", "Series"])
d = st.number_input("Common Difference")
a1 = st.number_input("Starting value (a1)")
n = int(st.number_input("Number of terms"))
if st.button("Calculate"):
  if choice == "Sequences":
    ans = (a1+(n-1)*d)
    st.write(f"Your answer is: {ans}")
  else:
    total = 0
    for n in range (1, n+1):
      ans = (a1+(n-1)*d)
      print(ans)
      total += ans
    print(f"Total: {total}")
