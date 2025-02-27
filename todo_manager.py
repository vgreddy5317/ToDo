import pandas as pd
from datetime import datetime
import os

class TodoManager:
    def __init__(self):
        self.file_path = "data/todos.csv"
        self.ensure_data_file()
        self.load_tasks()

    def ensure_data_file(self):
        """Ensure the data directory and file exist"""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=[
                'title', 'description', 'category', 'priority',
                'due_date', 'completed', 'created_at'
            ])
            df.to_csv(self.file_path, index=False)

    def load_tasks(self):
        """Load tasks from CSV file"""
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            self.tasks = pd.read_csv(self.file_path)
            self.tasks['due_date'] = pd.to_datetime(self.tasks['due_date']).dt.date
            self.tasks['created_at'] = pd.to_datetime(self.tasks['created_at'])
        else:
            self.tasks = pd.DataFrame(columns=[
                'title', 'description', 'category', 'priority',
                'due_date', 'completed', 'created_at'
            ])

    def save_tasks(self):
        """Save tasks to CSV file"""
        self.tasks.to_csv(self.file_path, index=False)

    def add_task(self, title, description, category, priority, due_date):
        """Add a new task"""
        new_task = {
            'title': title,
            'description': description,
            'category': category,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now()
        }
        self.load_tasks()  # Ensure we have the latest data
        self.tasks = pd.concat([self.tasks, pd.DataFrame([new_task])], ignore_index=True)
        self.save_tasks()

    def delete_task(self, index):
        """Delete a task by index"""
        self.load_tasks()
        self.tasks = self.tasks.drop(index)
        self.save_tasks()

    def toggle_task_status(self, index):
        """Toggle task completion status"""
        self.load_tasks()
        self.tasks.at[index, 'completed'] = not self.tasks.at[index, 'completed']
        self.save_tasks()

    def get_categories(self):
        """Get unique categories"""
        self.load_tasks()
        return self.tasks['category'].unique().tolist() if not self.tasks.empty else []

    def get_filtered_tasks(self, categories, priorities, sort_by):
        """Get filtered and sorted tasks"""
        self.load_tasks()  # Ensure the latest tasks are loaded from CSV
        filtered_tasks = self.tasks.copy()

        # Apply category filter
        if "All" not in categories:
            filtered_tasks = filtered_tasks[filtered_tasks['category'].isin(categories)]

        # Apply priority filter
        if "All" not in priorities:
            filtered_tasks = filtered_tasks[filtered_tasks['priority'].isin(priorities)]

        # Apply sorting
        if sort_by == "Due Date":
            filtered_tasks = filtered_tasks.sort_values('due_date')
        elif sort_by == "Priority":
            priority_order = {"High": 0, "Medium": 1, "Low": 2}
            filtered_tasks['priority_rank'] = filtered_tasks['priority'].map(priority_order)
            filtered_tasks = filtered_tasks.sort_values('priority_rank').drop('priority_rank', axis=1)
        elif sort_by == "Category":
            filtered_tasks = filtered_tasks.sort_values('category')

        return filtered_tasks

    def get_statistics(self):
        """Get task statistics"""
        self.load_tasks()
        total_tasks = len(self.tasks)
        completed_tasks = len(self.tasks[self.tasks['completed']]) if not self.tasks.empty else 0
        
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': total_tasks - completed_tasks
        }
