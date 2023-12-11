import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")
    st.subheader("Enter three numbers and click the button to find the largest one.")

    # Use columns for a better layout
    col1, col2, col3 = st.columns(3)

    with col1:
        num1 = st.number_input("Number 1", value=0.0, step=0.1, key="num1")

    with col2:
        num2 = st.number_input("Number 2", value=0.0, step=0.1, key="num2")

    with col3:
        num3 = st.number_input("Number 3", value=0.0, step=0.1, key="num3")

    # Create a button with a nice color
    if st.button("Find Largest", key="find_button", help="Click to find the largest number"):
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

    # Add a footer
    st.markdown(
        """
        *Tip: You can enter decimal numbers and negative numbers as well.*
        """
    )

if __name__ == "__main__":
    main()
