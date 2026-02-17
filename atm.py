# ATM TRANSACTION SYSTEM

print("🏦  ATM MACHINE")
print("=" * 50)

balance = 5000
users = 1
pin = 1234

while users <= 2:  # OUTER WHILE LOOP - Users
    print(f"\n👤 USER {users}")
    print("-" * 30)
    
    user_pin = int(input("Enter PIN: "))
    
    if user_pin == pin:
        attempts = 0
        while attempts < 3:  # NESTED WHILE LOOP - Menu display
            print(f"\n--- Main Menu (Attempt {attempts + 1}) ---")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Mini Statement")
            print("")
            print("5. Exit")
            
            choice = int(input("Choose option: "))
            
            # NESTED IF-ELIF
            if choice == 1:
                print(f"💰 Balance: Rs.{balance}")
                
            elif choice == 2:
                amount = int(input("Amount to withdraw: Rs."))
                
                # NESTED IF IN WITHDRAW
                if amount <= balance:
                    if amount <= 5000:
                        balance -= amount
                        print(f"✅ Withdrawn: Rs.{amount}")
                        print(f"💰 New Balance: Rs.{balance}")
                    else:
                        print("❌ Maximum withdrawal Rs.5000!")
                else:
                    print("❌ Insufficient balance!")
                    
            elif choice == 3:
                amount = int(input("Amount to deposit: Rs."))
                
                # NESTED IF IN DEPOSIT
                if amount > 0:
                    if amount <= 50000:
                        balance += amount
                        print(f"✅ Deposited: Rs.{amount}")
                        print(f"💰 New Balance: Rs.{balance}")
                    else:
                        print("❌ Maximum deposit Rs.50000!")
                else:
                    print("❌ Invalid amount!")
                    
            elif choice == 4:
                # NESTED FOR LOOP - Mini statement
                print("📜 Mini Statement:")
                transactions = ["Salary", "Groceries", "Bills", "Savings"]
                amounts = [5000, -500, -1000, 2000]
                
                for i in range(len(transactions)):  # NESTED FOR
                    print(f"   {transactions[i]}: Rs.{amounts[i]}")
                    
            elif choice == 5:
                print("👋 Thank you! Visit again!")
                break
                
            else:
                print("❌ Invalid option!")
            
            attempts += 1
            if attempts >= 3:
                print("⚠️ Maximum attempts reached!")
                
    else:
        print("❌ Wrong PIN!")
    
    users += 1

print("\n" + "=" * 50)
print("🏦 ATM Shutting Down...")