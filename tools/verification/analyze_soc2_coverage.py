#!/usr/bin/env python3
"""
Analyze SOC 2 Type 2 Trust Service Criteria Coverage
"""

import re
import sys

def analyze_soc2_yaml(file_path):
    """Analyze SOC 2 YAML file for trust service criteria coverage"""
    
    # Define the five trust service criteria categories
    tsc_categories = {
        'CC': 'Common Criteria (Security)',
        'A': 'Availability',
        'C': 'Confidentiality', 
        'PI': 'Processing Integrity',
        'P': 'Privacy'
    }
    
    # Initialize counters
    criteria_counts = {cat: [] for cat in tsc_categories}
    total_controls = 0
    assessable_controls = 0
    
    print(f"=== ANALYZING SOC 2 YAML FILE ===")
    print(f"File: {file_path}\n")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_ref_id = None
        is_assessable = False
        
        for i, line in enumerate(lines):
            # Look for ref_id
            if 'ref_id:' in line:
                match = re.search(r'ref_id:\s*(.+)', line)
                if match:
                    current_ref_id = match.group(1).strip()
                    total_controls += 1
                    
                    # Categorize by trust service criteria
                    for cat in tsc_categories:
                        if current_ref_id.startswith(cat):
                            criteria_counts[cat].append(current_ref_id)
                            break
            
            # Check if assessable
            if 'assessable:' in line and 'true' in line:
                assessable_controls += 1
        
        # Print results
        print("Trust Service Criteria Coverage:")
        print("-" * 40)
        
        for cat, desc in tsc_categories.items():
            count = len(criteria_counts[cat])
            print(f"{cat}: {desc}")
            print(f"   Controls found: {count}")
            
            if count > 0:
                # Show sample controls
                samples = criteria_counts[cat][:3]
                print(f"   Sample controls: {', '.join(samples)}")
                
                # Show range
                if count > 3:
                    first = criteria_counts[cat][0]
                    last = criteria_counts[cat][-1]
                    print(f"   Range: {first} to {last}")
            print()
        
        print(f"Total controls: {total_controls}")
        print(f"Assessable controls: {assessable_controls}")
        
        # Check for completeness - SOC 2 Type 2 typically has these ranges
        expected_ranges = {
            'CC': ('CC1', 'CC9'),  # Common Criteria typically CC1-CC9
            'A': ('A1',),          # Availability
            'C': ('C1',),          # Confidentiality  
            'PI': ('PI1',),        # Processing Integrity
            'P': ('P1', 'P8')      # Privacy typically P1-P8
        }
        
        print("\n=== COMPLETENESS CHECK ===")
        incomplete = []
        
        for cat, expected in expected_ranges.items():
            if criteria_counts[cat]:
                # Check first control
                first_found = criteria_counts[cat][0]
                if not first_found.startswith(expected[0]):
                    incomplete.append(f"{cat}: Missing controls before {first_found}")
                
                # Check last control for categories with ranges
                if len(expected) > 1:
                    last_found = criteria_counts[cat][-1]
                    if not last_found.startswith(expected[1]):
                        incomplete.append(f"{cat}: May be missing controls after {last_found}")
            else:
                incomplete.append(f"{cat}: No controls found")
        
        if incomplete:
            print("Potential gaps identified:")
            for issue in incomplete:
                print(f"  - {issue}")
        else:
            print("✓ All expected trust service criteria appear to be covered")
            
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return True


def main():
    base_path = "/Users/ashishthirunagari/Documents/GitHub/ciso-assistant-community"
    soc2_yaml = f"{base_path}/backend/library/libraries/soc2_2017_with_rev_2022.yaml"
    
    print("SOC 2 Type 2 Framework Analysis")
    print("=" * 40)
    
    # Analyze the main SOC 2 file
    analyze_soc2_yaml(soc2_yaml)
    
    print("\n=== RECOMMENDATIONS ===")
    print("1. Verify that all controls match the official SOC 2 2017 TSC")
    print("2. Check that 2022 revision points of focus are included")
    print("3. Ensure all controls have proper descriptions and metadata")
    print("4. Validate any MCPs (Master Control Points) if defined")
    print("5. Consider creating a mapping to ISO 27001 or other frameworks")


if __name__ == "__main__":
    main()
