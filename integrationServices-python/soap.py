from zeep import Client

# realizando uma integração de um serviço soap com python

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1('Hello', 'Bye')
print(result)