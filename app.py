import streamlit as st
from PIL import Image
import numpy as np

def predict_calories_from_image(image):
    # Placeholder function for image calorie prediction
    return "250-300 calories"  # This would be replaced by a model's output

def calculate_calories_from_input(food_name, quantity):
    # Placeholder for manual calorie calculation
    food_calories = {
        "apple": 52, "banana": 89, "rice": 130, "bread": 265
    }
    return food_calories.get(food_name.lower(), 0) * quantity

def main():
    st.title("Calorie Calculator")
    st.write("Upload a picture of your food or enter food details manually to estimate calories.")

    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an option", ["Home", "Upload Image", "Manual Input"])

    if option == "Home":
        st.image("https://source.unsplash.com/800x400/?food", caption="Track your meals efficiently!", container=True)
        st.write("This tool helps you keep track of your calories by allowing you to upload food images or input details manually.")

    elif option == "Upload Image":
        st.header("Calorie Estimation from Image")
        uploaded_image = st.file_uploader("Upload an image of food", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            st.write("Processing your image...")

            # Simulated calorie prediction
            predicted_calories = predict_calories_from_image(image)
            st.success(f"Estimated Calories: {predicted_calories}")

    elif option == "Manual Input":
        st.header("Calorie Estimation by Manual Input")

        food_name = st.text_input("Enter food name (e.g., apple, banana):")
        quantity = st.number_input("Enter quantity (e.g., 1, 2, etc.):", min_value=1, step=1)

        if st.button("Calculate Calories"):
            if food_name:
                total_calories = calculate_calories_from_input(food_name, quantity)
                if total_calories > 0:
                    st.success(f"Total Calories for {quantity} {food_name}(s): {total_calories} kcal")
                else:
                    st.error("Food item not recognized. Please try again.")
            else:
                st.error("Please enter a food name.")

if __name__ == "__main__":
    main()
