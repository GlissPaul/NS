# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

# Creating Hashtable as a nested List.
HashTable = [[] for _ in range(10)]

# Hashing Function to return key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Delhi')
insert(HashTable, 9, 'Mathura')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 21, 'Noida')

display_hash(HashTable)


OR 

import hashlib

def hash_function(message):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the message to bytes and feed it to the hash object
    hash_object.update(message.encode())

    # Get the hash value in hexadecimal format
    hash_value = hash_object.hexdigest()

    return hash_value

# Example usage
message = "Hello, world!"
hashed_message = hash_function(message)
print("Hash value:", hashed_message)
