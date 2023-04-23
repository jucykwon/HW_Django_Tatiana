def format_list_groups(courses):
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>Course Name</th>' \
             '<th>Start date</th>' \
             '<th>Course Description</th>' \
             '<th>Active course</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for st in courses:
        string += f'<tr>' \
                  f'<td>{st.course_name}</td>' \
                  f'<td>{st.start_date}</td>' \
                  f'<td>{st.course_description}</td>' \
                  f'<td>{st.is_active}</td>' \
                  f'<td><a href="/courses/update/{st.pk}"/>Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return
