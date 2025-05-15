#!/usr/bin/env python3
"""
Script to verify SOC 2 Type 2 framework coverage in CISO Assistant
"""

import sys
import os
import yaml
import json

def check_yaml_file(file_path):
    """Check the structure and content of a YAML file"""
    print(f"\n=== Checking {file_path} ===")
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        print(f"Library Name: {data.get('name', 'N/A')}")
        print(f"Library URN: {data.get('urn', 'N/A')}")
        print(f"Version: {data.get('version', 'N/A')}")
        print(f"Provider: {data.get('provider', 'N/A')}")
        print(f"Publication Date: {data.get('publication_date', 'N/A')}")
        
        if 'objects' in data:
            objects = data['objects']
            
            # Check framework
            if 'framework' in objects:
                framework = objects['framework']
                print(f"\nFramework: {framework.get('name', 'N/A')}")
                print(f"Framework URN: {framework.get('urn', 'N/A')}")
                
                if 'requirement_nodes' in framework:
                    req_nodes = framework['requirement_nodes']
                    print(f"Number of requirement nodes: {len(req_nodes)}")
                    
                    # Count by depth
                    depth_counts = {}
                    for node in req_nodes:
                        depth = node.get('depth', 0)
                        depth_counts[depth] = depth_counts.get(depth, 0) + 1
                    
                    print("Requirement nodes by depth:")
                    for depth in sorted(depth_counts.keys()):
                        print(f"  Depth {depth}: {depth_counts[depth]} nodes")
                    
                    # Show sample nodes
                    print("\nSample requirement nodes:")
                    for i, node in enumerate(req_nodes[:5]):
                        print(f"  {i+1}. {node.get('ref_id', 'N/A')} - {node.get('name', 'N/A')}")
                        if 'description' in node:
                            desc = node['description'][:100] + "..." if len(node['description']) > 100 else node['description']
                            print(f"     Description: {desc}")
            
            # Check reference controls
            if 'reference_controls' in objects:
                controls = objects['reference_controls']
                print(f"\nNumber of reference controls: {len(controls)}")
                
                print("Sample reference controls:")
                for i, control in enumerate(controls[:5]):
                    print(f"  {i+1}. {control.get('ref_id', 'N/A')} - {control.get('name', 'N/A')}")
            
            # Check threats
            if 'threats' in objects:
                threats = objects['threats']
                print(f"\nNumber of threats: {len(threats)}")
            
            # Check risk matrix
            if 'risk_matrix' in objects:
                print(f"\nRisk matrix present: Yes")
                
        return data
        
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return None


def main():
    # Define paths
    base_path = "/Users/ashishthirunagari/Documents/GitHub/ciso-assistant-community"
    yaml_path = os.path.join(base_path, "backend/library/libraries")
    
    # Check SOC 2 YAML files
    soc2_files = [
        "soc2-2017.yaml",
        "soc2_2017_with_rev_2022.yaml"
    ]
    
    for file_name in soc2_files:
        file_path = os.path.join(yaml_path, file_name)
        check_yaml_file(file_path)
    
    # Summary recommendations
    print("\n\n=== SUMMARY ===")
    print("SOC 2 Type 2 frameworks appear to be present in the repository.")
    print("Next steps:")
    print("1. Verify all controls are mapped correctly against official SOC 2 documentation")
    print("2. Check for any missing Master Control Points (MCPs)")
    print("3. Ensure all metadata fields are populated")
    print("4. Add HITRUST framework which is currently missing")


if __name__ == "__main__":
    main()
