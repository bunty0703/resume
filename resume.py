def generate_resume_template():
    print("Welcome to Resume Template Generator!")
    print("Please provide the following details:")
    
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    objective = input("Objective: ")
    education = input("Education: ")
    experience = input("Experience: ")
    skills = input("Skills: ")
    
    template = f"""
    -----------------------
    Name: {name}
    Email: {email}
    Phone: {phone}
    Address: {address}
    
    Objective:
    {objective}
    
    Education:
    {education}
    
    Experience:
    {experience}
    
    Skills:
    {skills}
    -----------------------
    """
    
    return template

if __name__ == "__main__":
    resume_template = generate_resume_template()
    print("Generated Resume Template:")
    print(resume_template)
