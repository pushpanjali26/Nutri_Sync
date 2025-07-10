import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image
image=Image.open("bi.png")
image=image.resize((32,32))
image.save("bitcoin_icon.ico")
class WebsiteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NutriSync")
        self.root.iconbitmap("bitcoin_icon.ico")
        self.root.geometry("750x500")
        self.root.resizable(False,False)

        self.background_image = tk.PhotoImage(file="biticon.png")

        # Login Page
        self.login_frame = tk.Frame(self.root)
        self.login_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.background_image = tk.PhotoImage(file="biticon.png")
        self.background_label = tk.Label(self.login_frame, image=self.background_image)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)


        # Username and Password Labels and Entry Fields
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")

# Login and Sign Up Buttons
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.place(relx=0.5, rely=0.6, anchor="center")

        self.signup_button = tk.Button(self.login_frame, text="Signup", command=self.signup)
        self.signup_button.place(relx=0.5, rely=0.65, anchor="center")

        

    def login(self):
        # Retrieve username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Placeholder authentication logic
        if username and password :
            if len(username) < 8:
                messagebox.showerror("Invalid Username", "Username must be at least 8 characters long.")
                return       
            try:
                conn = sqlite3.connect('user_credentials.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username, password))
                user=cursor.fetchone()
                conn.close()
                if user:
                    messagebox.showinfo("Login Successful", "Welcome {}!".format(username))
                    self.open_main_page()
                else:
                    
                    messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
            except sqlite3.Error as e:
                messagebox.showerror("Error","Error creating user: {}".format(e))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def signup(self):
        # Destroy login frame
        self.login_frame.destroy()

        # Signup Frame
        self.signup_frame = tk.Frame(self.root)
        self.signup_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.background_label = tk.Label(self.signup_frame, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)


        self.signup_username_label = tk.Label(self.signup_frame, text="Username:")
        self.signup_username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.signup_username_entry = tk.Entry(self.signup_frame)
        self.signup_username_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.signup_password_label = tk.Label(self.signup_frame, text="Password:")
        self.signup_password_label.place(relx=0.5, rely=0.5, anchor="center")
        self.signup_password_entry = tk.Entry(self.signup_frame, show="*")
        self.signup_password_entry.place(relx=0.5, rely=0.55, anchor="center")

        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:")
        self.confirm_password_label.place(relx=0.5, rely=0.6, anchor="center")
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*")
        self.confirm_password_entry.place(relx=0.5, rely=0.65, anchor="center")

    # Sign Up Button
        self.signup_button = tk.Button(self.signup_frame, text="Sign Up", command=self.create_account)
        self.signup_button.place(relx=0.5, rely=0.7, anchor="center")
        # Username, Password, Confirm Password Labels and Entry Fields
        

    def create_account(self):
        # Placeholder account creation logic
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password == confirm_password and username :
            try:
                conn = sqlite3.connect('user_credentials.db')
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                  )''')
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",(username, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Account Created", "Your account has been created successfully!")
            except sqlite3.Error as e:
                messagebox.showerror("Error","Error creating user: {}".format(e))
            # You may add code to store the username and password in a database or file
            # For simplicity, we'll just print them
            print(f"Username: {username}, Password: {password}")
            # Go back to login page
            self.signup_frame.destroy()
            self.__init__(self.root)
        else:
            messagebox.showerror("Password Mismatch", "Passwords do not match. Please try again.")


    def open_main_page(self):
        # Destroy login page
        self.login_frame.destroy()

        # Main Page
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.background_label = tk.Label(self.main_frame, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        button_height = 50  # Adjust as needed
        total_height = self.root.winfo_height()
        top_margin = (total_height - 2 * button_height) / 3

    # BMI Button
        self.bmi_button = tk.Button(self.main_frame, text="BMI", command=self.open_bmi_page)
        self.bmi_button.place(relx=0.5, rely=top_margin / total_height, anchor="n")

    # Exercise Button
        self.exercises_button = tk.Button(self.main_frame, text="Exercises", command=self.open_exercises_page)
        self.exercises_button.place(relx=0.5, rely=(top_margin + button_height) / total_height, anchor="n")


    
    def open_bmi_page(self):
    # Destroy main frame
        self.main_frame.destroy()

    # BMI Page
        self.bmi_frame = tk.Frame(self.root)
        self.bmi_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.background_label = tk.Label(self.bmi_frame, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    # Centering the BMI input fields
        frame_width = self.root.winfo_width()
        frame_height = self.root.winfo_height()

        label_width = 100
        entry_width = 20
        pady_value = 10

    # Age
        self.age_label = tk.Label(self.bmi_frame, text="Age:")
        self.age_label.place(relx=0.5, rely=0.4, anchor="e")
        self.age_entry = tk.Entry(self.bmi_frame, width=entry_width)
        self.age_entry.place(relx=0.5, rely=0.4, anchor="w")

    # Height
        self.height_label = tk.Label(self.bmi_frame, text="Height (in cm):")
        self.height_label.place(relx=0.5, rely=0.5, anchor="e")
        self.height_entry = tk.Entry(self.bmi_frame, width=entry_width)
        self.height_entry.place(relx=0.5, rely=0.5, anchor="w")

    # Weight
        self.weight_label = tk.Label(self.bmi_frame, text="Weight (in kg):")
        self.weight_label.place(relx=0.5, rely=0.6, anchor="e")
        self.weight_entry = tk.Entry(self.bmi_frame, width=entry_width)
        self.weight_entry.place(relx=0.5, rely=0.6, anchor="w")

    # Calculate BMI Button
        self.calculate_button = tk.Button(self.bmi_frame, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.place(relx=0.5, rely=0.7, anchor="center")

    # Back Button
        self.back_button = tk.Button(self.bmi_frame, text="Back", command=self.go_back)
        self.back_button.place(relx=0.5, rely=0.8, anchor="center")

    
    def calculate_bmi(self):
        try:
            age = int(self.age_entry.get())
            if not (1 <= age <= 100):
                messagebox.showerror("Invalid Age", "Age must be between 1 and 100.")
                return
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())
            bmi = weight_kg / ((height_cm / 100) ** 2)
            if bmi < 18.5:
                recommendation = "You are underweight. It is recommended to consume a balanced diet rich in proteins, healthy fats, and carbohydrates. Consider consulting a nutritionist for a personalized diet plan."
            elif 18.5 <= bmi < 25:
                recommendation = "Your BMI is within the healthy range. Continue to maintain a balanced diet and active lifestyle."
            elif 25 <= bmi < 30:
                recommendation = "You are overweight. It is advisable to focus on portion control, increase physical activity, and consume a diet rich in fruits, vegetables, and lean proteins."
            else:
                recommendation = "You are obese. It is crucial to consult a healthcare professional or nutritionist to develop a comprehensive weight management plan."
            messagebox.showinfo("BMI Result", f"Your BMI: {bmi:.2f}\n\n{recommendation}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values for height and weight.")
    
    def open_exercises_page(self):
        # Destroy main frame
        self.main_frame.destroy()

        # Exercise Page
        self.exercise_frame = tk.Frame(self.root)
        self.exercise_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.background_label = tk.Label(self.exercise_frame, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        

        # Add exercises functionality here
        body_parts = ["Arms", "Legs", "Chest", "Abs", "Butt", "Back"]
        for body_part in body_parts:
            button = tk.Button(self.exercise_frame, text=body_part, command=lambda bp=body_part: self.display_exercises(bp))
            button.pack(pady=5)

        self.back_button = tk.Button(self.exercise_frame, text="Back", command=self.go_back_from_exercise_page)
        self.back_button.pack(pady=5)

    def display_exercises(self, body_part):
    # Destroy body parts buttons
        for widget in self.exercise_frame.winfo_children():
            widget.destroy()
        background_image_path = f"{body_part.lower()}_image.png"  # Assuming image filenames are in lowercase
        try:
            background_image = tk.PhotoImage(file=background_image_path)
            background_label = tk.Label(self.exercise_frame, image=background_image)
            background_label.place(relwidth=1, relheight=1)
        except tk.TclError:
            print(f"Error: Background image file '{background_image_path}' not found.")
            background_label = tk.Label(self.exercise_frame, text="Image not found")
            background_label.pack()
            
    # Show exercises for the selected body part
        exercises = self.get_exercises(body_part)
        for index, header in enumerate(["Exercise", "Description"]):
            header_label = tk.Label(self.exercise_frame, text=header, font=("Helvetica", 12, "bold"))
            header_label.grid(row=0, column=index, padx=10, pady=5, sticky="ew")

    # Create and place exercise details
        for row, exercise in enumerate(exercises, start=1):
            exercise_label = tk.Label(self.exercise_frame, text=exercise["name"], font=("Helvetica", 10, "bold"))
            exercise_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            description_label = tk.Label(self.exercise_frame, text=exercise["description"], wraplength=600, justify="left")
            description_label.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
    # Add a back button
        self.back_button = tk.Button(self.exercise_frame, text="Back", command=self.open_exercises_page)
        self.back_button.grid(row=row + 1, column=0, columnspan=2, pady=10)

        self.exercise_frame.grid_columnconfigure(0, weight=1)
        self.exercise_frame.grid_columnconfigure(1, weight=2)
        self.exercise_frame.grid_rowconfigure(row + 1, weight=1)
    def get_exercises(self, body_part):
    # Function to get exercises for the selected body part
    # You can retrieve exercises from a database or define them in a dictionary
    # For demonstration purposes, a sample dictionary is used here
        exercises_dict = {
            "Arms": [
                {"name": "Push-ups", "description": "Start in a plank position with hands slightly wider than shoulder-width apart. Lower your body towards the floor by bending your elbows, keeping your back straight and your core engaged. Push back up to the starting position."},
                {"name": "Bicep Curls", "description": "Stand with feet shoulder-width apart, holding dumbbells at your sides with palms facing forward. Keeping your elbows close to your sides, curl the dumbbells towards your shoulders while exhaling. Lower the dumbbells back down with control while inhaling."},
                {"name": "Tricep Dips", "description": "Sit on the edge of a chair or bench with your hands gripping the edge, fingers facing forward. Walk your feet forward and lift your hips off the chair. Bend your elbows and lower your body towards the ground, keeping your back close to the chair. Push back up to the starting position by straightening your arms."},
                {"name": "Shoulder Press", "description": "Hold dumbbells at shoulder height with palms facing forward and elbows bent. Press the dumbbells upward until arms are fully extended overhead. Slowly lower the dumbbells back to shoulder height."},
                {"name": "Tricep Extensions", "description": "Hold a dumbbell in both hands and extend your arms overhead. Keeping your upper arms close to your head, bend your elbows to lower the dumbbell behind your head. Extend your arms back to the starting position, fully straightening your elbows."}
            ],
            "Legs" : [
                {"name":"Squats","description":"Stand with your feet shoulder-width apart, lower your body by bending your knees and pushing your hips back as if you're sitting into a chair. Keep your chest up and your back straight. Lower until your thighs are parallel to the ground, then push through your heels to return to the starting position."},
                {"name":"Lunges","description": "Step forward with one leg and lower your body until both knees are bent at a 90-degree angle. Keep your front knee over your ankle and your back knee just above the ground. Push back up to the starting position and repeat on the other leg."},
                {"name":"Deadlifts","description":"Stand with your feet shoulder-width apart, holding a barbell or dumbbells in front of your thighs. Keeping your back straight, bend at the hips and lower the weights towards the ground, keeping them close to your body. Once you feel a stretch in your hamstrings, return to the starting position by squeezing your glutes and pushing your hips forward."},
                {"name":"Leg Press","description": "Using a leg press machine, sit down and place your feet on the platform about shoulder-width apart. Push the platform away from your body by extending your knees, then slowly lower it back down until your knees are bent at a 90-degree angle."},
                {"name":"Calf Raises","description": "Stand with your feet hip-width apart on the edge of a step or platform, with your heels hanging off. Rise up onto your tiptoes as high as you can, then lower your heels back down below the level of the step."},
            ],
            "Chest":[
                {"name":"Push-ups","description":"A classic bodyweight exercise that primarily targets the chest, shoulders, and triceps. To perform a push-up, start in a plank position with your hands shoulder-width apart, lower your body until your chest nearly touches the ground, then push back up to the starting position."},
                {"name":"Chest Press","description":"This exercise can be done using dumbbells or a barbell on a bench. Lie down on the bench with your feet flat on the ground. Hold the dumbbells or barbell above your chest with your arms fully extended, then lower the weights down towards your chest, and push them back up to the starting position."},
                {"name":"Chest Fly","description":"Also performed on a bench with dumbbells, chest fly targets the chest muscles and helps improve chest width. Lie down on the bench holding dumbbells directly above your chest with your palms facing each other. Lower the dumbbells out to the sides in a wide arc until you feel a stretch in your chest, then bring them back up to the starting position."},
                {"name":"Dumbbell Pullover","description":"Lie down on a bench with only your upper back resting on the bench and your feet flat on the ground. Hold a dumbbell with both hands above your chest, arms slightly bent. Lower the dumbbell backward over your head in a controlled motion until your arms are parallel to the ground, then pull it back up to the starting position."},
            ],
            "Abs": [
                {"name": "Crunches", "description": "Lie on your back with knees bent and feet flat on the floor. Place your hands behind your head or across your chest. Engage your core muscles and lift your shoulders towards the ceiling while keeping your lower back on the floor. Lower back down with control."},
                {"name": "Planks", "description": "Start on your hands and knees. Place your forearms on the ground with elbows directly under your shoulders. Step your feet back, one at a time, until your body forms a straight line from head to heels. Hold this position, keeping your core tight and avoiding sagging or lifting of the hips."},
                {"name": "Leg Raises", "description": "Lie on your back with legs straight and together. Place your hands palms down under your hips to support your lower back. Keeping your legs straight, lift them towards the ceiling until they form a 90-degree angle with the floor. Slowly lower your legs back down, keeping them under control and avoiding arching your lower back."},
                {"name": "Russian Twists", "description": "Sit on the floor with knees bent and feet lifted off the ground. Lean back slightly to engage your core muscles. Hold a weight or medicine ball with both hands. Twist your torso to the right, bringing the weight towards the floor next to your right hip. Return to the center and then twist to the left, bringing the weight towards the floor next to your left hip. Repeat this twisting motion while keeping your core engaged."},
                {"name": "Mountain Climbers", "description": "Start in a plank position with your hands under your shoulders and your body forming a straight line from head to heels. Engage your core and bring one knee towards your chest, then quickly switch legs, bringing the other knee towards your chest while extending the opposite leg back. Continue alternating legs in a running motion while maintaining a strong plank position."}
            ],
            "Butt": [
                {"name": "Glute Bridges", "description": "Lie on your back with knees bent, lift your hips toward the ceiling, squeezing your glutes at the top."},
                {"name": "Donkey Kicks", "description": "Start on all fours, kick one leg back while keeping it bent, squeezing your glutes, then return to starting position."},
                {"name": "Clamshells", "description": "Lie on your side with knees bent, open and close your top knee while keeping your feet together, focusing on engaging the glute."},
                {"name": "Hip Thrusts", "description": " Sit on the ground with your back against a bench, roll a barbell over your hips, and thrust upward, squeezing your glutes at the top."},
                {"name": "Side-Lying Leg Lifts", "description": "Lie on your side, lift your top leg towards the ceiling while keeping it straight, then lower it back down with control, focusing on engaging the side glutes."}
            ],
            "Back": [
                {"name": "Superman", "description": "Lie face down with arms extended overhead, lift your chest, arms, and legs off the ground, squeezing your back muscles, then lower back down."},
                {"name": "Bent-over Rows", "description": "Hold dumbbells in each hand, hinge at the hips with a slight bend in your knees, pull the weights towards your waist, squeezing your shoulder blades together, then lower back down."},
                {"name": "Reverse Flyes", "description": "Stand with a dumbbell in each hand, hinge at the hips with a slight bend in your knees, raise your arms out to the sides, squeezing your shoulder blades together, then lower back down."},
                {"name": "Lat Pulldowns", "description": "Sit at a lat pulldown machine, grip the bar with hands wider than shoulder-width apart, pull the bar down towards your chest, squeezing your shoulder blades together, then slowly release back up."},
                {"name": "Renegade Rows", "description": "Start in a plank position with hands holding onto dumbbells, row one weight up towards your ribcage while stabilizing with your core and legs, then lower back down and repeat on the other side."} 
            ],
            
        }
        return exercises_dict.get(body_part, [])
    def go_back_from_exercise_page(self):
        # Destroy exercise frame and go back to the main page
        if hasattr(self, 'exercise_frame'):
            self.exercise_frame.destroy()
        self.open_main_page()  # Show the main page again

    def go_back(self):
        # Destroy current frame and go back to the login page
        if hasattr(self, 'bmi_frame'):
            self.bmi_frame.destroy()
            self.open_main_page()
        elif hasattr(self, 'exercise_frame'):
            self.exercise_frame.destroy()
            self.open_main_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteGUI(root)
    root.mainloop()

    
