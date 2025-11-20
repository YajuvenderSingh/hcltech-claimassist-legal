#!/usr/bin/env python3
"""
Update Python files to use HCL table names instead of NMM table names
"""

import os
import re

def update_file_table_names(file_path):
    """
    Update table names in a Python file
    """
    replacements = {
        'nmm-doc-extraction': 'hcltech-doc-extraction',
        'nmm-doc-dashboard': 'hcltech-doc-dashboard',
        'nmm-dashboard': 'hcltech-doc-dashboard'
    }
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        original_content = content
        
        # Replace table names
        for old_name, new_name in replacements.items():
            content = content.replace(f'"{old_name}"', f'"{new_name}"')
            content = content.replace(f"'{old_name}'", f"'{new_name}'")
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"✅ Updated: {file_path}")
            return True
        else:
            print(f"ℹ️  No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """
    Update all Python files in the current directory
    """
    print("🔄 Updating table names in Python files...")
    
    python_files = [
        'agent1_docextraction_agent.py',
        'agent2_docclassification_agent.py', 
        'agent3_doc_entity_extraction.py',
        'orchestrator.py',
        'orchestrator-agent.py'
    ]
    
    updated_count = 0
    
    for file_name in python_files:
        if os.path.exists(file_name):
            if update_file_table_names(file_name):
                updated_count += 1
        else:
            print(f"⚠️  File not found: {file_name}")
    
    print(f"\n📊 Summary: {updated_count} files updated")
    print("\n✅ Table name update completed!")

if __name__ == "__main__":
    main()
