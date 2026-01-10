from separated.createTask import TaskCreate

tasks_db = {
    1: {"title": "Buy groceries", "description": "Milk, Bread, Eggs", "due_date": "2024-06-30T12:00:00", "priority": 2, "completed": False},
    2: {"title": "Read book", "description": "Finish reading '1984'", "due_date": "2024-07-01T15:00:00", "priority": 3, "completed": True}
}

class TaskService:
    def CreateTask(self, task_data : TaskCreate) -> dict:
        """Create a new task with provided data"""
        new_id = self._generate_new_id()
        task_dict = self._prepare_task_dict(new_id, task_data)
        self._save_task(task_dict)
        self._notify_task_created(task_dict)
        return task_dict
    
    def _generate_new_id(self) -> int:
        """Generate a new unique ID for the task"""
        return max(tasks_db.keys()) + 1 if tasks_db else 1
    
    def _prepare_task_dict(self, task_id: int, task_data: TaskCreate) -> dict:
        """Prepare the task dictionary to be saved"""
        return {
            "ID" : task_id,
            "title": task_data.title,
            "description": task_data.description,
            "due_date": task_data.due_date.isoformat(),
            "priority": task_data.priority,
            "completed": task_data.completed
        }
    
    def _save_task(self, task_dict: dict):
        """Save the task to the tasks_db"""
        tasks_db[task_dict["ID"]] = task_dict

    def _notify_task_created(self, task_dict:dict):
        """Notify that a new task has been created (placeholder for actual notification logic)"""
        print(f"Task created: {task_dict}")