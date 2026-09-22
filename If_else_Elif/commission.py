S= input ('Enter your monthly sales:')
S= float (S)

T=S*0.15
T2= S*0.05

if S>40000:
    print('Your commision is:',T)
elif S<40000:
    print('Your commision is:',T2)