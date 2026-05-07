class counter():
     

def main():
    character_count = 1
    string_input = "Hello from"
    for character in string_input:
        string_input.strip()
        print("character",character)
        if character == " ":
           character_count =  character_count + 1
    print ("character_count",character_count )         
      
if __name__ == "__main__":
    main()

