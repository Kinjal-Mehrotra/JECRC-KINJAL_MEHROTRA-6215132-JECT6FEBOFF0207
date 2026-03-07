import time

class TODO:
    todos=[]
    
    def add_todo(self, desc):
        if (len(desc.strip())==0):
            print("Task cannot be empty!!!")
            return
        dict1={
            'id':int(time.time()),
            'desc':desc,
            'is_completed':False
        }
        self.todos.append(dict1)

    def remove_todo(self, id):
        i=0
        if len(self.todos)==0:
            print("No TODOS exist")
            return 
        
        while(i<len(self.todos)):
            if (self.todos[i]['id']==id):
                print(f"Removed to-do with id: {self.todos[i]['id']}")
                self.todos.pop(i)
                return
            i+=1
    
    def display_todos(self):
        print("To-Do list")
        
        for element in self.todos:
            if element['is_completed']:
                print(f"{element['desc']}  {element['id']}  (Completed) ")
            else:
                print(f"{element['desc']}  {element['id']}  (Pending) ")
    
    def update_todo(self, id, new_desc):
        i=0
        while(i<len(self.todos)):
            if (self.todos[i]['id']==id):
                self.todos[i]['desc']=new_desc
                print(f"Updated todo , id: {self.todos[i]['id']}")
                return
            i+=1

    def toggle_mark_as_completed(self, id):
        i=0
        while(i<len(self.todos)):
            if (self.todos[i]['id']==id):
                self.todos[i]['is_completed']=not self.todos[i]['is_completed']
                print(f"Todo marked as completed , id: {self.todos[i]['id']}")
                return
            i+=1
    
    
    def completed_todos(self):
        for element in self.todos:
            if (element['is_completed'])==True:
                print(f"{element['desc']}  {element['id']}  (Completed) ")
    
    def incompleted_todos(self):
        for element in self.todos:
            if (element['is_completed'])==False:
                print(f"{element['desc']}  {element['id']}  (Pending) ")      
    
