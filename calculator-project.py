from functions import *
from tkinter import ttk



# ==========================Calculator code=====================

root = tkinter.Tk()
text_input = tkinter.StringVar()
operator = ''
result = ''
equations = ''
collections = []
Memory = []
memory_counter = 0
count = 0
switchok = 0
switchequal = 0
sound_state = 0
root.geometry("600x670+0+0")
root.title('Tipan Calculator')
root.resizable(False, False)

#=================Function definitions=========================

def activation(a = True):
    '''
    This function performs the activation of this distribution, and incase it is activated it performs
    the validation of the activation key each time the program runs to avoid fraud.
    '''
    activation_button.destroy(); lable1.destroy(), lable2.destroy(), lable3.destroy()
    lable5 = tkinter.Label(root, text = '\n \n \n \n \n \n \n', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable5.grid(row =0, column=0, columnspan=12, rowspan=7)
    lable4 = tkinter.Label(root, text = 'Activation Key', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable4.grid(row =10, column=0, columnspan=3)
    lable5 = tkinter.Label(root, text = 'Email Address', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable5.grid(row =11, column=0, columnspan=3)
    entry1 = tkinter.Entry(root, width=25, font = ('arial', 15, 'bold italic'),bd=10)
    entry2 = tkinter.Entry(root, width=25, font = ('arial', 15, 'bold italic'), bd=10)
    def validate():
        key = entry1.get()
        email = entry2.get()
        conn = sqlite3.connect('keys.db')
        c = conn.cursor()
        c.execute('SELECT * FROM data')
        L = [i[0] for i in c.fetchall()]
        database = open("C:/Tipan-App/data/bin.txt", 'w+')
        for i in range(len(L)):
            if key == 'Free':
                p_number = key[-1] + key[1:-1].lower()+key[0].lower()
                print('SOFTWARE ACTIVATION DETAILS:\nEmail {:s}\nKey {:s} \nProduct-Number {:s}'.format(email, '1230'+key+'qrst', p_number), file=database)
                lable6 = tkinter.Label(root, text = 'Congratulations!\n Your software have successfully been licenced.\nHowever some functionalities have been disabled.\n You are requested to restart This Application.',
                                font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                lable6.grid(row =14, column=0, columnspan=12, rowspan=4)
                functions.speak('free_version.wav')
                break
            elif L[i] != key and i == len(L):
                lable6 = tkinter.Label(root, text = 'Sorry!\n You have entered an invalid Key,\n Please buy one.',
                                font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                lable6.grid(row =14, column=0, columnspan=12, rowspan=3)
                functions.speak('activation failed.wav')
            elif L[i] == key:
                p_number = key[-1] + key[1:-1].lower()+key[0].lower()
                print('SOFTWARE ACTIVATION DETAILS:\nEmail {:s}\nKey {:s} \nProduct-Number {:s}'.format(email, '1230'+key+'qrst', p_number), file=database)
                lable6 = tkinter.Label(root, text = 'Congratulations!\n Your software have successfully been activated.\n You are requested to restart This Application.',
                                font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                lable6.grid(row =14, column=0, columnspan=12, rowspan=3)
                functions.speak('activation succeeded.wav')
                break
        database.close()
        conn.close()
    
    activate_button = tkinter.Button(root, bd=4,height=1, width=8, fg='black', font=('arial', 20, 'bold'),
                              text='Activate', bg='powder blue', command = validate )
    restart_button = tkinter.Button(root, bd=4,height=1, width=8, fg='black', font=('arial', 20, 'bold'),
                              text='Restart', bg='powder blue', command = functions.restart_program )
    entry1.grid(row=10, column=3)
    entry2.grid(row=11, column=3)
    activate_button.grid(row=12, column=0, columnspan=2)
    restart_button.grid(row=13, column=0, columnspan=2)
    
                

def mute():
    '''
        None type function, takes no argument and controls the sound of this application.
    '''
    global sound_state
    if sound_state == 0:
        sound_state = 1
    else:
        sound_state =0
    
def quitter_function():
    from tkinter.messagebox import askquestion
    """ Asks a user if not he/she is quitting the application intentionally
        Allowing them to continue quitting or cancel
        """
    answer = askquestion(title = 'Quit?', message = 'Really quit?')
    if answer == 'yes':
        root.destroy()

def buttonclick(number):
    """
        It uses the lambda function to bind events to buttons and keys on the keyboard
        it receives one argument which can be any character that must be given it when called.
        On clicking the button to which it has been used as a command option, the character is added to a global
        variable called operator which is displayed to the user in the StringVar.
        """
    global operator, result
    if (number == '/' or number == '*' or number == '+') and operator == '' and functions.is_numeric(result):
        operator = 'Ans' + str(number)
    else:
        operator = operator + str(number)
    text_input.set(operator)

def buttonclear():
    """ It empties the global string variable called operator by resetting its value back
        to that of an empty string. Characters in the string are cleared all at once.
        """
    global operator
    operator = ''
    text_input.set('')
def buttonclear_c():
    """ It empties the global string variable called operator by resetting its value back
        to that of an empty string. Characters in the string are cleared one by one starting from the extreme RIGHT.
        """
    global operator
    operator = operator[ : len(operator)-1]
    text_input.set(operator)

def detbutton():
    """ Its the callback function for the button needed for the determination of the determinant of a matrix,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok
    switchok = 3
    operator = 'Matrix?'
    text_input.set(operator)
    operator = ''
def inversebutton():
    """ Its the callback function for the button needed for the determination of the inverse of a matrix,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok
    switchok = 4
    operator = 'Matrix?'
    text_input.set(operator)
    operator = ''
def reductionbutton():
    """ Its the callback function for the button needed for the determination of the reduced form or echelon form of a matrix,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok
    switchok = 5
    operator = 'Matrix?'
    text_input.set(operator)
    operator = ''
def dotproduct():
    """ Its the callback function for the button needed for the determination of the dot product of two vectors,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count =0
    switchok = 6
    operator = 'a1?'
    text_input.set(operator)
    operator = ''
def crossproduct():
    """ Its the callback function for the button needed for the determination of the cross product of two vectors,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count =0
    switchok = 7
    operator = 'a1?'
    text_input.set(operator)
    operator = ''
def anglevector():
    """ Its the callback function for the button needed for the determination of the angle between two vectors,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 8
    operator = 'a1?'
    text_input.set(operator)
    operator = ''
def calculate():
    """ Its the callback function for the button needed for the evaluating substitutive expression where the user is
        suppose to substitute multiple numerical values in the same expression,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 9
    operator = 'Expression?'
    text_input.set(operator)
    operator = ''

def ok_button():
    """ Its the callback function for the button needed to evaluate expressions or data that is input after the program
        prompts the user to do so.
        """
    global collections, operator, count, switchok, result
    a1=[]
    a2=[]
    if switchok == 1:
        if count == 0:
            collections.append(operator)
            operator = 'Lower limit?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            operator = 'upper Limit?'
            text_input.set(operator)
            operator = ''
        if count == 2:
            collections.append(operator)
            operator = ''
            function = collections[0]
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt') 
                if color.get()==1:
                    function = function.replace('Sin', 'sin')
                    function = function.replace('Cos', 'cos')
                    function = function.replace('Tan', 'tan')
                    function = function.replace('aSin', 'asin')
                    function = function.replace('aCos', 'acos')
                    function = function.replace('aTan', 'atan')
            a = functions.tipa_parse_str(collections[1])
            b = functions.tipa_parse_str(collections[2])
            function = functions.tipa_parse_str(function)
            try:
                if a == b == '':
                    c = sp.integrals.integrate(function, x)
                    c = functions.math_display(str(c))
                    result = str(c)
                else:
                    a = eval(a)
                    b = eval(b)
                    c = functions.simpsons_rule(function, a, b)
                    result = functions.float_analyzer(c)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
                
    if switchok == 2:
        if count == 0:
            collections.append(operator)
            operator = 'Highest Power Of x?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            function = collections[0]
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                if color.get() == 1 or color.get() == 2:
                    function = function.replace('Sin', 'sin')
                    function = function.replace('Cos', 'cos')
                    function = function.replace('Tan', 'tan')
                    function = function.replace('aSin', 'asin')
                    function = function.replace('aCos', 'acos')
                    function = function.replace('aTan', 'atan')
            try:
                a = eval(collections[1])
                result = functions.TaylorSeries(function, a)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
        

   
    if switchok == 3:
        try:
            A = sp.Matrix(eval(operator))
            ans = A.det()
            result = str(ans)
            text_input.set(result)
        except ZeroDivisionError :
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('zerodivisor.wav')
            operator = ''
        except SyntaxError:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('synthax error.wav')
            operator = ''
        except:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('Unknown Synthax.wav')
            operator = ''
        
    if switchok == 4:
        try:
            A = sp.Matrix(eval(operator))
            ans = A.inv()
            result = str(ans)
            text_input.set(result)
        except ZeroDivisionError :
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('zerodivisor.wav')
            operator = ''
        except SyntaxError:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('synthax error.wav')
            operator = ''
        except:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('Unknown Synthax.wav')
            operator = ''
        
    if switchok == 5:
        try:
            A = sp.Matrix(eval(operator))
            ans = A.rref()
            result = str(ans)
            text_input.set(result)
        except ZeroDivisionError :
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('zerodivisor.wav')
            operator = ''
        except SyntaxError:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('synthax error.wav')
            operator = ''
        except:
            operator = 'Math Error!'
            text_input.set(operator)
            if sound_state == 0:
                functions.speak('Unknown Synthax.wav')
            operator = ''
        
    if switchok == 6:
        if count == 0:
            collections.append(operator)
            operator = 'a2 ?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            try:
                a1.append(eval(collections[0]))
                a2.append(eval(collections[1]))
                ans = sp.Matrix(a1).dot(sp.Matrix(a2))
                result = str(ans)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
            
    if switchok == 7:
        if count == 0:
            collections.append(operator)
            operator = 'a2 ?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            try:
                collections.append(operator)
                a1.append(eval(collections[0]))
                a2.append(eval(collections[1]))
                ans = sp.Matrix(a1).cross(sp.Matrix(a2))
                result = str(ans)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
            
    if switchok == 8:
        if count == 0:
            collections.append(operator)
            operator = 'a2 ?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            try:
                a1.append(eval(collections[0]))
                a2.append(eval(collections[1]))
                M1 = sp.Matrix(a1)
                M2 = sp.Matrix(a2)
                if color.get()==1:
                    ans = acos(M1.dot(M2)/(M1.norm() * M2.norm() ))
                else:
                    ans = aCos(M1.dot(M2)/(M1.norm() * M2.norm() ))
                result = str(ans)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
            
    if switchok == 9:
        if count == 0:
            collections.append(operator)
        if count == 0 or count%2 == 0:
            operator = 'x ?'
            text_input.set(operator)
            operator = ''
        else:
            function = collections[0]
            value = operator
            for t in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                function = function.replace('π', 'pi')
                if color.get()==1:
                    function = function.replace('Sin', 'sin')
                    function = function.replace('Cos', 'cos')
                    function = function.replace('Tan', 'tan')
                    function = function.replace('aSin', 'asin')
                    function = function.replace('aCos', 'acos')
                    function = function.replace('aTan', 'atan')
            function = functions.tipa_parse_str(function)
            function = parse_expr(function)
            try:
                function = str(function.subs(x, value))
                ans = eval(function)
                result = str(ans)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
            
    if switchok == 10:
        if count == 0:
            collections.append(operator)
            operator = 'x ?'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            function = collections[0]
            value = collections[1]
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('exp', 'exp')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                function = function.replace('S', 's')
                function = function.replace('C', 'c')
                function = function.replace('T', 't')
            function = functions.tipa_parse_str(function)
            try:
                ans = sp.integrals.diff(function,x)
                if value == '':
                    ans = str(ans)
                    ans = functions.math_display(ans)
                else:
                    ans = ans.subs(x, value)
                    ans = str(eval(str(ans)))
                    ans = functions.float_analyzer(ans)
                result = ans
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
        

    if switchok == 11:
        if count == 0:
            collections.append(operator)
            operator = 'L-value of x'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            operator = 'H-value of x?'
            text_input.set(operator)
            operator = ''
        if count == 2:
            collections.append(operator)
            function = collections[0]
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                function = function.replace('S', 's')
                function = function.replace('C', 'c')
                function = function.replace('T', 't')
            function = functions.tipa_parse_str(function)
            try:
                a = eval(functions.tipa_parse_str(collections[1]))
                b = eval(functions.tipa_parse_str(collections[2]))
                functions.graph_plot(function, a, b)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
                
    if switchok == 12:
        if count == 0:
            collections.append(operator)
            operator = 'Lower-limit'
            text_input.set(operator)
            operator = ''
        if count == 1:
            collections.append(operator)
            operator = 'Upper-limit?'
            text_input.set(operator)
            operator = ''
        if count == 2:
            collections.append(operator)
            function = collections[0]
            a = eval(functions.tipa_parse_str(collections[1]))
            b = eval(functions.tipa_parse_str(collections[2]))
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                function = function.replace('S', 's')
                function = function.replace('C', 'c')
                function = function.replace('T', 't')
            try:
                if color4.get() == 0:
                    ans = functions.Fourier_Transform(function, a, b)
                else:
                    function = functions.tipa_parse_str(function)
                    ans = inverse_fourier_transform(function, k, x)
                result = functions.math_display(str(ans))
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
    if switchok == 13:
        if count == 0 and color4.get() == 0:
            collections.append(operator)
            operator = 'Upper-limit'
            text_input.set(operator)
            operator = ''
        elif count ==0 and color4.get() != 0:
            count = 1
        if count == 1:
            if color4.get() == 0:
                collections.append(operator)
                a = eval(functions.tipa_parse_str(collections[1]))
                function = collections[0]
            else:
                function = operator
            for x2 in function:
                function = function.replace('\u00b2', '**2')
                function = function.replace('E', '*10**')
                function = function.replace('\u00b3', '**3')
                function = function.replace('^', '**')
                function = function.replace('̷', '/')
                function = function.replace('Ans', result)
                function = function.replace('ln', 'log')
                function = function.replace('π', 'pi')
                function = function.replace('log10', '(1/log(10))*log')
                function = function.replace('√', 'sqrt')
                function = function.replace('S', 's')
                function = function.replace('C', 'c')
                function = function.replace('T', 't')
            try:
                if color4.get() == 0:
                    ans = functions.Laplace_Transform(function, a)
                else:
                    function = functions.tipa_parse_str(function)
                    ans = functions.Inverse_Laplace_Transform(function)
                result = functions.math_display(ans)
                text_input.set(result)
            except ZeroDivisionError :
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('zerodivisor.wav')
                operator = ''
            except SyntaxError:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('synthax error.wav')
                operator = ''
            except:
                operator = 'Math Error!'
                text_input.set(operator)
                if sound_state == 0:
                    functions.speak('Unknown Synthax.wav')
                operator = ''
        
    count+=1
        
def frac():
    """ Its the callback function for the button needed by the user to convert a given value in to a fraction.
        """
    global operator
    y = displayscreen.get()
    flag =0
    Bool = 0
    try:
        for i in y:
            if i == '/':
                flag = 1
                break
        if flag == 1:
            result = eval(y)
        else:
            result = functions.decimal_to_fraction(eval(y))
        text_input.set(result)
    except ZeroDivisionError :
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('zerodivisor.wav')
        operator = ''
    except SyntaxError:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('synthax error.wav')
        operator = ''
    except:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('Unknown Synthax.wav')
        operator = ''
def time_function():
    '''
    None type, it performs time calculation.
    It converts calculated time into hours, minutes, seconds and microseconds and vice versa.
    '''
    global operator
    y = displayscreen.get()
    flag =0
    for i in y:
        if i == '\u2032':
            flag = 1
            break
    try:
        if flag == 1:
            a = y.split('\u2032')
            try:
                ans = eval(a[0]) + eval(a[1])/60
            except:
                b = a[1].split('\u2033')
                try:
                    ans = eval(a[0]) + eval(b[0])/60 + eval(b[1])/3600
                except:
                    c = b[1].split('\u2034')
                    ans = eval(a[0]) + eval(b[0])/60 + eval(c[0])/3600 + eval(c[1])/360000
            time = str(ans)
        else:
            y = eval(y)
            H = int(y); r = (y - H) * 60
            M = int(r); r = (r - M) * 60
            S = int(r); r = (r - S) * 100
            mS = int(r)
            time = str(H)+'\u2032'+str(M)+"\u2033"+str(S)+"\u2034"+str(mS)
        text_input.set(time)
    except ZeroDivisionError :
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('zerodivisor.wav')
        operator = ''
    except SyntaxError:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('synthax error.wav')
        operator = ''
    except:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('Unknown Synthax.wav')
            operator = ''
        
def Arg(x):
    """ It accepts one argument in complex form
        it then evaluates the argument of that complex number number
        It returns the angle in radians or degrees depending on the state of the variable color..
        """
    angle = atan(x.imag/x.real)
    return angle if color==1 else degrees(angle)
def Integral():
    """ Its the callback function for the button needed for the evaluation of the definite integral of a function,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 1
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
    
def Taylor_series():
    """ Its the callback function for the button needed for the evaluation of the line integral along a given curve in a vector field,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 2
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
def Fourier():
    """ Its the callback function for the button needed for the evaluation of fourier transform,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 12
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
def Laplace():
    """ Its the callback function for the button needed for the evaluation of laplace transform,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 13
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
def Differentiation():
    """ Its the callback function for the button needed for the determination of the dot product of two vectors,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    count =  0; collections = []
    switchok = 10
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
def plots():
    """ Its the callback function for the button needed for plotting functions specified by the user,
        it works in collaboration with the 'OK' button
        """
    global operator, switchok, count, collections
    collections = []
    count = 0
    switchok = 11
    operator = 'Function?'
    text_input.set(operator)
    operator = ''
def complex_p():
    """ Its the callback function for the button needed computing a complex number raised to the nth power specified by the user,
        it works in collaboration with the 'OK' button
        """
    global operator, switchequal, count
    switchequal = 1
    count = 0
    operator = 'p('
    text_input.set(operator)
def clear_memory():
    '''
    Clears items stored in the temporarily created memory.
    '''
    global Memory
    Memory = []

def add_item_to_memory():
    '''
    Creates a memory that can be used to store data as the program runs, and each time it is clicked the current entry
    in the entrybox is copied and stored in the memory.
    '''
    global Memory
    Memory.append(displayscreen.get())
def recall_from_memory():
    '''
    returns items stored in the memory one after the other each time it is called.
    '''
    global Memory, memory_counter, operator
    if Memory == []:
        operator = ''
        text_input.set(operator)
    else:
        n = len(Memory)
        if memory_counter < n:
            operator = Memory[memory_counter]
            text_input.set(operator)
        else:
            memory_counter = 0
            operator = Memory[memory_counter]
            text_input.set(operator)
        memory_counter+=1
def remove_item_from_memory():
    '''
    Removes items stored in the memory one by one.
    '''
    global Memory
    a = displayscreen.get()
    for i in range(len(Memory)):
        if Memory[i] == a:
            Memory[i] = ''
            break
        else:
            speak('You have not stored such an item in the memory.')
            break
            

def buttonequal():
    """ Its the callback function for the button needed for the evaluation of data input at once in the display screen
        """
    global operator, result, switchequal
    for x2 in operator:
        operator = operator.replace('\u00b2', '**2')
        operator = operator.replace('E', '*10**')
        operator = operator.replace('\u00b3', '**3')
        operator = operator.replace('^', '**')
        operator = operator.replace('̷', '/')
        operator = operator.replace('Ans', result)
        operator = operator.replace('ln', 'log')
        operator = operator.replace('log10', '(1/log(10))*log')
        for i in range(len(operator)):
            if operator[i]=='C' and operator[i+1]!='o':
                operator = operator.replace('C', 'comb')
        operator = operator.replace('P', 'perm')
        operator = operator.replace('√', 'sqrt') 
        if color.get()==1:
            operator = operator.replace('Sin', 'sin')
            operator = operator.replace('Cos', 'cos')
            operator = operator.replace('Tan', 'tan')
            operator = operator.replace('aSin', 'asin')
            operator = operator.replace('aCos', 'acos')
            operator = operator.replace('aTan', 'atan')
    try:
        if switchequal == 0:
            try:
               ans = eval(functions.tipa_parse_str(operator)).evalf()
            except:
                ans = eval(functions.tipa_parse_str(operator))
        elif switchequal == 1:
            ans = eval(operator)
        result = str(ans)
        text_input.set(result)
        operator = ''
    except ZeroDivisionError :
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('zerodivisor.wav')
        operator = ''
    except SyntaxError:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('synthax error.wav')
        operator = ''
    except:
        operator = 'Math Error!'
        text_input.set(operator)
        if sound_state == 0:
            functions.speak('Unknown Synthax.wav')
            operator = ''

def Disable_Function():
    global operator
    operator = 'Button disabled'
    text_input.set(operator)
    if sound_state == 0:
        functions.speak('disabled_button.wav')
        

#=======================main=============================================================================================================





s_detail = functions.serialisation()
STATE = 'disabled' if s_detail == 1 else 'normal'
if s_detail == 1 or s_detail == 2 :
    frame1 = tkinter.Frame(root, width = 600, height = 15, bg = 'powder blue', relief = tkinter.SUNKEN)
    frame1.pack(side = tkinter.TOP)
    frame2 = tkinter.Frame(root, width = 600, height =650,  bg = 'powder blue', relief = tkinter.SUNKEN)
    frame2.pack(side = tkinter.LEFT)
    frame4 = tkinter.Frame(frame2, width = 600, height =50, bg = 'brown', relief = tkinter.SUNKEN)
    frame4.pack(side = tkinter.TOP)
    frame5 = tkinter.Frame(frame2, width = 400, height =600, bg = 'green', relief = tkinter.SUNKEN)
    frame5.pack(side = tkinter.LEFT)
    frame6 = tkinter.Frame(frame2, width = 200, height =600, bg = 'yellow', relief = tkinter.SUNKEN)
    frame6.pack(side = tkinter.RIGHT)
    Heading = tkinter.Label(frame1, text = 'The Tipan Calculator, Your Favorite', font = ('arial', 20, 'bold italic'), bg = 'purple', fg='Steel Blue', bd=10, anchor='w')
    Heading.grid(row =0, column=0, columnspan = 12)
    developers_website = ttk.Button(frame1,
                                       text='Developers Website', command=functions.Webpage)
    developers_website.grid(row=2, column=0)

    color = tkinter.IntVar()
    color2 = tkinter.IntVar()
    color3 = tkinter.IntVar()
    color4 = tkinter.IntVar()
    color5 = tkinter.IntVar()
    color.set(2)
    color4.set(0)
    rads = tkinter.Radiobutton(frame5, text='Rad', var=color, value=1).grid(row=0, column=0)
    degs = tkinter.Radiobutton(frame5, text='Deg', var=color, value=2).grid(row=0, column=1)
    Eqn = tkinter.Radiobutton(frame5, text='Eqns', var=color2, value=1, command=equat.equation if s_detail == 1 else Disable_Function).grid(row=0, column=2)
    shift = tkinter.Checkbutton(frame5, text='shift', var=color4).grid(row=0, column=3)


    displayscreen = tkinter.Entry(frame4, font = ('arial', 20, 'bold'), textvariable = text_input, bd=30, insertwidth=4, bg='powder blue', justify='right')
    displayscreen.grid(columnspan=5)
    mute_sound = ttk.Checkbutton(frame1, text='Mute Sound', var=color3, command = mute).grid(row=2, column=1)
    purchased_key = ttk.Checkbutton(frame1, state = STATE, text='Activate Product', var=color5, command = equat.activate_later).grid(row=2, column=3)
    restart_button = ttk.Checkbutton(frame1, text='Restart', var=color5, command = functions.restart_program).grid(row=2, column=4)
#   displayscreen.focus()
    root.bind('<Return>', lambda dummy=0:buttonequal())
    root.bind('<space>', lambda dummy=0:ok_button())
    root.bind('[', lambda dummy=0:buttonclick('['))
    root.bind(']', lambda dummy=0:buttonclick(']'))
    root.bind('(', lambda dummy=0:buttonclick('('))
    root.bind(')', lambda dummy=0:buttonclick(')'))
    root.bind('+', lambda dummy=0:buttonclick('+'))
    root.bind('-', lambda dummy=0:buttonclick('-'))
    root.bind('*', lambda dummy=0:buttonclick('*'))
    root.bind('/', lambda dummy=0:buttonclick('/'))
    root.bind('1', lambda dummy=0:buttonclick('1'))
    root.bind('2', lambda dummy=0:buttonclick('2'))
    root.bind('3', lambda dummy=0:buttonclick('3'))
    root.bind('4', lambda dummy=0:buttonclick('4'))
    root.bind('5', lambda dummy=0:buttonclick('5'))
    root.bind('6', lambda dummy=0:buttonclick('6'))
    root.bind('7', lambda dummy=0:buttonclick('7'))
    root.bind('8', lambda dummy=0:buttonclick('8'))
    root.bind('9', lambda dummy=0:buttonclick('9'))
    root.bind('0', lambda dummy=0:buttonclick('0'))
    root.bind('.', lambda dummy=0:buttonclick('.'))
    root.bind(',', lambda dummy=0:buttonclick(','))
    root.bind('x', lambda dummy=0:buttonclick('x'))
    root.bind('j', lambda dummy=0:buttonclick('j'))
    root.bind('\'', lambda dummy=0:buttonclick(functions.apostrophe(operator)))
    root.bind('t', lambda dummy=0:buttonclick('t'))
    root.bind('s', lambda dummy=0:buttonclick('s'))
    root.bind('k', lambda dummy=0:buttonclick('k'))
    root.bind('i', lambda dummy=0:buttonclick('i'))
    root.bind('n', lambda dummy=0:buttonclick('n'))
    root.bind('c', lambda dummy=0:buttonclick('c'))
    root.bind('o', lambda dummy=0:buttonclick('o'))
    root.bind('a', lambda dummy=0:buttonclick('a'))
    root.bind('w', lambda dummy=0:buttonclick('w'))
    root.bind('y', lambda dummy=0:buttonclick('y'))
    root.bind('z', lambda dummy=0:buttonclick('z'))
    root.bind('u', lambda dummy=0:buttonclick('u'))
    root.bind('b', lambda dummy=0:buttonclick('b'))
    root.bind('<BackSpace>',  lambda dummy=0:buttonclear_c() )
    clear=tkinter.Button(frame4, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                   text='Clear', bg='powder blue', command= buttonclear).grid(row=0, column=5)

#=====================================================================Buttons========================================================================
    button7=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='7', bg='powder blue', command=lambda: buttonclick(7)).grid(row=3, column=0)
    button8=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='8', bg='powder blue', command=lambda: buttonclick(8)).grid(row=3, column=1)
    button9=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='9', bg='powder blue', command=lambda: buttonclick(9)).grid(row=3, column=2)
    addition=tkinter.Button(frame5,padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='+', bg='powder blue', command=lambda: buttonclick('+')).grid(row=1, column=0)
    Subtraction=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', width=2, font=('arial', 20, 'bold'),
               text='-', bg='powder blue', command=lambda: buttonclick('-')).grid(row=1, column=1)
    sines=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 16, 'bold'),
               text='sin', bg='powder blue', command=lambda: buttonclick('Sin(') if s_detail == 1 else None).grid(row=1, column=0)
    cosines=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 15, 'bold'),
               text='cos', bg='powder blue', command=lambda: buttonclick('Cos(') if s_detail == 1 else None).grid(row=1, column=1)
    tangents=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 16, 'bold'),
               text='tan', bg='powder blue', command=lambda: buttonclick('Tan(') if s_detail == 1 else None).grid(row=1, column=2)
    hsines=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='sinh', bg='powder blue', command=lambda: buttonclick('sinh(') if s_detail == 1 else None).grid(row=2, column=0)
    hcosines=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='cosh', bg='powder blue', command=lambda: buttonclick('cosh(') if s_detail == 1 else None).grid(row=2, column=1)
    htangents=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='tanh', bg='powder blue', command=lambda: buttonclick('tanh(') if s_detail == 1 else None).grid(row=2, column=2)
#=======================================================================Buttons=============================================================================
    button6=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='6', bg='powder blue', command=lambda: buttonclick(6)).grid(row=4, column=0)
    button5=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='5', bg='powder blue', command=lambda: buttonclick(5)).grid(row=4, column=1)
    button4=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='4', bg='powder blue', command=lambda: buttonclick(4)).grid(row=4, column=2)
    multiplication=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='×', bg='powder blue', command=lambda: buttonclick('*')).grid(row=1, column=2)
    division=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', width=2, font=('arial', 20, 'bold'),
               text='÷', bg='powder blue', command=lambda: buttonclick('/')).grid(row=1, column=3)
    Arcsine=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='Asin', bg='powder blue', command=lambda: buttonclick('aSin(') if s_detail == 1 else None).grid(row=3, column=0)
    Arccosine=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='Acos', bg='powder blue', command=lambda: buttonclick('aCos(') if s_detail == 1 else None).grid(row=3, column=1)
    Arctangent=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='Atan', bg='powder blue', command=lambda: buttonclick('aTan(') if s_detail == 1 else None).grid(row=3, column=2)
    ahsine=tkinter.Button(frame6,height=1, pady=4, bd=4, fg='black', font=('arial', 10, 'bold'),
               text='Asinh', bg='powder blue', command=lambda: buttonclick('asinh(') if s_detail == 1 else None).grid(row=4, column=0)
    ahcosine=tkinter.Button(frame6,height=1, pady=4, bd=4, fg='black', font=('arial', 10, 'bold'),
               text='Acosh', bg='powder blue', command=lambda: buttonclick('acosh(') if s_detail == 1 else None).grid(row=4, column=1)
    ahtangent=tkinter.Button(frame6,height=1, pady=4, bd=4, fg='black', font=('arial', 10, 'bold'),
               text='Atanh', bg='powder blue', command=lambda: buttonclick('atanh(') if s_detail == 1 else None).grid(row=4, column=2)
    dot_product=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='.pdt', bg='powder blue', command=dotproduct if s_detail == 1 else Disable_Function).grid(row=7, column=1)
    cross_product=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='xpdt', bg='powder blue', command=crossproduct if s_detail == 1 else Disable_Function).grid(row=7, column=2)
    angle_vectors=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text='<', bg='powder blue', command=anglevector if s_detail == 1 else Disable_Function).grid(row=8, column=1)
#=====================================================================Buttons================================================================================
    button3=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='3', bg='powder blue', command=lambda: buttonclick(3)).grid(row=5, column=0)
    button2=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='2', bg='powder blue', command=lambda: buttonclick(2)).grid(row=5, column=1)
    button1=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='1', bg='powder blue', command=lambda: buttonclick(1)).grid(row=5, column=2)
    openbrace=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', width=2, font=('arial', 19, 'bold'),
               text='(', bg='powder blue', command=lambda: buttonclick('(')).grid(row=2, column=0)
    closebrace=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', width=2, font=('arial', 19, 'bold'),
               text=')', bg='powder blue', command=lambda: buttonclick(')')).grid(row=2, column=1)
    log10=tkinter.Button(frame5, bd=4, fg='black', height=2, width=4, font=('arial', 15, 'bold'),
               text='log', bg='powder blue', command=lambda: buttonclick('log10(') if s_detail == 1 else None).grid(row=1, column=4)
    loge=tkinter.Button(frame5, pady=4, bd=4, fg='black', height=2, width=4, font=('arial', 15, 'bold'),
               text='ln', bg='powder blue', command=lambda: buttonclick('ln(') if s_detail == 1 else None).grid(row=2, column=4)
    e_x=tkinter.Button(frame5,width =4, bd=4, fg='black', height=2, font=('arial', 16, 'bold'),
               text='e ͯ', bg='powder blue', command=lambda: buttonclick('exp(') if s_detail == 1 else None).grid(row=3, column=4)
    absolute=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='Abs', bg='powder blue', command=lambda: buttonclick('abs(') if s_detail == 1 else None).grid(row=6, column=2)
    argument=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='Arg', bg='powder blue', command=lambda: buttonclick('Arg(') if s_detail == 1 else None).grid(row=5, column=0)
    cpow=tkinter.Button(frame6, width=3, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='Z\u207F', bg='powder blue', command=complex_p if s_detail == 1 else Disable_Function).grid(row=5, column=1)
    solvebutton = tkinter.Button(frame6, pady=3, bd=4, fg='black', font=('arial', 13, 'bold'),
                     text='solve', bg='powder blue', command =  calculate if s_detail == 1 else Disable_Function).grid(row=5, column=2)
    j_button=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text='J', bg='powder blue', command=lambda: buttonclick('j')).grid(row=8, column=2)
    cons_pi=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 18, 'bold'),
               text='π', bg='powder blue', command=lambda: buttonclick('pi')).grid(row=6, column=2)
    comma=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', width=2, font=('arial', 20, 'bold'),
               text=',', bg='powder blue', command=lambda: buttonclick(',')).grid(row=6, column=3)
    square=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 18, 'bold'),
               text='x\u00b2', bg='powder blue', command=lambda: buttonclick('\u00b2') if s_detail == 1 else None).grid(row=5, column=3)
    cube=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 18, 'bold'),
               text='x\u00b3', bg='powder blue', command=lambda: buttonclick('\u00b3') if s_detail == 1 else None).grid(row=5, column=4)
#==========================================================================Buttons=========================================================================
    button0=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='0', bg='powder blue', command=lambda: buttonclick(0)).grid(row=6, column=0)
    buttonfloat=tkinter.Button(frame5, padx=8, pady=4, bd=8, fg='black', font=('arial', 20, 'bold'),
               text='.', bg='powder blue', command=lambda: buttonclick('.')).grid(row=6, column=1)
    equals=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='=', bg='powder blue', command=buttonequal).grid(row=3, column=3)
    answer=tkinter.Button(frame5, pady=4, bd=4, fg='black', height=2, font=('arial', 16, 'bold'),
               text='Ans', bg='powder blue', command=lambda: buttonclick('Ans') if s_detail == 1 else None).grid(row=4, column=3)
    exponential=tkinter.Button(frame5, pady=5, bd=4, fg='black', height=2, font=('arial', 14, 'bold'),
               text='EXP', bg='powder blue', command=lambda: buttonclick('E') if s_detail == 1 else None).grid(row=2, column=3)
    power=tkinter.Button(frame5,pady=5, padx=4, width=3, bd=4, fg='black', height=2, font=('arial', 14, 'bold'),
               text='X\u207F', bg='powder blue', command=lambda: buttonclick('^') if s_detail == 1 else None).grid(row=2, column=2)
    combinations=tkinter.Button(frame6, pady=8, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='nCr', bg='powder blue', command=lambda: buttonclick('C(') if s_detail == 1 else None).grid(row=0, column=1)
    permutations=tkinter.Button(frame6,pady=8, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='nPr', bg='powder blue', command=lambda: buttonclick('P(') if s_detail == 1 else None).grid(row=0, column=2)
    facts=tkinter.Button(frame6, padx=4, bd=4, fg='black', font=('arial', 18, 'bold'),
               text='n!', bg='powder blue', command=lambda: buttonclick('fact(') if s_detail == 1 else None).grid(row=0, column=0)
    squareroot=tkinter.Button(frame5, padx=8, pady=8, bd=4, fg='black', font=('arial', 20, 'bold'),
               text='√', bg='powder blue', command = lambda: buttonclick('√(') if s_detail == 1 else None).grid(row=6, column=4)
    integration=tkinter.Button(frame6, padx=10, pady=4, bd=8, fg='black', font=('arial', 14, 'bold'),
               text='∫', bg='powder blue', command = Integral if s_detail == 1 else Disable_Function).grid(row=0, column=3)
    maclaurins_series=tkinter.Button(frame6, width=3, padx=5, pady=4, bd=8, fg='black', font=('arial', 10, 'bold'),
               text='series', bg='powder blue', command=Taylor_series if s_detail == 1 else Disable_Function).grid(row=1, column=3)
    differentiation=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='Diff', bg='powder blue', command=Differentiation if s_detail == 1 else Disable_Function).grid(row=2, column=3)
    graph_plotting=tkinter.Button(frame6, padx=3, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='Plot', bg='powder blue', command=plots if s_detail == 1 else Disable_Function).grid(row=3, column=3)
    memory=tkinter.Button(frame6, padx=4, width=3, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='M', bg='powder blue', command=recall_from_memory).grid(row=4, column=3)
    memory_add_item=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='M+', bg='powder blue', command=add_item_to_memory).grid(row=5, column=3)
    memory_remove_item=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='M-', bg='powder blue', command=remove_item_from_memory).grid(row=6, column=3)
    memory_clear=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='MC', bg='powder blue', command=clear_memory).grid(row=7, column=3)
    expressFraction=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 13, 'bold'),
               text='a/b', bg='powder blue', command=frac).grid(row=8, column=3)
    Time_operation=tkinter.Button(frame6, padx=4, bd=6, fg='black', font=('arial', 14, 'bold'),
               text='◦,,,', bg='powder blue', command=time_function if s_detail == 1 else Disable_Function).grid(row=9, column=3)
    okbutton=tkinter.Button(frame5, pady=12, bd=4, fg='black', height=1, font=('arial', 18, 'bold'),
               text='Ok', bg='powder blue', command=ok_button if s_detail == 1 else Disable_Function).grid(row=4, column=4)
    x_button=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text='x', bg='powder blue', command=lambda:buttonclick('x')).grid(row=8, column=0)
    t_button=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text='\u2032', bg='powder blue', command=lambda:buttonclick(apostrophe(operator))).grid(row=9, column=2)
    det_button=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='Det', bg='powder blue', command=detbutton if s_detail == 1 else Disable_Function).grid(row=6, column=0)
    inverse_button=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 14, 'bold'),
               text='Inv', bg='powder blue', command=inversebutton if s_detail == 1 else Disable_Function).grid(row=6, column=1)
    rref_button=tkinter.Button(frame6, bd=4, fg='black', font=('arial', 13, 'bold'),
               text='Rred', bg='powder blue', command=reductionbutton if s_detail == 1 else Disable_Function).grid(row=7, column=0)
    sqbracketo=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text='[', bg='powder blue', command=lambda:buttonclick('[')).grid(row=9, column=0)
    sqbracketc_button=tkinter.Button(frame6, bd=4, fg='black', width=3, font=('arial', 16, 'bold'),
               text=']', bg='powder blue', command=lambda:buttonclick(']')).grid(row=9, column=1)
    fourier_transformation=tkinter.Button(frame6, bd=4,height=1, width=8, fg='black', font=('arial', 16, 'bold'),
               text='F-Trans', bg='powder blue', command=Fourier if s_detail == 1 else Disable_Function).grid(row=10, column=0, columnspan=2)
    laplace_transformation=tkinter.Button(frame6, bd=4,height=1, width=8, fg='black', font=('arial', 16, 'bold'),
               text='L-Trans', bg='powder blue', command=Laplace if s_detail == 1 else Disable_Function).grid(row=10, column=2, columnspan=2)
else:
    root.geometry("700x670")
    lable1 = tkinter.Label(root, text = 'Thanks For acquiring this piece of software', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable1.grid(row =0, column=0, columnspan=12)
    
    lable2 = tkinter.Label(root, text = '''We highly recommend that you purchase yourself an activation key,
                                    \ncurrently our online server is down to enable automatic
                                       \nvalidation of the key therefore our ample appologies.
                                       \nHowever our agents will do the activation for you in person,
                                       \nplease contact Stephen Tipa on 0772740796 or 0756916213
                                                   \n or even physically
                                                       \nfor more assistance.''',
                   font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable2.grid(row =1, column=0, rowspan=6, columnspan=12)
    
    lable3 = tkinter.Label(root, text = 'If you have an activation key, please click the below button.', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
    lable3.grid(row =8, column=0, columnspan=10)
    
    activation_button=ttk.Button(root, text='Activate', command=activation)
    activation_button.grid(row=11, column=0, columnspan=2)
    functions.speak('intro.wav')




import os
import errno

filename = "/foo/bar/baz.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write("FOOBAR")
    
#=======================================================================================================================================================


root.protocol('WM_DELETE_WINDOW', quitter_function)
root.mainloop()
