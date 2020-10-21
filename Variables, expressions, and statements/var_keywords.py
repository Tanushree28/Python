#Variable names and keywords
#Programmers generally choose names for their variables that are meaningful and document what the variable is used for.

#Variable names can be arbitrarily long. They can contain both letters and numbers, but they cannot start with a number. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter (you’ll see why later).

#The underscore character ( _ ) can appear in a name. It is often used in names with multiple words, such as my_name or airspeed_of_unladen_swallow. Variable names can start with an underscore character, but we generally avoid doing this unless we are writing library code for others to use.

#If you give a variable an illegal name, you get a syntax error:

#76trombones = 'big parade'
#SyntaxError: invalid syntax


#more@ = 1000000
#SyntaxError: invalid syntax


#class = 'Advanced Theoretical Zymurgy'
#SyntaxError: invalid syntax




#Python reserves 35 keywords:

#and       del       from      None      True
#as        elif      global    nonlocal  try
#assert    else      if        not       while
#break     except    import    or        with
#class     False     in        pass      yield
#continue  finally   is        raise     async
#def       for       lambda    return    await