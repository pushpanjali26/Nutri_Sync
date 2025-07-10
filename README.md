# Nutri_Sync
NutriSync is a smart health assistant application built using Python that combines BMI tracking and personalized fitness guidance in one easy-to-use interface. It includes secure user authentication (login/signup) and interactive tools to promote a healthy lifestyle.

#### Key Features

- **BMI Calculator** – Calculates Body Mass Index based on user input (height and weight).
- **Targeted Exercise Suggestions** – Recommends exercises for specific body parts (e.g., arms, legs, abs).
- **GUI-Based Application** – Easy-to-use interface built using Tkinter in Python.

#### Project Workflow

##### 1. User Authentication (Login / Signup)
- On launching the application, users are greeted with a **login/signup screen**.
- New users can **sign up** by providing a username and password.
- User credentials are securely stored in a **database** (e.g., SQLite), allowing them to **log in** anytime with the same credentials.

##### 2. 🏠 Home Interface
After a successful login, the user is taken to the main menu, which provides access to:
- **BMI Calculator**
- **Exercise Recommendations**

---

######  BMI Calculator
- The user enters their **height, weight, and age**.
- The app calculates the **BMI** using the formula:  
  `BMI = weight (kg) / height (m)^2`
- Based on the result, the app gives feedback such as:
  - Underweight
  - Normal weight
  - Overweight
- After the result is shown, the user can return to the main menu.

---

###### Exercise Suggestions
- The user can select from different **body parts** (e.g., Arms, Legs, Abs, Chest, etc.).
- Upon clicking a body part, the app displays **a list of relevant exercises** for that area.
- The user can explore exercises tailored to their focus area for a complete fitness experience.

#### Technologies Used

- **Python** – Programming language
- **Tkinter** – GUI development
- **SQLite** – For user authentication and storing login credentials
- *(Optional extension: images or videos for exercise demonstrations)*

