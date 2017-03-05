"""Get Message with given ID.
"""
from apiclient import errors

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """


  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    return message
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


