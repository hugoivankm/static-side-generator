from utilities.copy_dir_from_src_to_dst import copy_directory_from_src_to_dest
from page_generator import generate_pages_recursive


def main():
    try:
        copy_directory_from_src_to_dest('static/', 'public/')
        # generate_page('./content/index.md', './template.html', './public')
        generate_pages_recursive("./content", './template.html',  './public')
        
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()