class ToDo:
    all = []
    def add_task(self, task):
        self.task = task
        ToDo.all.append(self.task)
        print("Task added successfully!")
    def task_completed(self):
        ToDo.all.remove(self.task)
        print("Task completed!")
    def display_list():
        print("Tasks list:",ToDo.all)    

task1 =ToDo()
task1.add_task('Physics Revision')
task2 = ToDo()
task2.add_task('Chemistry Homework')
ToDo.display_list()
task1.task_completed()
ToDo.display_list()
