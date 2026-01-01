# 🧠 Smart Task Scheduler Using Priority Queue

## 📌 Overview
The **Smart Task Scheduler** is a Python-based mini project that helps users manage and schedule tasks efficiently.  
Unlike traditional to-do lists that follow FIFO order, this system uses a **Priority Queue (Heap)** to execute tasks based on **priority and deadline**, improving productivity and task management.

---

## 🎯 Objectives
- To schedule tasks efficiently based on priority
- To demonstrate practical application of **Data Structures and Algorithms**
- To implement a real-life use case of **Priority Queue**
- To provide a simple and user-friendly interface

---

## ✨ Features
- Add tasks with priority and deadline
- Automatic task scheduling using Priority Queue
- View the next task to execute
- Mark tasks as completed
- View pending and completed tasks separately
- Interactive web interface using Streamlit

---

## 🧠 Concepts Used
- Priority Queue
- Heap Data Structure
- Task Scheduling Algorithm
- Time Complexity Optimization

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Data Structure:** Priority Queue (Heap using `heapq`)  

---

## ⚙️ How It Works
- Each task is stored as a tuple `(priority, deadline, task_name)`
- The heap automatically arranges tasks:
  - Higher priority tasks are executed first
  - If priorities are equal, tasks with earlier deadlines are executed first
- Heap operations ensure efficient scheduling with **O(log n)** time complexity

---

## ▶️ How to Run the Project

streamlit run scheduler.py

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

