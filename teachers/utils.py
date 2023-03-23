def format_list_teachers(teachers):
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First Name</th>' \
             '<th>Last Name</th>' \
             '<th>Birthday</th>' \
             '<th>Salary</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for st in teachers:
        string += f'<tr>' \
                  f'<td>{st.first_name}</td>' \
                  f'<td>{st.last_name}</td>' \
                  f'<td>{st.birth_date}</td>' \
                  f'<td>{st.phone}</td>' \
                  f'<td><a href="/teachers/update/{st.pk}"/>Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string
