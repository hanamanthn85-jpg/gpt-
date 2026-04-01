import stack
def cheak_breackets(statement):
    s=stack.stack()
for token in statment:
    if token in "{((":
        s_push(token)
     elif token in "}))":
         if s is empty():
             return false
         else:
             left=s pop()
             if(token=="} "and left!={"}"or/
                (token=="}"add left="{"or/:
                 (token==")"& left!="("):
                     return false
                    return s is empty()
                smt=input("enter an expression")
                res=check_breaket(smt)
                if res=true:
                    print(f"(smt)is having balanced ")
                 else:
                     print(f"(smt)is not having balanced ")
