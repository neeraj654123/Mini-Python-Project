balance =0.0
kyc_documents={}
def check_balance():
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f"Your current balance is {balance}")
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

def deposit(amount):
    global balance
    if amount<0:
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print("Enter Valid amount")
    else:
        balance+=amount
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print("Amount Deposited")
    
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)
    
    
def check_kyc():
    if len(kyc_documents)==0:
                print("KYC not done")
    else:
        for doc in kyc_documents:
            print(f"{doc}:{kyc_documents[doc]}")

def withdraw(drawed):
    global balance
    if drawed<0:
        print("Enter Valid amount")
    elif drawed>balance:
        print(f"Amount to be withdraw mus be less than account balance: {balance}")
    else:
        balance-=drawed
        print("Amount Withdrawed. Please collect it from the box")
    
if __name__=="__main__":
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print("Welcome to ABC Bank")
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    while True:
        print("1. Check balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice =input("Enter your choice (1-6): ")
        if choice =='1':
            check_balance()
        elif choice=='2':
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            amount=int(input("Enter amount you want to deposit:"))
            deposit(amount)
        elif choice=='3':
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            drawed=int(input("Enter amount you want to withdraw:"))
            withdraw(drawed)
        elif choice=='4':
            check_kyc()
        elif choice=='5':
            kyc_docs={}
            n_documents=int(input("Enter no. of documents you want to add: "))
            for i in range(n_documents):
                key =input("Enter the document type:")
                Value=input("Enter the document no. :")
                kyc_docs[key]=Value
            update_kyc(kyc_docs)
            print("KYC updated")
        elif choice=='6':
            break
        else:
            print("please Enter Valid input")
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print("Thankyou for banking with us")
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')