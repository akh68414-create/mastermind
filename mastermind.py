import random

allowed_val = [1 ,2 ,3 ,4 ,5 ,6]

def random_pass ():
    """  ساخت رمز 4 رقمی با ارقام 1تا 6 و بدون تکرار ارقام"""

    
    password = []

    for i in range(4):

        a = random.choice(allowed_val)
        password.append(a)
        allowed_val.remove(a)       # برای تکرار نشدن ارقام

    return password



def user_input ():
    """ گرفتن حدس کاربر در مقادیر مجاز و بدون تکرار 
        در نهایت ورودی درست از کاربر گرفته و برمیگرداند"""

    allowed_val_ch = ['1' ,'2' ,'3' ,'4' ,'5' ,'6']

    
    while True :

        
        ch_counter = []
        user_pass = input("\nenter your guess (digits 1_6)")
        
        if ( len(user_pass) == 4 ):
            
            for ch in user_pass :       #پیمایش روی مقادیر ورودی کاربر

                if ch in allowed_val_ch :       #چک مجاز بودن مقادیر
                    ch_counter.append(ch)

            flag = False

            for i in ch_counter:        #تکراری نبودن مقادیر 

                counter = ch_counter.count(i)
                

                if counter > 1 :
                    flag = True

            if ( len(ch_counter)== 4 and flag == False):      #ساخت ورودی معتبر از ورودی کاربر

                user_guess = []

                for item in ch_counter :

                    int_item = int (item)
                    user_guess.append(int_item)
                
                return  user_guess

            
        print ("wrong val . guess must int , 1-6   , gheire tekrary")


                 

key = random_pass ()
chances = 10


def comparison ( user , key):
    """مقایسه کاربر و رمز بازی را انجام داده 
        و تعداد ارقام درست در جای درسن و ارقام درست در جای نادرست را برمیگرداند """

    right_place_val = 0
    right_val_wrong_place = 0
 
    for i in range (4):

        if user[i] == key[i] :
            right_place_val +=1

        
        elif user[i] in key :   
            right_val_wrong_place +=1

     
    return right_place_val , right_val_wrong_place



def information ():
    """ تابعی برای نمایش اظلاعات کاربر بدون  برگرداندن """

    print (" game name    :       Bazi fekr bekr")
    print (" lesson name  :       advanced programming")
    print (" programmer   :       Ali Khodabande")
    print (" student ID   :       404130633\n")



option = input(" do you want read information about GAME and PROGRAMMER ? (Y to yes/N to no)\n")
if(option.upper() == 'Y'):
    information()

while chances > 0:      # تکرار حلقه تا پایان شانس کاربر



    user = user_input()
    chances -=1

    
    right_place_val , right_val_wrong_place = comparison ( user , key)

    print ("\nright number in right place :",right_place_val)
    print ("right number in wrong place :",right_val_wrong_place)

    print ("\nyour chancess : ___" , chances , "___")

    tries = 10 - chances
    
    if( right_place_val == 4):
        print ("YOU WON .      tries : " ,  tries)      #نشان دادن تعداد تلاش های کاربر

        break

else:
    result =""

    for item in key:
        result += str(item)


    print("you lose bro")    
    print("the secret key = ",  result)


