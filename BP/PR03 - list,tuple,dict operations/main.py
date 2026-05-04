# --- List ---
my_list = [10, 20]
val_list_add = int(input("Enter integer to add to list: "))
my_list.append(val_list_add)
val_list_del = int(input("Enter value to remove from list: "))
if val_list_del in my_list:
    my_list.remove(val_list_del)
print(f"List: {my_list}\n")

# --- Set ---
my_set = {10, 20}
val_set_add = int(input("Enter integer to add to set: "))
my_set.add(val_set_add)
val_set_del = int(input("Enter value to remove from set: "))
my_set.discard(val_set_del)
print(f"Set: {my_set}\n")

# --- Tuple ---
# Tuples are immutable; addition/deletion requires creating a new object
my_tuple = (10, 20)
val_tuple_add = int(input("Enter integer to add to tuple: "))
my_tuple += (val_tuple_add,)
val_tuple_del = int(input("Enter value to remove from tuple: "))
temp_list = list(my_tuple)
if val_tuple_del in temp_list:
    temp_list.remove(val_tuple_del)
my_tuple = tuple(temp_list)
print(f"Tuple: {my_tuple}\n")

# --- Dictionary ---
my_dict = {"a": 1, "b": 2}
k_add = input("Enter key to add to dict: ")
v_add = int(input("Enter value for key: "))
my_dict[k_add] = v_add
k_del = input("Enter key to delete from dict: ")
my_dict.pop(k_del, None)
print(f"Dictionary: {my_dict}")
