phonebook = {"John" : 938477566, "Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Delete John
del phonebook["John"]
# Another way to delete 
# phonebook.pop("John")
          
print(phonebook)
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  
