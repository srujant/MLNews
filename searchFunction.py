from apiclient.http import BatchHttpRequest
def list_animals(request_id, response, exception):
  if exception is not None:
    # Do something with the exception
    pass
  else:
    # Do something with the response
    pass

def list_farmers(request_id, response):
  """Do something with the farmers list response."""
  pass

service = build('farm', 'v2')

batch = service.new_batch_http_request()

batch.add(service.animals().list(), callback=list_animals)
batch.add(service.farmers().list(), callback=list_farmers)
batch.execute(http=http)