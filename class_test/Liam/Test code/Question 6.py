C= input ('Enter eather the weather, day, or date: ')

if C== ('Weather') or C==('weather'):
    A= input ('Is it a sunny or rainy day: ')
    if A== ('Sunny') or A==('sunny'):
        print ('It is goint to be a happy day.')
    else:
        print ('It is going to be a sad day.')
        
elif C== ('Day') or C==('day'):
    B= input ('What day of the week is it: ')
    if B==('Sunday') or B== ('sunday') or B==('Saturday') or B==('saturday'):
            print ('It is going to be a happy day.')
    else:
            print ('It is going to be a sad day.')
            
elif C== ('Date') or C==('date'):
    D= int (input ('What is the date: '))
    if (D%2==0):
        print ('It is going to be a happy day.')
    else:
        print ('It is going to be a sad day.')
            
 
