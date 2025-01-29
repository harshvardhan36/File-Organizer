
import os      # To interact with the operating system
import shutil  # For copying and moving
import logging # use for logs.

  #Organise the files by their type.
def organize_files_by_type(directory):
  
    # List all files in the given directory
    files = os.listdir(directory)
    
    # Create subfolders for each file type (if not already created)
    for file in files:
        # Skip hidden files
        if file.startswith('.'):
            continue
        
        # Full path of the file
        file_path = os.path.join(directory, file)
        
        # Skip directories, only process files
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension 
        file_extension = file.split('.')[-1].lower()
        
        # Skip files without extensions
        if len(file.split('.')) == 1:
            continue
        
        # Creating a folder for the extension if it doesn't exist
        folder_name = os.path.join(directory, file_extension)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Move the file into the appropriate folder
        try:
            shutil.move(file_path, os.path.join(folder_name, file))
            logging.info(f"Moved: {file} -> {folder_name}")
        except Exception as e:
            logging.error(f"Error moving file {file}: {e}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    directory = input("Enter the path to the folder you want to organize: ")
    if os.path.exists(directory):
        organize_files_by_type(directory)
    else:
        print("The specified directory does not exist.")