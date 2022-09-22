import streamlit as st
import pandas as pd


def _create_df():
    data = {
        "series_1": [1, 3, 4, 5, 7],
        "series_2": [10, 30, 40, 100, 250],
    }
    return pd.DataFrame(data)


def main():
    st.title("Test driving streamlit from Python")
    st.subheader("Studying this now.")
    st.write(
        """Hello world!
    This is my first streamlit app.
    Just testing around and making sure things are in place.
    """
    )
    st.write(_create_df())
    st.line_chart(_create_df())
    st.area_chart(_create_df())

    my_slider = st.slider("Temperature:", -50, 150)
    st.write(my_slider, "Celsius is ", my_slider + 9 / 5 * 32, " Fahrenheit")


if __name__ == "__main__":
    main()
    # streamlit run h_modern_tools/streamlit_webapp.py
