#!/usr/bin/env python3
"""
Simple script to verify SOC 2 Type 2 framework coverage in CISO Assistant
"""

import os
import json

def verify_soc2_framework():
    """Verify SOC 2 Type 2 framework status"""
    
    base_path = "/Users/ashishthirunagari/Documents/GitHub/ciso-assistant-community"
    
    # Check YAML files
    yaml_path = os.path.join(base_path, "backend/library/libraries")
    soc2_yaml_files = []
    hitrust_yaml_files = []
    
    print("=== CHECKING YAML LIBRARY FILES ===")
    
    try:
        files = os.listdir(yaml_path)
        for file in files:
            if 'soc2' in file.lower() and file.endswith('.yaml'):
                soc2_yaml_files.append(file)
            if 'hitrust' in file.lower() and file.endswith('.yaml'):
                hitrust_yaml_files.append(file)
        
        print(f"\nSOC 2 YAML files found: {len(soc2_yaml_files)}")
        for file in soc2_yaml_files:
            print(f"  - {file}")
        
        print(f"\nHITRUST YAML files found: {len(hitrust_yaml_files)}")
        if not hitrust_yaml_files:
            print("  - NONE (Framework needs to be added)")
        else:
            for file in hitrust_yaml_files:
                print(f"  - {file}")
    
    except Exception as e:
        print(f"Error checking YAML files: {e}")
    
    # Check Excel files
    excel_path = os.path.join(base_path, "tools")
    soc2_excel_files = []
    hitrust_excel_files = []
    
    print("\n=== CHECKING EXCEL SOURCE FILES ===")
    
    # Walk through tools directory
    for root, dirs, files in os.walk(excel_path):
        for file in files:
            if file.endswith('.xlsx'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, excel_path)
                
                if 'soc2' in file.lower():
                    soc2_excel_files.append(rel_path)
                if 'hitrust' in file.lower():
                    hitrust_excel_files.append(rel_path)
    
    print(f"\nSOC 2 Excel files found: {len(soc2_excel_files)}")
    for file in soc2_excel_files:
        print(f"  - {file}")
    
    print(f"\nHITRUST Excel files found: {len(hitrust_excel_files)}")
    if not hitrust_excel_files:
        print("  - NONE (Source file needs to be created)")
    else:
        for file in hitrust_excel_files:
            print(f"  - {file}")
    
    # Summary and recommendations
    print("\n=== SUMMARY AND RECOMMENDATIONS ===")
    
    print("\nSOC 2 Type 2 Framework:")
    if soc2_yaml_files and soc2_excel_files:
        print("✓ Framework appears to be present in both Excel and YAML formats")
        print("  Actions needed:")
        print("  1. Verify all controls match official SOC 2 Type 2 documentation")
        print("  2. Check for completeness (all Trust Service Criteria covered)")
        print("  3. Validate MCPs and control mappings")
    elif soc2_excel_files and not soc2_yaml_files:
        print("⚠ Excel files found but no YAML files")
        print("  Action: Run convert_library.py to generate YAML files")
    else:
        print("✗ Framework appears to be incomplete or missing")
    
    print("\nHITRUST Framework:")
    if not hitrust_yaml_files and not hitrust_excel_files:
        print("✗ Framework is completely missing")
        print("  Actions needed:")
        print("  1. Create HITRUST Excel file with all controls")
        print("  2. Convert Excel to YAML using convert_library.py")
        print("  3. Validate and test the converted framework")
    elif hitrust_excel_files and not hitrust_yaml_files:
        print("⚠ Excel files found but no YAML files")
        print("  Action: Run convert_library.py to generate YAML files")
    else:
        print("✓ Framework files found")
        print("  Action: Verify completeness and accuracy")


if __name__ == "__main__":
    verify_soc2_framework()
