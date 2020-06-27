from zeep import Client

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1('Hello', 'Bye')
print(result)