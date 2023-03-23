def format_list_groups(groups):
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>Group Name</th>' \
             '<th>Start date</th>' \
             '<th>Group Description</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for st in groups:
        string += f'<tr>' \
                  f'<td>{st.group_name}</td>' \
                  f'<td>{st.start_date}</td>' \
                  f'<td>{st.group_description}</td>' \
                 f'<td><a href="/groups/update/{st.pk}"/>Edit</a></td>' \
                  f'</tr>'
    string += '</tbody></table>'
    return string
