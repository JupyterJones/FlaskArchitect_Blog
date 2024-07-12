ip = get_ipython()

from IPython.display import display

def display_with_id(obj, display_id, update=False, execute_result=False):
    iopub = ip.kernel.iopub_socket
    session = get_ipython().kernel.session
    data, md = ip.display_formatter.format(obj)
    transient = {'display_id': str(display_id)}
    content = {'data': data, 'metadata': md, 'transient': transient}
    if execute_result:
      msg_type = 'execute_result'
      content['execution_count'] = ip.execution_count
    else:
      msg_type = 'update_display_data' if update else 'display_data'
    session.send(iopub, msg_type, content, parent=ip.parent_header)


display('above')
display_with_id(1, 'here')
display('below')

display_with_id(2, 'here')
display_with_id(3, 'there')
display_with_id(4, 'here')

display_with_id(5, 'there')
display_with_id(6, 'there', update=True)

display_with_id(7, 'here')
display_with_id(8, 'here', update=True)
display_with_id(9, 'result', execute_result=True)

display_with_id(10, 'result', update=True)

