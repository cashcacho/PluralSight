#contacts dictionary
contacts = {
    'number': 4,
    'students':
        [
            {'name':'Justine Cacho', 'email':'justinecacho@example.com'},
            {'name':'Kristi Nguyen', 'email':'kristinguyen@example.com'},
            {'name':'Kobe Bryant', 'email':'kobebryant@example.com'},
            {'name':'Travis Scott', 'email':'travisscott@example.com'},
        ]
}

print('Student emails:')
for student in contacts['students']:
    
    """#Will print out names and emails
    print(student)"""

    #print out only email lits
    print(student['email'])