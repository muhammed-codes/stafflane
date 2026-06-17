import os
import shutil
import re

ROOT_DIR = "/home/muhammad/Desktop/stafflane"
EXCLUDE_DIRS = {".git", "venv", "node_modules", "__pycache__", "staticfiles", "media", ".vscode", "docker", ".github"}
EXCLUDE_FILES = {".env", "docker-compose.yml"}

# Case-preserving replacements
REPLACEMENTS = [
    (r'stafflane', 'stafflane'),
    (r'Stafflane', 'Stafflane'),
    (r'stafflane', 'stafflane'),
    (r'Stafflane', 'Stafflane'),
    (r'stafflane_theme', 'stafflane_theme'),
    (r'stafflane_dbtemplate', 'stafflane_dbtemplate'),
    (r'stafflane_auth', 'stafflane_auth'),
    (r'stafflane_widgets', 'stafflane_widgets'),
    (r'stafflane_crumbs', 'stafflane_crumbs'),
    (r'stafflane_views', 'stafflane_views'),
    (r'stafflane_audit', 'stafflane_audit'),
    (r'stafflane_api', 'stafflane_api'),
    (r'stafflane_automations', 'stafflane_automations'),
    (r'stafflane_meet', 'stafflane_meet'),
    (r'stafflane_documents', 'stafflane_documents'),
    (r'stafflane_ldap', 'stafflane_ldap'),
    (r'stafflane_backup', 'stafflane_backup'),
    (r'stafflane', 'stafflane'),
    (r'Stafflane', 'Stafflane'),
    (r'STAFFLANE', 'STAFFLANE'),
    (r'stafflane', 'stafflane'),
    (r'Stafflane', 'Stafflane'),
    (r'stafflane-logo\.png', 'stafflane-logo.png'),
    (r'auth-logo\.png', 'auth-logo.png'), # Keep this name, just replace the image
    (r'logo\.svg', 'stafflane-logo.png') # Let's change references of stafflane-logo.png to stafflane-logo.png
]

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return False

    new_content = content
    for pattern, replacement in REPLACEMENTS:
        new_content = re.sub(pattern, replacement, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# First pass: replace content in all files
for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for file in files:
        if file in EXCLUDE_FILES or file.endswith('.png') or file.endswith('.jpg') or file.endswith('.svg') or file.endswith('.pyc') or file.endswith('.po') or file.endswith('.mo'):
            continue
        filepath = os.path.join(root, file)
        replace_in_file(filepath)

# Second pass: rename directories and files
# We do this bottom-up (by collecting and then reversing, or using topdown=False in os.walk)
dirs_to_rename = []
files_to_rename = []

for root, dirs, files in os.walk(ROOT_DIR, topdown=False):
    # Only care about non-excluded dirs
    if any(ex_dir in root.split(os.sep) for ex_dir in EXCLUDE_DIRS):
        continue
        
    for file in files:
        if 'stafflane' in file.lower() or 'stafflane' in file.lower():
            files_to_rename.append(os.path.join(root, file))
            
    for d in dirs:
        if d in EXCLUDE_DIRS:
            continue
        if 'stafflane' in d.lower() or 'stafflane' in d.lower():
            dirs_to_rename.append(os.path.join(root, d))

def compute_new_name(old_name):
    new_name = old_name
    for pattern, replacement in REPLACEMENTS:
        new_name = re.sub(pattern, replacement, new_name)
    return new_name

for old_path in files_to_rename:
    dir_name = os.path.dirname(old_path)
    base_name = os.path.basename(old_path)
    new_base = compute_new_name(base_name)
    if new_base != base_name:
        new_path = os.path.join(dir_name, new_base)
        os.rename(old_path, new_path)

for old_path in dirs_to_rename:
    dir_name = os.path.dirname(old_path)
    base_name = os.path.basename(old_path)
    new_base = compute_new_name(base_name)
    if new_base != base_name:
        new_path = os.path.join(dir_name, new_base)
        os.rename(old_path, new_path)

print("Replacement and renaming complete!")
