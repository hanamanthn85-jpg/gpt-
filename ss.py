class stack:
    def __init__(self):
        self.item=()
    def itEmpty(self):
        return self.item==()
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def check_bracket(statement):
        S=stack()
        for token in statement:
            if token is"{[(":
                s.push(token)
            elif token is"}])":
                  if s.isEmpty():
                      return False
                  else:
                        left=s.pop()
                        if(token=="}" and left !="{")or\
                          (token=="]" and left !="[")or\
                          (token==")" and left !="("):
                                return False
            return s.isEmpty()
    statement=input("enter an expression:")
    if check_brackets(statement):
        print("this is having balanced parantheses")
    else:
        print("this is not having balanced parantheses")
    
                  
            
              
