import os

def get_directory_structure(base_dir):
    """Recursively collects the directory structure while preserving order."""
    structure = []

    for root, dirs, files in os.walk(base_dir):
        # Ignore hidden & exclude folders and files 
        dirs[:] = [d for d in sorted(dirs) if not d.startswith('.') and not d.startswith('image')]
        files = [f for f in sorted(files) if not f.startswith('.') and f not in ["README.md", "index.md"]]
        

        # Store current folder
        folder_relative_path = os.path.relpath(root, start=base_dir)
        structure.append((folder_relative_path, "folder"))

        # Store markdown files (excluding README.md)
        for file in files:
            if file.endswith(".md"):
                file_relative_path = os.path.relpath(os.path.join(root, file), start=base_dir)
                structure.append((file_relative_path, "file"))

    return structure

def format_summary_entry(relative_path, entry_type, depth):
    """Formats entries for SUMMARY.md while maintaining hierarchy."""
    indent = "  " * depth  # Adjusts indentation for nested entries
    # name of the page, used in summary.md & remove .md extension
    name = os.path.splitext(os.path.basename(relative_path))[0].replace("_", " ").title()  
    
    # Build summary.md
    if entry_type == "folder":
        return f"{indent}- [{name}]({relative_path}/README.md)\n"
    else:
        return f"{indent}- [{name}]({relative_path})\n"

def main():
    # Prommpt: specify base_dir
    base_dir = input("Enter the base directory of your lab guide: ").strip()
    # Check base_dir exist
    if not os.path.exists(base_dir):
        print("Error: Directory does not exist.")
        return
    # Get folders, files and relative_paths
    structure = get_directory_structure(base_dir)
    selected_entries = []
    folder_depths = {}  # Track nesting depth for correct indentation

    for relative_path, entry_type in structure:
        depth = relative_path.count(os.sep)  # Determine indentation level

        if entry_type == "folder":
            include = input(f"Include folder {relative_path}? (y/n): ").strip().lower()
            if include == "y":
                selected_entries.append((relative_path, entry_type, depth))
                folder_depths[relative_path] = depth  # Store folder depth
        else:
            parent_folder = os.path.dirname(relative_path)
            if parent_folder in folder_depths:  # Only prompt if the parent is selected
                include = input(f"  Include file {relative_path}? (y/n): ").strip().lower()
                if include == "y":
                    selected_entries.append((relative_path, entry_type, folder_depths[parent_folder] + 1))

    summary_content = "# Summary\n\n"

    for relative_path, entry_type, depth in selected_entries:
        summary_content += format_summary_entry(relative_path, entry_type, depth)

    summary_path = os.path.join(base_dir, "SUMMARY.md")
    with open(summary_path, "w") as summary_file:
        summary_file.write(summary_content)

    print("\n ✅ SUMMARY.md has been generated successfully!")

if __name__ == "__main__":
    main()
