import streamlit as st
import heapq
from datetime import datetime

# Initialize session state
if "task_queue" not in st.session_state:
    st.session_state.task_queue = []

if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []

# Page config
st.set_page_config(page_title="Smart Task Scheduler", layout="centered")

st.title("🧠 Smart Task Scheduler Using Priority Queue")
st.write("Efficient task scheduling based on priority and deadline")

# -------------------- Add Task --------------------
st.header("➕ Add New Task")

task_name = st.text_input("Task Name")

priority = st.selectbox(
    "Priority (1 = High, 5 = Low)",
    [1, 2, 3, 4, 5]
)

deadline = st.date_input("Deadline")

if st.button("Add Task"):
    if task_name.strip() == "":
        st.warning("Please enter a task name.")
    else:
        task = (priority, deadline, task_name)
        heapq.heappush(st.session_state.task_queue, task)
        st.success("Task added successfully!")

# -------------------- Next Task --------------------
st.header("⏭️ Next Task to Execute")

if st.session_state.task_queue:
    next_task = st.session_state.task_queue[0]
    st.write(f"**Task:** {next_task[2]}")
    st.write(f"**Priority:** {next_task[0]}")
    st.write(f"**Deadline:** {next_task[1]}")

    if st.button("Mark as Completed"):
        completed = heapq.heappop(st.session_state.task_queue)
        st.session_state.completed_tasks.append(completed)
        st.success("Task marked as completed!")
else:
    st.info("No pending tasks available.")

# -------------------- Pending Tasks --------------------
st.header("📋 Pending Tasks")

if st.session_state.task_queue:
    for i, task in enumerate(sorted(st.session_state.task_queue)):
        st.write(
            f"{i+1}. **{task[2]}** | Priority: {task[0]} | Deadline: {task[1]}"
        )
else:
    st.write("No pending tasks.")

# -------------------- Completed Tasks --------------------
st.header("✅ Completed Tasks")

if st.session_state.completed_tasks:
    for i, task in enumerate(st.session_state.completed_tasks):
        st.write(
            f"{i+1}. **{task[2]}** | Priority: {task[0]} | Deadline: {task[1]}"
        )
else:
    st.write("No completed tasks yet.")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("Built using Python & Priority Queue (Heap)")
