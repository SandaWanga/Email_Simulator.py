# Email_Simulator.py

### --- OOP Email Simulator --- ###

# --- Email Class --- #

 # A constructor that takes in arguments
     
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Initialise class variables for emails. 
     def __init__(self,email_address,subject_line,email_contents,has_been_read=False, is_spam=False):
        
    # Initialise instance variables for emails.
      self.email_address = email_address
      self.subject_line = subject_line
      self.email_contents = email_contents
      self.has_been_read = has_been_read
      self.is_spam = is_spam
      
      #def __str__(self):
       # return f'{self.email_address}'
     pass
    # Method to change 'has_been_read' emails from False to True.

 
    
     def mark_as_read(self):
         if self.has_been_read == False:
             self.has_been_read = True
  

    # Method to change 'is_spam' emails from False to True.
   
      
     def mark_as_spam(self):
         if self.is_spam == False:
             self.is_spam= True
  


# --- Lists --- #
# Initialise empty lists to store the email objects.
inbox = []
outbox = []

# --- Functions --- #
# Create and build out the required functions for your program.
def populate_inbox():

# Create 3 sample emails and add it to the inbox list.

 inbox.append(Email('jchawa@test.local', 'first email', 'this is my first email'))
 inbox.append(Email('wanga@test.local', 'second email', 'this is my second email'))
 inbox.append(Email('musa@test.local', 'third email', 'this is my third email'))
   
# Create a function which prints the email’s subject_line, along with a corresponding number.

def list_emails():
 for index, email in enumerate(inbox):
        print(index, email.subject_line)

def send_email():
      email_address = []
      subject_line = []
      email_contents = []
         # Create an email to 'send'/add to the outbox list.
      new_email = Email(email_address, subject_line, email_contents)
      outbox.append(new_email)
      print("Email sent to Outbox.")

      recipient = input("Recipient email : ")
      subject = input("Email subject: ")
      contents = input("Email contents: ")
      email = Email(recipient, subject, contents)
      outbox.append(email)
      print("Email sent!")
 

#email_address,subject_line,email_contents
def read_email(index):
   email = inbox[index]
   print("From: {}\nSubject: {}\n{}".format(email.email_address, email.subject_line, email.email_contents))
   email.mark_as_read()

print("Unread emails:")
for i, email in enumerate(inbox):
    if not email.has_been_read:
        print(i,email.subject_line)


#     # Create a function which displays a selected email and then sets its has_been_read instance variable to True.

def mark_spam(index):
    email = inbox[index]
    email.mark_as_spam()
    print("Email marked as spam.")
    
#     # Create a function which sets the selected email's mark_as_spam instance variable to True.


def delete_email(self):
  
    
#     # Create a function which deletes an email from the inbox.
 if len(inbox) > 0:
    print("Email deleted.")

# # --- Email Program --- #

# # Populate the inbox with 3 sample emails for use in your program
populate_inbox()

# # Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. Mark an email as spam
    3. Delete an email
    4. View unread emails
    5. View spam emails
    6. Send an email
    7. Quit application

    Enter selection: '''))
       
#     # Read an email
    if user_choice == 1:
        # add logic here
         list_emails()
         index = int(input("Enter the index of the email you want to read: "))
         read_email(index)

        
    # Mark an email as spam
    elif user_choice == 2:
        # add logic here
         list_emails()
         index = int(input("Enter the index of the email you want to mark as spam: "))
         mark_spam(index)

    # Delete an email
    elif user_choice == 3:

        # add logic here
         list_emails()
         index = int(input("Enter the index of the email you want to delete: "))
         delete_email(index)
    
    # View unread emails
    elif user_choice == 4:
        # add logic here
    
         print("Unread emails:")
         for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(i,email.subject_line)
               
            
    # View spam emails
    elif user_choice == 5:
        # add logic here
         print("Spam emails:")
         for i, email in enumerate(inbox):
            if email.is_spam:
                print(i,email.subject_line)
               
    
    # Send an email
    elif user_choice == 6:
         send_email()
        # add logic here
       
        

    # Quit appplication
    elif user_choice == 7:
        # add logic here
        print("Exiting email simulator...")
        print("Goodbye!")
       


    else:
        print("Oops - incorrect input.")


    



