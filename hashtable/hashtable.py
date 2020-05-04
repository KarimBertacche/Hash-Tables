class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity=53):
        self.capacity = capacity
        self.storage = [0] * capacity 

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # prime number
        hash = 5381

        # loop through each character within key
        for char in key:
            # make the hash the sum of the charCode of the character 
            # plus the prime number times 33
            hash = (hash * 33) + ord(char)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # first grab index by hashing key
        index = self.hash_index(key)

        current_node = self.storage[index]
        # check if the memory slot is empty
        if current_node is None:
            # if so store key value pair as a linked list node
            current_node = HashTableEntry(key, value)
        else:
            # check if next node is None, end of linked list
            if current_node.next is None:
                # if so place value by creating connection
                current_node.next = HashTableEntry(key, value)

            # else iterate over the list of nodes until an empty space is found
            while current_node.next is not None:
                # if a node key in the linked list matches the key
                if current_node.key == key:
                    # replace the value
                    current_node.value = value
                    # stop looping
                    break
                # set current node to be node.next
                # to move forward in the linked list
                current_node = current_node.next

            # if no matches are found for the key and we are at the end of the loop
            # then set the last node next to the new key value pair
            current_node.next = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # hash the current key
        index = hash_index(key)
        # grab the first linked list node within list that matches the key
        current_node = self.storage[key]

        # if there is a node in the linked list 
        if current_node != None:
            # check if the node key is equal to the key
            # that needs to be deleted
            if current_node.key == key:
                # if so remove the node
                current_node = None
            else:
                # move to the next node
                next_node = current_node.next

                # iterate until there is a next 
                while next_node is not None:
                    # check if next node key matches given key
                    if next_node.key == key:
                        # if so delete node
                        next_node = None
                        # stop iteration
                        break
                    else:
                        # move to next iteration
                        # and set the next node
                        next_node = next_node.next
            
        else:
            # if not found print message
            print(f"Key:{key} not found in memory")

            


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # grab index by hashing key
        index = hash_index(key)
        # grab the first node
        current_node = self.storage[index]

        # check if the current node is not None
        if current_node is not None:
            # if the current node key matches the given key
            if current_node.key == key:
                # then return the value of that node
                return current_node.value
            else:
                # else set the next node to be the current node next
                next_node = current_node.next
                # iterate over while there is a next
                while next_node is not None:
                    # if the next node key is equal to the given key
                    if next_node.key == key:
                        # return the next node value
                        return next_node.value
                    else:
                        # else move to the following node
                        next_node = next_node.next 
        else: 
            # if so return None
            return None


    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
