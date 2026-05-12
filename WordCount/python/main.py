class counter():

    def __init__(self, input_string, option):
        self.input_string = input_string
        self.option = option

    def count(self):
        self.word_count = 1 
        self.input_string = self.input_string.strip(" ")  
        print (f'in count functio***{self.input_string}***')  
        for character in self.input_string:        
            print("character",character)
            if character == " ":
                self.word_count =  self.word_count + 1
                print("in space loop")
            print ("word_count",self.word_count )
        return self.word_count

def main():

     
    string_input = "Hello from "

    counter_input = counter(string_input,"")
    print(counter_input.count())

if __name__ == "__main__":
    main()
