import os
import sys

sys.path.append('C:\Python311\Scripts')

import constants
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.APIKEY

# query = sys.argv[1]


print(sys.path)

loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))


