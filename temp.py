import re

def extract_info(text):
    """Extracts information from the given text and returns it as a dictionary."""
    info = {}

    # Extract name
    name_match = re.search(r"^(.*?)\n", text)
    if name_match:
        info["name"] = name_match.group(1).strip()

    # Extract contact information
    info["phone"] = re.search(r"\+91(\d+)", text).group(1)
    info["email"] = re.search(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text).group(1)

    # Extract education
    education_match = re.search(r"EDUCATION\n(.*?)\nSKILLS", text, re.DOTALL)
    if education_match:
        education = education_match.group(1).strip()
        info["education"] = education.splitlines()

    # Extract skills
    skills_match = re.search(r"SKILLS\n(.*?)\nPROJECTS", text, re.DOTALL)
    if skills_match:
        skills = skills_match.group(1).strip()
        info["skills"] = skills.splitlines()

    # Extract projects
    projects_match = re.search(r"PROJECTS\n(.*?)\nLANGUAGES", text, re.DOTALL)
    if projects_match:
        projects = projects_match.group(1).strip()
        info["projects"] = projects.splitlines()

    # Extract languages
    languages_match = re.search(r"LANGUAGES\n(.*?)\nACHIEVEMENT", text, re.DOTALL)
    if languages_match:
        languages = languages_match.group(1).strip()
        info["languages"] = languages.splitlines()

    # Extract achievements
    achievements_match = re.search(r"ACHIEVEMENT\n(.*?)\nEXTRA-CURRICULAR ACTIVITIES", text, re.DOTALL)
    if achievements_match:
        achievements = achievements_match.group(1).strip()
        info["achievements"] = achievements.splitlines()

    # Extract extra-curricular activities
    extracurricular_match = re.search(r"EXTRA-CURRICULAR ACTIVITIES\n(.*)", text, re.DOTALL)
    if extracurricular_match:
        extracurricular = extracurricular_match.group(1).strip()
        info["extracurricular"] = extracurricular.splitlines()

    return info

# Example usage
resume_text = """
ANKIT SHARMA
+918115080798 ⋄Gorakhpur, Uttar Pradesh India
ankit972125@gmail.com ⋄linkedin ⋄Portfolio
EDUCATION
Bachelor of Technology , 2022 - 2026
•Studying Information Technology at Rajkiya Engineering College, Azamgarh, Uttar Pradesh.
•Relevant coursework : Operating system, DSA, OOPs, DBMS & Computer Networking.
SKILLS
Programming Languages : C&C++, Python
Front-end Development: HTML, CSS, JavaScript, Tailwind CSS, Bootstrap
Back-end Development: Django, SQL, Linux, MongoDB, REST API
Tools: Postman, Git & GitHub, Visual Studio Code, Docker, Jupyter
PROJECTS
Social-Media
•Developed a responsive social media platform using Django, ensuring optimal performance across devices.
•Apply modern design principles and responsive layouts, ensuring seamless user experience across various devices
and screen sizes.
•Integrated key features such as follow/unfollow, like/dislike, viewing and editing profile information, and contact
details for a dynamic user experience. Source code,Deploy
E-commerce Application
•Developed a comprehensive E-commerce application using Django, providing features for product browsing,
shopping cart management, and secure checkout.
•Implemented an intuitive user interface to enhance the shopping experience, focusing on ease of navigation and
seamless interactions.
•Integrated secure authentication mechanisms using Django’s authentication features, ensuring protected access
to user accounts and order history. Source code, Deploy
Heart Disease Prediction
•Trained predictive models using a dataset of 1016 patient records for heart disease prediction.
•Conducted feature selection and engineering to enhance model performance and reduce complexity.
•Integrated the trained model into a Django-based web application for user-friendly heart disease prediction.
Source Code, Deploy.
Blog
•Developed a dynamic blog application using Django, allowing users to create, edit, and publish blog posts.
•Implemented modern design principles and responsive layouts for a seamless reading experience on various
devices.
•Optimized website performance through efficient coding practices, enhancing loading speed and overall accessi-
bility. Source code , Deploy.
LANGUAGES
•Hindi: Proficient
•English: Intermediate
ACHIEVEMENT
•Solve 800+ problems over Geeks for Geeks, Leetcode, Hackerrank.
•5 star in C & C++ on Hackerank.
•3 star in Python on Hackerank.
EXTRA-CURRICULAR ACTIVITIES
•Co-Founder and Vice President, Optimix Club
•Member of E-Cell
•Volunteer, Hamari Pahchan NGO
"""

extracted_info = extract_info(resume_text)
print(extracted_info)
{'name': 'ANKIT SHARMA', 'phone': '8115080798', 'email': 'ankit972125@gmail.com', 'education': ['Bachelor of Technology , 2022 - 2026', '•Studying Information Technology at Rajkiya Engineering College, Azamgarh, Uttar Pradesh.', '•Relevant coursework : Operating system, DSA, OOPs, DBMS & Computer Networking.'], 'skills': ['Programming Languages : C&C++, Python', 'Front-end Development: HTML, CSS, JavaScript, Tailwind CSS, Bootstrap', 'Back-end Development: Django, SQL, Linux, MongoDB, REST API', 'Tools: Postman, Git & GitHub, Visual Studio Code, Docker, Jupyter'], 'projects': ['Social-Media', '•Developed a responsive social media platform using Django, ensuring optimal performance across devices.', '•Apply modern design principles and responsive layouts, ensuring seamless user experience across various devices\nand screen sizes.', '•Integrated key features such as follow/unfollow, like/dislike, viewing and editing profile information, and contact\ndetails for a dynamic user experience. Source code,Deploy', 'E-commerce Application', '•Developed a comprehensive E-commerce application using Django, providing features for product browsing,\nshopping cart management, and secure checkout.', '•Implemented an intuitive user interface to enhance the shopping experience, focusing on ease of navigation and\nseamless interactions.', '•Integrated secure authentication mechanisms using Django’s authentication features, ensuring protected access\nto user accounts and order history. Source code, Deploy', 'Heart Disease Prediction', '•Trained predictive models using a dataset of 1016 patient records for heart disease prediction.', '•Conducted feature selection and engineering to enhance model performance and reduce complexity.', '•Integrated the trained model into a Django-based web application for user-friendly heart disease prediction.\nSource Code, Deploy.', 'Blog', '•Developed a dynamic blog application using Django, allowing users to create, edit, and publish blog posts.', '•Implemented modern design principles and responsive layouts for a seamless reading experience on various\ndevices.', '•Optimized website performance through efficient coding practices, enhancing loading speed and overall accessi-\nbility. Source code , Deploy.'], 'languages': ['•Hindi: Proficient', '•English: Intermediate'], 'achievements': ['•Solve 800+ problems over Geeks for Geeks, Leetcode, Hackerrank.', '•5 star in C & C++ on Hackerank.', '•3 star in Python on Hackerank.'], 'extracurricular': ['•Co-Founder and Vice President, Optimix Club', '•Member of E-Cell', '•Volunteer, Hamari Pahchan NGO']}