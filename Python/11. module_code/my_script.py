#Q. Where does Python look for modules? 
#A. It looks in the current directiory, the python installed directory, and all locations specified in PythonPath (env var)

# import my_module as my_module # this is good but erquires everything important to be pre-fixed by the module name
# from my_module import * # DO NOT do this because you are importing things you may not know about
# from my_module import hello, goodbye # still risk overwriting things in this file

import my_module as mm 

mm.Salutations.hello()