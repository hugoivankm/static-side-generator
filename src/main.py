from textnode import TextNode

def main():
   try:
       text_node = TextNode("This is a text node", "text", "https://www.boot.dev")
       print(text_node)
   except ValueError as e:
       print(e)
    
if __name__ == "__main__":
    main()