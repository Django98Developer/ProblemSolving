
name = input("What's your name ?").strip().capitalize()
email = input("Enter your Email : ").strip()
userName = email[:email.index("@")]
domain = email[email.index("@")+1 :]

print(f"Hello {name}, your userName is {userName} and your domain is {domain}")
