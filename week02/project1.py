import time
## time.time()

class TODO:

    def __init__(self):
        self.todos=[]

    
    def add_todo(self, desc):
        ## 1. Take the desc from the user
        ## 2. We have to create one dictionry in which we will add the todo desc
        ## 3. We have to append that dictionory inside todos

        todo={'id': int(time.time()),
              'desc':desc,
              'is_complete':False}
        
        self.todos.append(todo)

    
    def remove_todo(self, id):
        
        for i in self.todos :
            if id == i['id']:
                self.todos.remove(i)
                break
    
    def display_todos(self):

        if not self.todos:
            print('Todos is empty...') 

        
        for i in self.todos:
            print(f"Desc->{i['desc']}  ID->{i['id']} IsCompleted->{i['is_complete']}")

    
    def update_todo(self, id, new_desc):

        for i in self.todos:

            if id == i['id']:

                i['desc']=new_desc
                break

        
    
    def toggle_mark_as_completed(self, id):
        
        for i in self.todos:

            if id == i['id']:
                i['is_complete']= not i['is_complete']
                break
    
    def completed_todos(self):
        
        for i in self.todos:

            if i['is_complete']:
                print(f"Desc->{i['desc']}  ID->{i['id']} IsCompleted->{i['is_complete']}")
    
    def incompleted_todos(self):
        for i in self.todos:

            if i['is_complete']== False:
                print(f"Desc->{i['desc']}  ID->{i['id']} IsCompleted->{i['is_complete']}")
    