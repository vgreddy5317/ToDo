import streamlit as st
from todo_manager import TodoManager
from utils import initialize_session_state
from styles import apply_custom_styles

def main():
    st.set_page_config(
        page_title="Task Manager",
        page_icon="✅",
        layout="wide"
    )

    apply_custom_styles()
    initialize_session_state()
    todo_manager = TodoManager()

    st.title("📝 Task Manager")

    with st.sidebar:
        st.header("Add New Task")
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Description")
        category = st.selectbox("Category", ["Work", "Personal", "Shopping", "Health", "Other"])
        priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
        due_date = st.date_input("Due Date")

        if st.button("Add Task", type="primary") and task_title:
            todo_manager.add_task(task_title, task_description, category, priority, due_date)

            # Reload the tasks in session state and refresh UI
            st.session_state.tasks = todo_manager.get_filtered_tasks(["All"], ["All"], "Due Date")
            st.success("Task added successfully!")
            st.rerun()  # <-- Corrected from st.experimental_rerun()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Tasks")
        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            filter_category = st.multiselect("Filter by Category", ["All"] + todo_manager.get_categories(), default="All")
        with filter_col2:
            filter_priority = st.multiselect("Filter by Priority", ["All", "Low", "Medium", "High"], default="All")
        with filter_col3:
            sort_by = st.selectbox("Sort by", ["Due Date", "Priority", "Category"])

        tasks = todo_manager.get_filtered_tasks(filter_category, filter_priority, sort_by)

        if not tasks.empty:
            for idx, task in tasks.iterrows():
                with st.container():
                    task_col1, task_col2, task_col3 = st.columns([3, 1, 1])

                    with task_col1:
                        st.markdown(f"**{task['title']}**")
                        st.write(task['description'])

                    with task_col2:
                        st.write(f"**Due:** {task['due_date']}")
                        st.write(f"**Priority:** {task['priority']}")

                    with task_col3:
                        if not task['completed']:
                            if st.button("Complete", key=f"complete_{idx}", type="primary"):
                                todo_manager.toggle_task_status(idx)
                                st.success("Task completed!")
                                st.rerun()  # <-- Corrected from st.experimental_rerun()
                        else:
                            st.write("✅ Done")

                        if st.button("Delete", key=f"delete_{idx}", type="secondary"):
                            todo_manager.delete_task(idx)
                            st.success("Task deleted!")
                            st.rerun()  # <-- Corrected from st.experimental_rerun()
                    st.divider()
        else:
            st.info("No tasks found.")

    with col2:
        st.subheader("Statistics")
        stats = todo_manager.get_statistics()

        st.metric("Total Tasks", stats['total_tasks'])
        st.metric("Completed Tasks", stats['completed_tasks'])
        st.metric("Pending Tasks", stats['pending_tasks'])

        if stats['total_tasks'] > 0:
            progress = stats['completed_tasks'] / stats['total_tasks']
            st.progress(progress)


if __name__ == "__main__":
    main()
