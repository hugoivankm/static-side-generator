from utilities.copy_dir_from_src_to_dst import copy_directory_from_src_to_dest

def main():
    try:
        copy_directory_from_src_to_dest('static/', 'public/')
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()