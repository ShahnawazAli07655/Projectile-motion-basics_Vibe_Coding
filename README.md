# Projectile Motion Simulation in Python

This project simulates **projectile motion** using classical physics equations and visualizes the trajectory using **NumPy** and **Matplotlib**.

The program calculates:
* **Time of flight**
* **Maximum height reached**
* **Horizontal range**
* **Trajectory plot** of the projectile

---

## 📌 Features

- **Interactive User Input:**
  - Initial velocity ($m/s$)
  - Angle of projection (degrees)
  - Duration for the simulation
- **Physics Computations:** Calculates key physical quantities automatically.
- **Visual Feedback:** Displays a high-quality **2D trajectory plot**.
- **Beginner Friendly:** Clean, documented code for physics and Python learners.

---

## 🧮 Physics Used

The simulation is based on standard projectile motion equations under uniform gravity:



* **Horizontal velocity:** $vx = v0 \cos(\theta)$
* **Vertical velocity:** $vy = v0 \sin(\theta)$
* **Time of flight:** $T = 2vy/g$
* **Maximum height:** $H = (vy^2)/(2g)$
* **Range:** $R = vx \times T$

**Assumptions:**
* No air resistance
* Constant gravitational acceleration ($g = 9.8  m/s^2)

---

## 🛠️ Requirements

Make sure you have Python 3 installed along with the following libraries:

1. Numpy
2. Matplotlib

---

##🧮 Physics Logic

The script implements standard kinematic equations 
where 
*  $g = 9.8  m/s^2$
*  Horizontal Distance: $x = v0 \cos(\theta)t$
*  Vertical Distance: $y = v0 \sin(\theta)t - \0.5*gt^2$

---

##📈 Sample Output

When the script runs, it provides a summary of the flight data in the console:

Time of Flight: 4.08 s
Max Height: 20.41 m
Horizontal Range: 70.68 m

---

##📚 Educational Use

This project is ideal for:

1. Physics students studying kinematics.

2. Python beginners learning how to use libraries.

3. Data Visualization practice with Matplotlib.

---

Happy Computing!

---
