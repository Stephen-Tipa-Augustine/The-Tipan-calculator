from math import *
from sympy.abc import x, s, t, j, a, w, v, n, m, k, y, z
from sympy import sqrt, sin, cos, tan, log, series, integrate, evalf, re, im, oo, solve, Abs, inverse_laplace_transform, simplify, inverse_fourier_transform
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from fractions import Fraction
import sqlite3
import tkinter
import os, errno

class equat:
    @staticmethod
    def activate_later():
        main = tkinter.Toplevel()
        frame = tkinter.Frame(main, width =600, height = 670)
        frame.grid(row=0, column=0)
        lable5 = tkinter.Label(frame, text = '\n \n \n \n \n \n \n', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
        lable5.grid(row =0, column=0, columnspan=12, rowspan=7)
        lable4 = tkinter.Label(frame, text = 'Activation Key', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
        lable4.grid(row =10, column=0, columnspan=3)
        lable5 = tkinter.Label(frame, text = 'Email Address', font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
        lable5.grid(row =11, column=0, columnspan=3)
        entry1 = tkinter.Entry(frame, width=25, font = ('arial', 15, 'bold italic'),bd=10)
        entry2 = tkinter.Entry(frame, width=25, font = ('arial', 15, 'bold italic'), bd=10)
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
                    lable6 = tkinter.Label(frame, text = 'Congratulations!\n Your software have successfully been licenced.\nHowever some functionalities have been disabled.\n You are requested to restart This Application.',
                                    font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                    lable6.grid(row =14, column=0, columnspan=12, rowspan=4)
                    functions.speak('free_version.wav')
                    break
                elif L[i] != key and i == len(L):
                    lable6 = tkinter.Label(frame, text = 'Sorry!\n You have entered an invalid Key,\n Please buy one.',
                                    font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                    lable6.grid(row =14, column=0, columnspan=12, rowspan=3)
                    functions.speak('activation failed.wav')
                elif L[i] == key:
                    p_number = key[-1] + key[1:-1].lower()+key[0].lower()
                    print('SOFTWARE ACTIVATION DETAILS:\nEmail {:s}\nKey {:s} \nProduct-Number {:s}'.format(email, '1230'+key+'qrst', p_number), file=database)
                    lable6 = tkinter.Label(frame, text = 'Congratulations!\n Your software have successfully been activated.\n You are requested to restart This Application.',
                                    font = ('arial', 15, 'bold italic'), fg='Steel Blue', bd=10, anchor='w')
                    lable6.grid(row =14, column=0, columnspan=12, rowspan=3)
                    functions.speak('activation succeeded.wav')
                    break
            database.close()
            conn.close()
    
        activate_button = tkinter.Button(frame, bd=4,height=1, width=8, fg='black', font=('arial', 20, 'bold'),
                                  text='Activate', bg='powder blue', command = validate )
        restart_button = tkinter.Button(frame, bd=4,height=1, width=8, fg='black', font=('arial', 20, 'bold'),
                                  text='Restart', bg='powder blue', command = functions.restart_program )
        entry1.grid(row=10, column=3)
        entry2.grid(row=11, column=3)
        activate_button.grid(row=12, column=0, columnspan=2)
        restart_button.grid(row=13, column=0, columnspan=2)
        


    @staticmethod
    def equation():
        equations = tkinter.Toplevel()
        equations.resizable(False, False)
        equations.geometry("1340x640+0+0")
        frame7 = tkinter.Frame(equations, width = 800, height = 5, bg = 'blue', relief = tkinter.SUNKEN)
        frame7.pack(side = tkinter.TOP)
        frame8 = tkinter.Frame(equations, width = 500, height =600,  bg = 'green', relief = tkinter.SUNKEN)
        frame8.pack(side = tkinter.LEFT)
        frame9 = tkinter.Frame(equations, width = 500, height =600, bg = 'yellow', relief = tkinter.SUNKEN)
        frame9.pack(side = tkinter.RIGHT)
        frame10 = tkinter.Frame(equations, width = 800, height =50, bg = 'brown', relief = tkinter.SUNKEN)
        Heading = tkinter.Label(frame7, text = 'Solutions To Equations', font = ('arial', 20, 'bold italic'), bg = 'purple', fg='Steel Blue', bd=10, anchor='w')
        Heading.grid(row =0, column=0)
        f2 = tkinter.Frame(frame8,  width = 400, height = 2, bg = 'blue', relief = tkinter.SUNKEN)
        f2.grid(row=0, column=0, rowspan=2, columnspan=500 )
        #=========================================1-Linear equations=====================================================================================
        #=========================================2-Unknowns=============================================================================================
        label0 = tkinter.Label(f2, text = 'Linear Equations:', font = ('arial', 20, 'bold italic'),
                       fg='Steel Blue', bd=10, anchor='w').grid(row=0,column=0, columnspan=3)
        label02 = tkinter.Label(f2, text = 'Form: ax + by = c:', font = ('arial', 20, 'bold italic'),
                       fg='Steel Blue', bd=10, anchor='w').grid(row=1,column=0, columnspan=3)
        labelf = tkinter.Label(frame8, text='For the First equation:', font=('arial', 20, 'bold italic'), fg='steel Blue', bd=10, anchor='w').grid(row=2, column=0, columnspan=3)
        labels = tkinter.Label(frame8, text='For the second equation:', font=('arial', 20, 'bold italic'), fg='steel Blue', bd=10, anchor='w').grid(row=3, column=0, columnspan=3)
        label1 = tkinter.Label(frame8, text='x +', font=('arial', 20, 'italic'), bg='powder Blue').grid(row=2, column=4)
        label1 = tkinter.Label(frame8, text='y =', font=('arial', 20, 'italic'), bg='powder Blue').grid(row=2, column=6)
        entry1 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        entry2 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        entry3 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        label2 = tkinter.Label(frame8, text='x +', font=('arial', 20, 'italic'), bg='powder Blue').grid(row=3, column=4)
        label3 = tkinter.Label(frame8, text='y =', font=('arial', 20, 'italic'), bg='powder Blue').grid(row=3, column=6)
        entry4 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        entry5 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        entry6 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        def calculate():
            a1 = eval(entry1.get())
            b1 = eval(entry2.get())
            c1 = eval(entry3.get())
            a2 = eval(entry4.get())
            b2 = eval(entry5.get())
            c2 = eval(entry6.get())
            D =a1*b2 -a2*b1
            D1 =c1*b2 - c2*b1
            D2 =a1*c2 - a2*c1
            try:
                output.configure(text = 'Solution: x= {:s}, y= {:s}'.format(functions.float_answer_analyzer(D1/D), functions.float_answer_analyzer(D2/D)))
            except:
                output.configure(text = 'Math error')
            
        calc_button = tkinter.Button(frame8, text='Cal', font = ('arial', 20, 'bold'), command = calculate)
        entry4.grid(row=3, column=3)
        entry5.grid(row=3, column=5)
        entry6.grid(row=3, column=7)
        entry1.grid(row=2, column=3)
        entry2.grid(row=2, column=5)
        entry3.grid(row=2, column=7)
        output = tkinter.Label(frame8, font = ('arial', 15, 'bold'))
        output.grid(row=4, column=0, columnspan=5)
        calc_button.grid(row=3, column=8)
        #===================================================3-Unknowns====================================================================
        f1 = tkinter.Frame(frame8,  width = 400, height = 2, bg = 'blue', relief = tkinter.SUNKEN)
        f1.grid(row=6, column=0, columnspan=400)
        labela =tkinter.Label(f1, text='Equations With Three Unknowns', font=('Verdana', 20, 'bold italic'), fg='green')
        labela.pack(side=tkinter.LEFT)
        labelb = tkinter.Label(frame8, text='Form: ax + by + cz = d', font=('Verdana', 16, 'bold italic'), fg='green')
        labelb.grid(row=8, column=0, columnspan=3)
        labelc = tkinter.Label(frame8, text='First Equation:', font=('Verdana', 20, 'bold italic'), fg='green')
        labelc.grid(row=10, column=0, columnspan=2)
        labeld = tkinter.Label(frame8, text='x +', font=('Verdana', 20, 'bold italic'), fg='green')
        labeld.grid(row=10, column=4)
        labele = tkinter.Label(frame8, text='y +', font=('Verdana', 20, 'bold italic'), fg='green')
        labele.grid(row=10, column=6)
        labelf = tkinter.Label(frame8, text='z =', font=('Verdana', 20, 'bold italic'), fg='green')
        labelf.grid(row=10, column=8)
        coeff1 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff2 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff3 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff4 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff1.grid(row=10, column=3)
        coeff2.grid(row=10, column=5)
        coeff3.grid(row=10, column=7)
        coeff4.grid(row=10, column=9)
        labelg = tkinter.Label(frame8, text='Second Equation:', font=('Verdana', 20, 'bold italic'), fg='green')
        labelg.grid(row=11, column=0, columnspan=2)
        labelh = tkinter.Label(frame8, text='x +', font=('Verdana', 20, 'bold italic'), fg='green')
        labelh.grid(row=11, column=4)
        labeli = tkinter.Label(frame8, text='y +', font=('Verdana', 20, 'bold italic'), fg='green')
        labeli.grid(row=11, column=6)
        labelj = tkinter.Label(frame8, text='z =', font=('Verdana', 20, 'bold italic'), fg='green')
        labelj.grid(row=11, column=8)
        coeff5 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff6 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff7 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff8 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff5.grid(row=11, column=3)
        coeff6.grid(row=11, column=5)
        coeff7.grid(row=11, column=7)
        coeff8.grid(row=11, column=9)
        labelk = tkinter.Label(frame8, text='Third Equation:', font=('Verdana', 20, 'bold italic'), fg='green')
        labelk.grid(row=12, column=0, columnspan=2)
        labell = tkinter.Label(frame8, text='x +', font=('Verdana', 20, 'bold italic'), fg='green')
        labell.grid(row=12, column=4)
        labelm = tkinter.Label(frame8, text='y +', font=('Verdana', 20, 'bold italic'), fg='green')
        labelm.grid(row=12, column=6)
        labeln = tkinter.Label(frame8, text='z =', font=('Verdana', 20, 'bold italic'), fg='green')
        labeln.grid(row=12, column=8)
        coeff9 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff10 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff11 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff12 =tkinter.Entry(frame8, font=('arial', 20, 'italic'), width=2, bg= 'powder Blue')
        coeff9.grid(row=12, column=3)
        coeff10.grid(row=12, column=5)
        coeff11.grid(row=12, column=7)
        coeff12.grid(row=12, column=9)
        def _det3_(a, b, c, e, f, g, i, j, k):
            return (a*f*k + b*i*g + c*e*j - a*j*g - b*e*k - c*i*f)
        def cubic_equation():
            a = eval(coeff1.get())
            b = eval(coeff2.get())
            c = eval(coeff3.get())
            d = eval(coeff4.get())
            e = eval(coeff5.get())
            f = eval(coeff6.get())
            g = eval(coeff7.get())
            h = eval(coeff8.get())
            i = eval(coeff9.get())
            j = eval(coeff10.get())
            k = eval(coeff11.get())
            l = eval(coeff12.get())
            D = _det3_(a, b, c, e, f, g, i, j, k)
            D1 = _det3_(d, b, c, h, f, g, l, j, k)
            D2 = _det3_(a, d, c, e, h, g, i, l, k)
            D3 = _det3_(a, b, d, e, f, h, i, j, l)
            try:
                output2.configure(text = 'The Solution Are: x= {:s}, y= {:s}, z= {:s}'.format(functions.float_answer_analyzer(D1/D), functions.float_answer_analyzer(D2/D), functions.float_answer_analyzer(D3/D)))
            except:
                output2.configure(text = 'Math error')
                              
    
        ok_button = tkinter.Button(frame8, text='Cal', font = ('arial', 20, 'bold'), command = cubic_equation)
        ok_button.grid(row=12, column=11)
        output2 = tkinter.Label(frame8, font = ('arial', 15, 'bold'))
        output2.grid(row=14, column=0, columnspan=8)
        #========================================================quadratic equations============================================================
        lab1 = tkinter.Label(frame9, text='Quadratic Equation:', font = ('arial', 20, 'bold'), fg = 'green').grid(row=0, column=0, columnspan=4)
        lab2 = tkinter.Label(frame9, text='Form: ax\u00b2 + bx + c =0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=1, column=0, columnspan=4)
        lab3 = tkinter.Label(frame9, text='x\u00b2 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=2, column=1)
        lab4 = tkinter.Label(frame9, text='x +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=2, column=3)
        lab7 = tkinter.Label(frame9, text='= 0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=2, column=5)
        ent1 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent2 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent3 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent1.grid(row=2, column=0)
        ent2.grid(row=2, column=2)
        ent3.grid(row=2, column=4)
        def _quadraticroot_(i, a, b, c):
            if i == 1:
                return ((-b+sqrt(b*b-4*a*c))/(2*a))
            else:
                return ((-b-sqrt(b*b-4*a*c))/(2*a))

        def calc3():
            a = eval(ent1.get())
            b = eval(ent2.get())
            c = eval(ent3.get())
            try:
                L = solve(a*x**2+b*x+c, x)
                flag = 0
                if len(L) == 1:
                    lab5.configure(text='The equation has a repeated root!')
                    a = str(L[0])
                    for i in a:
                        if i.isalpha():
                            L[0] = L[0].evalf()
                            flag = 1
                    if flag == 0:
                        lab6.configure(text='The repeated root is: {:}'.format(L[0]))
                    else:
                        lab6.configure(text='The repeated root is: {:s}'.format(functions.float_answer_analyzer(L[0])))
                elif len(L) != 1 and not functions.complex_checker(L[0]):
                    for i in L:
                        a = str(i)
                        for j in a:
                            if j.isalpha() and j != 'j':
                                L[0] = L[0].evalf(); L[1] = L[1].evalf()
                                flag = 1
                    lab5.configure(text='The equation has two distinct roots!')
                    if flag == 0:
                        lab6.configure(text='The roots are: {:} and {:}'.format(re(L[0]), re(L[1])))
                    else:
                        lab6.configure(text='The roots are: {:s} and {:s}'.format(functions.float_answer_analyzer(re(L[0])), functions.float_answer_analyzer(re(L[1]))))
                else:
                    for i in L:
                        a = str(i)
                        for j in a:
                            if j.isalpha() and j != 'j':
                                L[0] = L[0].evalf(); L[1] = L[1].evalf()
                                flag = 1
                    lab5.configure(text='The equation has complex roots!')
                    if flag == 0:
                        lab6.configure(text='The roots are: {:}+{:}j and  {:}-{:}j'.format(re(L[0]), im(L[0]), re(L[1]), im(L[1])))
                    else:
                        lab6.configure(text='The roots are: {:s}+{:s}j and  {:s}-{:s}j'.format(functions.float_answer_analyzer(re(L[0])), functions.float_answer_analyzer(Abs(im(L[0]))),
                                                                                                   functions.float_answer_analyzer(re(L[1])), functions.float_answer_analyzer(Abs(im(L[1])))))
            except:
                lab5.configure(text='Math error!')
            
        calc2_button = tkinter.Button(frame9, text = 'Cal', font = ('arial', 20, 'bold italic'), fg = 'green', command = calc3)
        calc2_button.grid(row=2, column=6)
        lab6 = tkinter.Label(frame9, font = ('arial', 15, 'bold italic'))
        lab6.grid(row=4, column=0, columnspan=15, rowspan=2)
        lab5 = tkinter.Label(frame9, font = ('arial', 15, 'italic'), fg = 'green')
        lab5.grid(row=3, column=0, columnspan=10)
        #===============================================================Cubic Equations==========================================================
        lab8 = tkinter.Label(frame9, text='Cubic Equation:', font = ('arial', 20, 'bold'), fg = 'green').grid(row=7, column=0, columnspan=4)
        lab9 = tkinter.Label(frame9, text='Form: ax\u00b3 + bx\u00b2 + cx + d = 0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=8, column=0, columnspan=20)
        lab10 = tkinter.Label(frame9, text='x\u00b3 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=9, column=1)
        lab11= tkinter.Label(frame9, text='x\u00b2 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=9, column=3)
        lab12= tkinter.Label(frame9, text='x +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=9, column=5)
        lab13= tkinter.Label(frame9, text='= 0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=9, column=7)
        ent4= tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent5= tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent6 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent7 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent4.grid(row=9, column=0)
        ent5.grid(row=9, column=2)
        ent6.grid(row=9, column=4)
        ent7.grid(row=9, column=6)
        def cubic():
            a = eval(ent4.get())
            b = eval(ent5.get())
            c = eval(ent6.get())
            d = eval(ent4.get())
            try:
                l = solve(a*x**3+b*x**2+c*x+d, x)
                L = []
                for i in l:
                    a = i.evalf()
                    L.append(a)
                ans = []
                for i in L:
                    b = str(i)
                    for j in b:
                        if j == 'I':
                            ans.append('{:s}{:1s}{:s}j'.format(functions.float_answer_analyzer(re(i)), '+' if im(i) > 0 else '-', functions.float_answer_analyzer(Abs(im(i)))))
                            break

                    else:
                        ans.append('{:s}'.format(functions.float_answer_analyzer(i)))
                lab14.configure(text='The roots are: {:s}, {:s}\n and {:s}'.format(ans[0], ans[1], ans[2]))
            except:
                lab14.configure(text='Math error!')

        calc3_button = tkinter.Button(frame9, text = 'Cal', font = ('arial', 15, 'bold italic'), fg = 'green', command = cubic)
        calc3_button.grid(row=9, column=9)
        lab14 = tkinter.Label(frame9, font = ('arial', 15, 'bold italic'))
        lab14.grid(row=10, column=0, columnspan=15)
########################################################Quatic-Equation################################################################################
        lab114 = tkinter.Label(frame9, text='Quatic-Equation:', font = ('arial', 20, 'bold'), fg = 'green').grid(row=13, column=0, columnspan=4)
        lab115 = tkinter.Label(frame9, text='Form: ax\u2074 + bx\u00b3 + cx\u00b2 + dx + e = 0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=14, column=0, columnspan=20)
        lab116 = tkinter.Label(frame9, text='x\u2074 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=15, column=1)
        lab117= tkinter.Label(frame9, text='x\u00b3 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=15, column=3)
        lab118= tkinter.Label(frame9, text='x\u00b2 +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=15, column=5)
        lab119= tkinter.Label(frame9, text='x +', font = ('arial', 20, 'bold'), fg = 'green').grid(row=15, column=7)
        labl20= tkinter.Label(frame9, text='= 0', font = ('arial', 20, 'bold'), fg = 'green').grid(row=15, column=9)
        ent8= tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent9= tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent10 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent11 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent12 = tkinter.Entry(frame9, font = ('arial', 20, 'bold'), width=2, fg = 'green')
        ent8.grid(row=15, column=0)
        ent9.grid(row=15, column=2)
        ent10.grid(row=15, column=4)
        ent11.grid(row=15, column=6)
        ent12.grid(row=15, column=8)
        def quatic_equation():
            a = eval(ent8.get())
            b = eval(ent9.get())
            c = eval(ent10.get())
            d = eval(ent11.get())
            e = eval(ent12.get())
            try:
                l = solve(a*x**4+b*x**3+c*x**2+d*x+e, x)
                L = []
                for i in l:
                    a = i.evalf()
                    L.append(a)
                ans = []
                for i in L:
                    b = str(i)
                    for j in b:
                        if j == 'I':
                            ans.append('{:s}{:1s}{:s}j'.format(functions.float_answer_analyzer(re(i)), '+' if im(i) > 0 else '-', functions.float_answer_analyzer(Abs(im(i)))))
                            break

                    else:
                        ans.append('{:s}'.format(functions.float_answer_analyzer(i)))
                lab15.configure(text='The roots are: {:s}, {:s},\n {:s} and {:s}'.format(ans[0], ans[1], ans[2], ans[3]))
            except:
                lab15.configure(text='Math error!')
        quatic_button = tkinter.Button(frame9, text = 'Cal', font = ('arial', 15, 'bold italic'), fg = 'green', command = quatic_equation)
        quatic_button.grid(row=15, column=10)
        lab15 = tkinter.Label(frame9, font = ('arial', 15, 'bold italic'))
        lab15.grid(row=16, column=0, columnspan=20)


class functions:
    '''
        This class simply contains static methods.
    '''

    @staticmethod
    def restart_program():
        import sys
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)

   
    @staticmethod
    def Webpage():
        import webbrowser as wb
        wb.open_new_tab('http://www.tipan-coders.simplesite.com')

    @staticmethod
    def tipa_parse_str(a):
        """ This function parses a text input in such a way that users can input mathematical expressions in a more friendly way
            it takes on only one argument which is a string, and returns a string as well.
            """
        a=list(a)
        for i in range(len(a)-1):
            if a[i].isdigit() and a[i+1].isalpha() and a[i+1] != 'j':
                a[i+1]='*'+a[i+1]
            if a[i].isdigit() and a[i+1]=='x' :
                a[i+1]='*'+a[i+1]
            if a[i] == 'x' and a[i+1].isalpha() and a[i+1] != 'p':
                a[i+1]='*'+a[i+1]
            if a[i]==')' and a[i+1].isalpha():
                a[i+1]='*'+a[i+1]
        a=''.join(a)
        return a

    @staticmethod
    def simpsons_rule(f, a, b):
        """ This performs definite integral by the method of approximation based on simpson's rule, it takes on three arguments, f, a and b
            f: is the function to be operated upon which is normally in string form
            a: lower limit of integration
            c: upper limit of integration
            It returns a floating point value"""
        n=100; h = (b-a)/n
        x1 = [(a + i*h) for i in range(n+1)]
        f = parse_expr(f)
        y = [f.subs(x,t).evalf() for t in x1]
        E = [y[t] for t in range(len(y)) if (t!=0 and t%2==0 and t!=n) ]
        R = [y[t] for t in range(len(y)) if (t!=0 and t%2!=0 and t!=n) ]
        sum1 = y[0]+y[n]
        sum2 = sum(E)
        sum3 = sum(R)
        A = h*(sum1 + 2*sum2 + 4*sum3)/3
        return A

    @staticmethod
    def graph_plot(f, a, b, c=100):
        from matplotlib.pyplot import plot, show, legend, xlabel, ylabel
        import numpy as np
        """ It plots functions
            It takes on four arguments that is f, a, b and c:
            f: function to be plotted in string format only.
            a: the least value of the independent variable.
            b: The greatest value of the independent variable.
            c: the smoothness of the curve low values gives only point plots, while higher values gives a continous smooth plot
            """
        x_axis=[]; y_axis=[]
        hor = np.linspace(a,b,c)
        hor = hor.tolist()
        x_axis = [0 for i in range(len(hor))]
        try:
            L = f.split(',')
            F = []
            for function in L:
                vert = parse_expr(function)
                vert = [vert.subs(x, i).evalf() for i in hor]
                vert.append(function)
                F.append(vert)
            for t in F:
                function = functions.math_display(t[-1])
                del t[-1]
                vert = np.array(t)
                hor = np.array(hor)
                plot(hor,vert, label=('$'+function+'$'))
            y_axis = [0 for i in range(len(vert))]
            x_axis = np.array(x_axis)
            y_axis = np.array(y_axis)
            plot(hor, x_axis, 'r--', linewidth=0.5)
            plot(y_axis, vert, 'r--', linewidth=0.5)
            legend()
            xlabel('independent-var')
            ylabel('dependent-var')
            show()
            
        except:
            vert = parse_expr(f)
            vert = [vert.subs(x, i).evalf() for i in hor]
            y_axis = [0 for i in range(len(vert))]
            vert = np.array(vert)
            hor = np.array(hor)
            x_axis = np.array(x_axis)
            y_axis = np.array(y_axis)
            f = functions.math_display(f)
            plot(hor,vert, label=('$'+f+'$'))
            plot(hor, x_axis, 'r--', linewidth=0.5)
            plot(y_axis, vert, 'r--', linewidth=0.5)
            legend()
            xlabel('independent-variable')
            ylabel('dependent-variable')
            show()

            
    @staticmethod
    def math_display(a):
        """ This function modifies a string so that it is output in more mathematical format,
        it takes on a single argument in string format and returns a string
        For Example:
        a = '3*x**2*sin(x**3)'
        b = math_display(a)
        b
        '3x\u00b2sin(x\u00b3)'
        """
        a = list(a)
        def superscript(t):
            a =  {0:'\u2070', 1:'\u00B9', 2:'\u00b2', 3:'\u00b3', 4:'\u2074', 5:'\u2075', 6:'\u2076', 7:'\u2077', 8:'\u2078', 9:'\u2079'}
            if t.isdigit():
                return a[int(t)]
        
        for i in range(len(a)-3):
            if a[i]==a[i+1]=='*' and a[i+2].isdigit() and a[i+3].isdigit():
                a[i] = superscript(a[i+2])+superscript(a[i+3]); a[i+1]=a[i+2]=a[i+3]=''
            elif a[i]==a[i+1]=='*' and a[i+2].isdigit() and (not a[i+3].isdigit()):
                a[i] = superscript(a[i+2]); a[i+1]=a[i+2]=''
            if a[i]=='*' and a[i+1]!='*':
                a[i]=''
            if a[i]=='l' and a[i+1]=='o' and a[i+2]=='g':
                a[i]='ln'; a[i+1]=a[i+2]=''
            if a[i]=='s' and a[i+1]=='q' and a[i+2]=='r' and a[i+3]=='t':
                a[i]='√'; a[i+1]=a[i+2]=a[i+3]=''
        a = ''.join(a)
        return a

    @staticmethod
    def decimal_to_fraction(y):
        try:
            a = y.numerator
            number = float(y)
        except:
            number = float(y)
            number = number.as_integer_ratio()
            number = Fraction(number[0]/number[1]).limit_denominator()
        return str(number)

    @staticmethod
    def apostrophe(x):
        try:
            a = x.count('\u2032')
            b = x.count('\u2033')
            c = x.count('\u2034')
            if a == b == c == 0:
                y = '\u2032'
            elif a == 1 and b == c == 0:
                y = '\u2033'
            elif a == b == 1 and c == 0:
                y = '\u2034'
            return y
        except:
            functions.speaking('Please you can not alter the standard format, the last value is microseconds.')
            return ''
        
    @staticmethod
    def TaylorSeries(f, b, a = 0):
        ans = functions.Maclaurins_series(f, b)
        ans = functions.math_display(str(ans))
        return ans
    
    @staticmethod
    def complex_checker(n):
        try:
            a = re(n)
            b = im(n)
            if b != 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def serialisation():
        filename = "C:/Tipan-App/data/bin.txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        try:
            with open(filename, 'r') as f:
                activation_detail = [i.strip() for i in f]
                a_detail = activation_detail[2].split(' ')
                validation_key = activation_detail[3].split(' ')
                key = a_detail[1]
                key = key[4:-4]
                v_key = validation_key[1].upper()
                v_key = v_key[-1] + v_key[1:-1] + v_key[0]
            if len(key) == 16 and key[-1].isdigit() and key == v_key and key != 'Free':
                return 1
            else:
                return 2
        except:
            return 3

    @staticmethod
    def speak(a):
        import pygame
        pygame.mixer.init(25000,-16,2,2048)
        sound = pygame.mixer.Sound(a)
        sound.play()

    @staticmethod
    def float_analyzer(a):
        a = float(a)
        if a.is_integer():
            a = int(a)
            return str(a)
        else:
            number = a.as_integer_ratio()
            den = str(number[1])
            if len(den) <= 3:
                number = Fraction(number[0]/number[1]).limit_denominator()
                return str(number)
            else:
                return str(a)

            
    @staticmethod
    def float_answer_analyzer(a):
        a = float(a)
        if a.is_integer():
            a = int(a)
            return str(a)
        else:
            number = a.as_integer_ratio()
            den = str(number[1])
            if len(den) <= 3:
                number = Fraction(number[0]/number[1]).limit_denominator()
                return str(number)
            else:
                return '{:.4f}'.format(a)

    @staticmethod
    def is_numeric(a):
        try:
            float(eval(a))
            return True
        except:
            return False

        
    @staticmethod
    def Maclaurins_series(f, b, a = 0):
        f = functions.tipa_parse_str(f)
        f = parse_expr(f)
        L = []
        for i in range(a, b+1):
            if i == 0:
                try:
                    ans = f.subs(x, 0).evalf()
                    ans = functions.decimal_to_fraction(ans)
                except:
                    ans = ''
            else:
                try:
                    c = sp.diff(f, x, i, evaluate = False)
                    c = c.subs(x, 0).evalf()
                    c = c / fact(i)
                    c = functions.decimal_to_fraction(c)
                    c = '' if c == '1' else '('+c+')'
                    x_value = 'x' if i == 1 else 'x**{:d}'.format(i)
                    ans = c + x_value
                except:
                    ans = ''
            L.append(ans)
        ans = functions.math_display('+'.join(L))
        return ans

    @staticmethod
    def Fourier_Transform(f, a, b):
        f = f + '*exp(-s*x)'
        f = functions.tipa_parse_str(f)
        f = parse_expr(f)
        ans = simplify(integrate(f, (x, a, b), conds='none'))
        return str(ans)

    @staticmethod
    def Laplace_Transform(f, a):
        f = '(' + f + ')'+ '*exp(-s*t)'
        f = functions.tipa_parse_str(f)
        f = parse_expr(f)
        ans = simplify(integrate(f, (t, 0, a), conds='none'))
        return str(ans)
    @staticmethod
    def Inverse_Laplace_Transform(f):
        ans = inverse_laplace_transform(f, s, t)
        return str(ans)




def Sin(angle):
    if angle==30:
        return 0.5
    elif angle==90:
        return 1
    elif angle==180:
        return 0
    elif angle==0:
        return 0
    elif angle==360:
        return 0
    else:
        x = radians(angle)
        total = sin(x)
        return total

def Cos(angle):
    if angle==60:
        return 0.5
    elif angle==90:
        return 0
    elif angle==180:
        return -1
    elif angle==0:
        return 1
    elif angle==360:
        return 1
    elif angle==270:
        return 0
    else:
        x = radians(angle)
        total = cos(x)
        return total

def Tan(angle):
    if angle==45:
        return 1
    elif angle==180:
        return 0
    elif angle==0:
        return 0
    elif angle==360:
        return 0
    else:
        x = radians(angle)
        return tan(x) 

def aSin(x):
    if x==0.5:
        return 30
    elif x==1:
        return 90
    elif x == 2/sqrt(3):
        return 60
    elif x == 1/sqrt(2):
        return 45
    
    else:
        ans = asin(x)
        angle = degrees(ans)
        return angle

def aCos(x):
    if x==0.5:
        return 60
    elif x==1:
        return 0
    elif x == 2/sqrt(3):
        return 30
    elif x == 1/sqrt(2):
        return 45
    else:
        total = acos(x)
        angle = degrees(total)
        return angle

def aTan(x):
    if x==1:
        return 45
    elif x == 1/sqrt(3):
        return 30
    elif x == sqrt(3):
        return 60
    else:
        total = atan(x)
        angle = degrees(total)
        return angle
  
def fact(n):
    """ Takes one argument n which is an integer and returns the factorial of that integer value """
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def perm(n, r):
    """ Evaluates the permutation of integers n and r
            n should be greater than r"""
    return (fact(n)/fact(n-r))

def comb(n, r):
    """ Evaluates the Combination of integers n and r  """
    return (fact(n)/(fact(n-r) * fact(r)))

    
def p(x,n):
    """ This function evaluates a complex number raised to the power n
            it takes on two arguments x and n.
            x: This is normally a complex number e.g. x = 2+3j
            n: is a numerical value which can be an integer or a float
            It returns a complex number"""
    angle = atan(x.imag/x.real)
    mod=abs(x)
    angle=n*angle
    mod =mod**n
    r = functions.float_analyzer(mod * cos(angle))
    i = functions.float_analyzer(mod * sin(angle))
    return '{:.2f}{:s}{:.2f}j'.format(r, '+' if i>0 else '-', abs(i))

    
    


        
    
    
    
        
    
    


    



