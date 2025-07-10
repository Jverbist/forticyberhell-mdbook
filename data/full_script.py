import os

SRC_DIR = "src"  # Define the source directory

def get_directory_structure(base_dir):
    """Recursively collects the directory structure while preserving order."""
    structure = []

    for root, dirs, files in os.walk(base_dir):
        # Ignore hidden & exclude folders like "image"
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
    name = os.path.splitext(os.path.basename(relative_path))[0].replace("_", " ").title()  # Format name

    # Build summary.md
    if entry_type == "folder":
        return f"{indent}- [{name}]({relative_path}/README.md)\n"
    else:
        return f"{indent}- [{name}]({relative_path})\n"

def generate_summary():
    """Generates SUMMARY.md based on the 'src' folder structure."""
    if not os.path.exists(SRC_DIR):
        print("\n❌ Error: 'src' directory not found! Run the script from the correct location.")
        return

    structure = get_directory_structure(SRC_DIR)
    summary_content = "# Summary\n\n"
    folder_depths = {}  # Track folder depth

    for relative_path, entry_type in structure:
        depth = relative_path.count(os.sep)  # Determine indentation level

        if entry_type == "folder":
            summary_content += format_summary_entry(relative_path, entry_type, depth)
            folder_depths[relative_path] = depth  # Store folder depth
        else:
            parent_folder = os.path.dirname(relative_path)
            if parent_folder in folder_depths:  # Ensure file is under an included folder
                summary_content += format_summary_entry(relative_path, entry_type, folder_depths[parent_folder] + 1)

    # Write to SUMMARY.md inside "src" folder
    summary_path = os.path.join(SRC_DIR, "SUMMARY.md")
    with open(summary_path, "w") as summary_file:
        summary_file.write(summary_content)

    print("\n✅ SUMMARY.md has been generated successfully inside 'src' folder!")

if __name__ == "__main__":
    generate_summary()
