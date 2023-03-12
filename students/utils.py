def format_list_students(students):
    # string = '<br>'.join(str(student) for student in students)
    string = '<table><thead><tr><th>First Name</th><th>Last Name</th><th>Email</th><th>Birthday</th><thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td>' \
                  f'<td>{st.phone}</td></tr>'
    string += '</tbody></table>'
    return string
