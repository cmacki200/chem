from pickle import load
import molecules_api.api as ma

"""
Create a Python package 'molecules_api' that has an API module 'api'
based on pymongo. This API must allow manipulating the data in the
input pickle database.
Keep in mind each entry of this database is a dictionary.

The API must expose the following functionality:


1. creation of a MongoDB database named Reactions

2. creation of a first collection named ReactionData, including
the keys 'reaxys_id', 'smiles', 'name', 'formula' and 'InChI_key' from
the input database. The API must take the number of documents as input
(within the size of the input database)

3. creation of a second collection with name ReactionMetadata,
using the keys 'n_references', 'ma_publication_year', 'entry_date' and
'update_date' from the original database

4. addition of new documents (single or multiple) in any of the
collections

5. modification of an existing document in any of the collections

6. deletion of existing documents in any of the collections

Use this test script to:

- Demonstrate the functionality of APIs 2 and 3 using the first 1,000,000
elements of the input database only.

- Demonstrate the functionality of APIs 4 to 6 by adding the next 50,000
elements of the input database into the created collections, then
modifying the last element in each collection and finally deleting the
last 359,999 elements of each collection.

Pointers:
- Assume the database is in the same directory as this test script.

"""

def main():
    FILE_NAME = "molecules_part1.p"

    infile = open(FILE_NAME,'rb')
    molecules = load(infile)
    molecules_keys = molecules.keys()

    # Your test code goes here


    infile.close()


if "__main__" ==__name__:
    main()