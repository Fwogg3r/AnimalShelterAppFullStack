#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username #'aacuser'
        PASS = password #'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30516
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    def create(self, data): #inserts an element into the database.
        if data is not None:
            try: #here I try to insert the value, and if an exception is raised, can assume the entry failed.
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                print(e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False
            
    '''def read(self, key, value): #returns a key, value list from the database.
        try:
            cur = self.database.animals.find({key: value})
            pyListConstructed = []
            for doc in cur:
                pyListConstructed.append(doc)
            return pyListConstructed #i just return the find query here, if it's empty, it wasn't found.
        except Exception as e:
            return []
            #return []'''
    
    def read(self, keyValueSet): #returns a key, value list from the database.
        try:
            cur = self.database.animals.find(keyValueSet)
            pyListConstructed = []
            for doc in cur:
                pyListConstructed.append(doc)
            return pyListConstructed #i just return the find query here, if it's empty, it wasn't found.
        except Exception as e:
            #return []
            return e
    
    def update(self, keyToUpdate, valueToUpdate, newKey, newValue): #updates a key, value pair to a new key, value
        try:
            #found = read(self, keyToUpdate, valueToUpdate) #find the values to update
            updateQuery = {"$set": { newKey: newValue }} #construct update query in a nested list
            result = self.database.animals.update_many({keyToUpdate: valueToUpdate}, updateQuery) #produce result object
            return result.modified_count #separate constructed result object into num updated objects, return
        except Exception as e:
            return 0 #if error, none updated.
        
    def delete(self, keyToDelete, valueToDelete): #deletes an existing key, value.
        try:
            #found = read(self, keyToUpdate, valueToUpdate) #find the values to update
            result = self.database.animals.delete_many({keyToDelete: valueToDelete}) #produce result object
            return result.deleted_count #separate constructed result object into num updated objects, return
        except Exception as e:
            return 0 #if error, none updated.
        