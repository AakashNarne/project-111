import os
import shutil

def organize_downloads(download_folder, target_folder, document_extensions, specific_names):
    # Ensure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created folder: {target_folder}")

    # Iterate through all the files in the download folder
    for item in os.listdir(download_folder):
        item_path = os.path.join(download_folder, item)
        
        # Get the file name without the extension
        base_name, ext = os.path.splitext(item)
        
        # Check if the item is a file and either has one of the document extensions or matches the specific names
        if os.path.isfile(item_path) and (
            item.lower().endswith(document_extensions) or base_name in specific_names):
            # Move the file to the target folder
            shutil.move(item_path, target_folder)
            print(f"Moved: {item}")

def main():
    # Define the path to the Downloads folder
    downloads_path = os.path.expanduser("~/Downloads")  # This works for most OS
    
    # Define the path to the Document_Files folder
    document_files_path = os.path.join(downloads_path, "Document_Files")
    
    # Define the document file extensions to look for
    document_extensions = (".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".xls", ".ppt")
    
    # Define specific file names to move
    specific_names = ["hf (1)", "Despicable Me_ Steal the moon (HD CLIP)"]

    # Call the function to organize the Downloads folder
    organize_downloads(downloads_path, document_files_path, document_extensions, specific_names)

if __name__ == "__main__":
    main()
