#WITI Academy is proposing a Sacco to help students save their money
# Design a platform that will do the following.
#  1.Deposit money
#  2.Withdraw money
#  3.Check balance 
#  Ensure if the student selcts 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the student selects 3, the account balance should be displayed.

#SOLUTION
def sacco_transaction():
     account_balance=0
     run=1
     while run==1:
          
      print("\n Welcome to WITIAcademy Sacco")
      print("1.Deposit money")
      print("2.Withdraw money")
      print("3.Check balance")

      student_choice=int(input("Enter your selection (1,2 or 3) :"))
      if student_choice==1 :
           print("\n...processing a deposit transaction")
           deposit_amount=int(input("Enter amount to be deposited :"))
           if deposit_amount < 1000:
             print('\n minimum deposit is 1000')
           else:
            account_balance+=deposit_amount
            print(f"Dear student, you have deposited {deposit_amount:,} and your new account balance is {account_balance:,}")

      elif student_choice ==2:
              print("\n...processing a Withdraw transaction")
              withdraw_amount=int(input("Enter amount to be withdrawn :"))
              if account_balance == 0:
                  print("Your account balance is 0")
              elif withdraw_amount < 500:      
               print("\n Minimum withdraw amount is 500")
              elif withdraw_amount > account_balance:
                         print("Dear student,you have insufficient funds.")
              else:
                  account_balance-= withdraw_amount
                  print(f"Dear student, you have withdrawn {withdraw_amount:,} and your new account balance is {account_balance:,}")
                 
      elif  student_choice== 3:
       print(f'your account balance is {account_balance}')
     else:
      print("You entered a wrong choice!! please select 1,2 or 3\n")
      run = int(input('Enter 1 to continue or any number to exist'))
      if run !=1:
         print("Thanks for joining Sacco")
         
         

sacco_transaction()