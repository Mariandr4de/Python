from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AlzaSyAI0coggbHzTCe5rGF86FLUKw2YPMM').geocoder(endereco).coordinates)