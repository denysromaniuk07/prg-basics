###2.2

# emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
# unique_emails = set(emails)  # Removes duplicates
# print(unique_emails)

###2.3

# all_students = {"Alice", "John", "Sara", "Bob"}
# attended_students = {"Alice", "Bob"}

# absent_students = all_students - attended_students # Difference
# print(absent_students)

###2.4

# emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
# spam_list = {"spam1@example.com", "spam2@example.com"}

# spam_emails = emails_received & spam_list # Intersection
# print("Spam emails:", spam_emails)

###2.5

# contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
# contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# merged_contacts = contacts_A | contacts_B  # Union
# print("Merged contacts:", merged_contacts)

###2.6

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = required_permissions.issubset(user_permissions)   # subset
print(has_permissions)  # Will return False because "execute" is missing.

