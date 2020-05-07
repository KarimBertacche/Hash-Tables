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
        self.storage = [None] * capacity 
        self.el_count = 0

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
        hashed_value = 5381

        # loop through each character within key
        for char in key:
            # make the hash the sum of the charCode of the character 
            # plus the prime number times 33
            hashed_value = (hashed_value * 33) + ord(char)

        return hashed_value

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

        # if the current node is None
        if self.storage[self.hash_index(key)] != None:
            current = self.storage[self.hash_index(key)]
            # while there is a current keep iterating
            while current:
                # if current node key matches given key
                if current.key == key:
                    # set current node value to the new given value
                    current.value = value
                    # break out of loop
                    break
                # if the current node as a next
                if current.next != None:
                    # set current node to be the next node
                    current = current.next
                else:
                    # else break out of the loop
                    break
            # and set the current node next to be the new key value pair
            current.next = HashTableEntry(key, value)
            # increase element count by one
            self.el_count += 1
            # check if hashTable needs to be resized
            self.resize()
        else:
            # if there is no value already in the current node
            # set that to the key value pair given
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)
            # increase element count by one
            self.el_count += 1
            # check if hashTable needs to be resized
            self.resize()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        if  self.storage[self.hash_index(key)] != None:
            previous_node = None
            current_node = self.storage[self.hash_index(key)]
            next_node = current_node.next
            while True:
                if current_node.key == key:
                     # If the current node is the only one in the list
                    if previous_node == None and next_node == None:
                        # we set that to None
                        self.storage[self.hash_index(key)] = None
                        # break out of loop
                        break
                    # if the current node has no previous node but a next (start of list)
                    if previous_node == None and next_node != None:
                        # we make the current node to be the next node in line
                        self.storage[self.hash_index(key)] = next_node
                        # we break out of the loop
                        break
                    # if the node has a previous and next
                    if previous_node != None and next_node != None:
                        # previous node will point to the current next
                        previous_node.next = next_node
                        # break out of loop
                        break
                    # if the current node is the last one in the list and there are no next
                    if previous_node != None and next_node == None:
                        # set the previous node next to be None
                        previous_node.next = None
                        # break out of the loop
                        break
                    # decrease element count by one
                    self.el_count -= 1
                    # check if hashTable needs to be resized
                    self.resize()

                # else if there is a next move forward until there are next nodes 
                elif current_node.next != None:
                    # set the previous to be the current node
                    previous_node = current_node
                    # set the current to be the next node
                    current_node = current_node.next
                    # and set the next node to be the new current next node
                    next_node = current_node.next

                # if no matches are found 
                else:
                    # print a message
                    print(f"Key:{key} not found in memory")
                    # and break out of the loop
                    break
        # no node is present
        else:
            # print a message
            print(f"Key:{key} not found in memory")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # grab index by hashing key
        index = self.hash_index(key)
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
    
    def relocate_entries(self, prev_storage):
        # iterate over the previous storage entries
        for entry in prev_storage:
            # if the entry is not empty
            if entry != None:
                # set the current node to be the entry
                current_node = entry

                # and while there is an entry
                while current_node is not None:
                    # pass that to the new storage with increased capacity the entry
                    self.put(current_node.key, current_node.value)
                    # if there is a next set the current to be next in line and so on
                    current_node = current_node.next


    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # if element/slot are > 70% - Grow Factor
        if int((self.el_count / self.capacity) * 100) > 70:
            # double the current storage capacity
            self.capacity *= 2
            # save the previous storage content in a variable
            prev_storage = self.storage
            # allocate new slots in accordance with new capacity
            self.storage = [None] * self.capacity
            # invoke method to relocate entries to new increased storage
            self.relocate_entries(prev_storage)
        
        # if element/slot are < 20% - Low Factor
        elif int((self.el_count / self.capacity) * 100) < 20 and self.capacity >= 16:
            # half the capacity 
            self.capacity /= 2
            # save previous storage content for later retrieval
            prev_storage = self.storage
            # relocate slots
            self.storage = [None] * self.capacity
            # invoke method to relocate entries to new shrank storage
            self.relocate_entries(prev_storage)
            

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
