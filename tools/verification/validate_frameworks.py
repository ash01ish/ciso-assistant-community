#!/usr/bin/env python3
"""
Framework Validation Script for CISO Assistant
Helps validate that framework files meet requirements
"""

import os
import sys
import re

def validate_yaml_structure(file_path):
    """Validate YAML file structure without parsing"""
    
    print(f"Validating: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return False
    
    required_fields = [
        'urn:',
        'locale:',
        'ref_id:',
        'name:',
        'description:',
        'version:',
        'provider:',
        'objects:'
    ]
    
    found_fields = set()
    has_framework = False
    control_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for required fields
            for field in required_fields:
                if field in content:
                    found_fields.add(field)
            
            # Check for framework object
            if 'framework:' in content:
                has_framework = True
            
            # Count requirement nodes
            control_count = content.count('urn:intuitem:risk:req_node:')
            
        print("\nValidation Results:")
        print(f"Required fields found: {len(found_fields)}/{len(required_fields)}")
        
        missing_fields = set(required_fields) - found_fields
        if missing_fields:
            print(f"Missing fields: {missing_fields}")
        else:
            print("✓ All required fields present")
        
        if has_framework:
            print("✓ Framework object found")
        else:
            print("✗ Framework object missing")
        
        print(f"Control count: {control_count}")
        
        return len(missing_fields) == 0 and has_framework
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False


def check_excel_structure(file_path):
    """Check Excel file structure without openpyxl"""
    
    print(f"Checking Excel structure: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return False
    
    # Since we can't use openpyxl, just verify file exists and has .xlsx extension
    if file_path.endswith('.xlsx'):
        print("✓ Excel file format (.xlsx)")
        print("Note: Cannot validate sheet structure without openpyxl library")
        return True
    else:
        print("✗ Not an Excel file (.xlsx)")
        return False


def list_frameworks(directory):
    """List all framework files in a directory"""
    
    yaml_files = []
    excel_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                yaml_files.append(os.path.join(root, file))
            elif file.endswith('.xlsx'):
                excel_files.append(os.path.join(root, file))
    
    return yaml_files, excel_files


def main():
    base_path = "/Users/ashishthirunagari/Documents/GitHub/ciso-assistant-community"
    
    print("CISO Assistant Framework Validator")
    print("="*40)
    
    # Check YAML frameworks
    yaml_dir = os.path.join(base_path, "backend/library/libraries")
    yaml_files, _ = list_frameworks(yaml_dir)
    
    print(f"\nFound {len(yaml_files)} YAML framework files")
    
    # Look specifically for SOC 2 and HITRUST
    soc2_found = False
    hitrust_found = False
    
    for file in yaml_files:
        filename = os.path.basename(file).lower()
        if 'soc2' in filename:
            soc2_found = True
            print(f"\nSOC 2 Framework: {filename}")
            validate_yaml_structure(file)
        elif 'hitrust' in filename:
            hitrust_found = True
            print(f"\nHITRUST Framework: {filename}")
            validate_yaml_structure(file)
    
    # Check Excel source files
    excel_dir = os.path.join(base_path, "tools")
    _, excel_files = list_frameworks(excel_dir)
    
    print(f"\n\nFound {len(excel_files)} Excel source files")
    
    for file in excel_files:
        filename = os.path.basename(file).lower()
        if 'soc2' in filename:
            print(f"\nSOC 2 Excel: {filename}")
            check_excel_structure(file)
        elif 'hitrust' in filename:
            print(f"\nHITRUST Excel: {filename}")
            check_excel_structure(file)
    
    # Summary
    print("\n" + "="*40)
    print("SUMMARY")
    print("="*40)
    
    print(f"SOC 2 Framework: {'✓ Found' if soc2_found else '✗ Not Found'}")
    print(f"HITRUST Framework: {'✓ Found' if hitrust_found else '✗ Not Found'}")
    
    if not hitrust_found:
        print("\nHITRUST Implementation Steps:")
        print("1. Create Excel file with framework structure")
        print("2. Run: python3 convert_library.py hitrust/HITRUST_CSF_v11.xlsx")
        print("3. Move YAML to backend/library/libraries/")
        print("4. Validate using this script")
        print("5. Test in CISO Assistant application")


if __name__ == "__main__":
    main()
