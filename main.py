+0
from todo_manager import TodoManager
from utils import initialize_session_state
from styles import apply_custom_styles
import time
# Initialize the application
def main():
-6
+6
        page_icon="✅",
        layout="wide"
    )
    
    # Apply custom styles
    apply_custom_styles()
    
    # Initialize session state
    initialize_session_state()
    
    # Create TodoManager instance
    todo_manager = TodoManager()
    # Main title
    st.title("📝 Task Manager")
    
    # Sidebar for adding new tasks
    with st.sidebar:
        st.header("Add New Task")
        
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Description")
        category = st.selectbox("Category", ["Work", "Personal", "Shopping", "Health", "Other"])
        priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
        due_date = st.date_input("Due Date")
        
        if st.button("Add Task", type="primary"):
            if task_title:
                todo_manager.add_task(task_title, task_description, category, priority, due_date)
-36
+35
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Filters
        st.subheader("Tasks")
        filter_col1, filter_col2, filter_col3 = st.columns(3)
        
        with filter_col1:
            filter_category = st.multiselect("Filter by Category", ["All"] + todo_manager.get_categories(), default="All")
        
        with filter_col2:
            filter_priority = st.multiselect("Filter by Priority", ["All", "Low", "Medium", "High"], default="All")
            
        with filter_col3:
            sort_by = st.selectbox("Sort by", ["Due Date", "Priority", "Category"])
        # Display tasks
        tasks = todo_manager.get_filtered_tasks(filter_category, filter_priority, sort_by)
        
        if not tasks.empty:
            for idx, task in tasks.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        task_done = st.checkbox(
                            f"**{task['title']}**\n\n{task['description']}", 
                            value=task['completed'],
                            key=f"task_{idx}"
                        )
                        
                        if task_done != task['completed']:
                            todo_manager.toggle_task_status(idx)
                            st.rerun()
                            
                    with col2:
                        st.write(f"**Due:** {task['due_date']}")
                        st.write(f"**Priority:** {task['priority']}")
                    # Task title and checkbox
                    task_done = st.checkbox(
                        f"**{task['title']}**\n\n{task['description']}", 
                        value=task['completed'],
                        key=f"task_{idx}"
                    )
                    with col3:
                        col3_left, col3_right = st.columns(2)
                        with col3_left:
                            if not task['completed']:
                                if st.button("Complete", key=f"complete_{idx}", type="primary"):
                                    todo_manager.toggle_task_status(idx)
                                    st.success("Task completed!")
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.write("✅ Done")
                    if task_done != task['completed']:
                        todo_manager.toggle_task_status(idx)
                        st.rerun()
                        with col3_right:
                            if st.button("Delete", key=f"delete_{idx}", type="secondary"):
                                todo_manager.delete_task(idx)
                                st.success("Task deleted!")
                    # Task details
                    st.write(f"**Due:** {task['due_date']}")
                    st.write(f"**Priority:** {task['priority']}")
                    # Action buttons
                    button_cols = st.columns([1, 1])
                    with button_cols[0]:
                        if not task['completed']:
                            if st.button("Complete", key=f"complete_{idx}", type="primary"):
                                todo_manager.toggle_task_status(idx)
                                st.success("Task completed!")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.write("✅ Done")
                    with button_cols[1]:
                        if st.button("Delete", key=f"delete_{idx}", type="secondary"):
                            todo_manager.delete_task(idx)
                            st.success("Task deleted!")
                            time.sleep(1)
                            st.rerun()
                    st.divider()
        else:
-2
+2
    with col2:
        st.subheader("Statistics")
        stats = todo_manager.get_statistics()
        
        # Display statistics
        st.metric("Total Tasks", stats['total_tasks'])
        st.metric("Completed Tasks", stats['completed_tasks'])
        st.metric("Pending Tasks", stats['pending_tasks'])
        
        # Progress bar
        if stats['total_tasks'] > 0:
            progress = stats['completed_tasks'] / stats['total_tasks']
stats['total_tasks']