import pickle
import StringIO

class objectGoingToSerializing:
    field1 = 1
    field2 = 2.8
    field3 = "abc"

_stream = StringIO.StringIO()
source = objectGoingToSerializing()
source.field1 = 5
# serialization
pickle.dump(source, _stream)
# sourceAsByteIO = io.BytesIO()
# pickle.dump(source, sourceAsByteIO)
# print sourceAsByteIO

# deserialization
obj = pickle.load(StringIO.StringIO(_stream.getvalue()))
# obj = pickle.load(sourceAsByteIO.read(-1))

print objectGoingToSerializing()
print repr(_stream)
print obj.field1
print obj == source

