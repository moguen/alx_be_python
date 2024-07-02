# pattern_drawing.py

def draw_pattern(size):
     # Outer loop for rows
     while size > 0:
           # Inner loop for columns in each row
           for _ in range(size):
               print("*", end="")
           print()  # Move to the next line after each row
           size -= 1  # Decrement size to move towards a square shape

def main():
    # Prompt user to enter the size of the patten
    size = int(input("Enter the size of the pattern: "))
                                                                                
    if size <=0:
       print("Please enter a positive integer.")
    else:
                                                                                                                draw_pattern(size)
                                                                                                    

if __name__ == "__main__":
                                                                                                             main()
