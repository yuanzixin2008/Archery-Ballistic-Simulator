# Project: Archery Ballistic Simulator

## Project Overview
I developed this project to simulate an arrow's flight over a distance of **70 meters**. My goal was to investigate how **gravity** and **wind** affect the arrow's accuracy. I used Python to build a physics engine that follows official archery standards.

## 1. 2D Scoring Analysis (archery_2D.py)
In this part, I focused on the final **results** of the shots on the target.
* **Standard Settings**: I set the target height at **1.3 meters**, which is the official competition standard.
* **Human Error Simulation**: I used `np.random.normal` to simulate 100 shots. This modeled the small variances in launch angles that happen in real life.
* **Automatic Scoring**: The program automatically calculated the score (10, 9, 7, or 5) for each arrow based on its distance from the center.



## 2. 3D Trajectory Modeling (archery_3D.py)
In this part, I focused on the **process** of the flight in a 3D environment.
* **Physics Logic**: The model updated the arrow's position every 0.01 seconds. It accounted for both **Gravity** and **Air Resistance** ($k=0.02$).
* **Wind Resistance**: I implemented a "drag-based" wind model. It showed how crosswinds pulled the arrow away from the center line during its flight.
* **The Blue Cross (Verification)**: I added a **blue cross** at 70 meters to act as a "perfect" target. This allowed me to verify that my 3D flight paths were accurate and hit the target at the correct height.



## Conclusion
This project demonstrated my ability to turn physics theory into a working simulation. I successfully maintained **consistency** between the 2D scoring model and the 3D trajectory model. The results showed that environmental wind is the biggest challenge for long-distance accuracy.
