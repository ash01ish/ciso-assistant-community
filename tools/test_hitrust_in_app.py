#!/usr/bin/env python3
"""
Test script to verify HITRUST CSF v11 framework is loaded in CISO Assistant
"""
import requests
import json
import time
import urllib3

# Disable SSL warnings for local testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://localhost:8443"
API_URL = f"{BASE_URL}/api"

def test_hitrust_framework():
    print("CISO Assistant HITRUST Framework Test")
    print("="*40)
    
    # Wait for services to be ready
    print("Waiting for services to be ready...")
    time.sleep(5)
    
    # Test API connectivity
    print("\n1. Testing API connectivity...")
    try:
        response = requests.get(f"{API_URL}/build", verify=False)
        if response.status_code == 200:
            print("✓ API is accessible")
            build_info = response.json()
            print(f"  Version: {build_info.get('version', 'N/A')}")
        else:
            print(f"✗ API returned status code: {response.status_code}")
            return
    except Exception as e:
        print(f"✗ Failed to connect to API: {e}")
        print("Make sure CISO Assistant is running on https://localhost:8443")
        return
    
    # Login
    print("\n2. Logging in...")
    login_data = {
        "username": "admin@example.com",
        "password": "admin123"
    }
    
    try:
        response = requests.post(f"{API_URL}/iam/login/", json=login_data, verify=False)
        if response.status_code == 200:
            print("✓ Logged in successfully")
            token = response.json().get("access")
            headers = {"Authorization": f"Bearer {token}"}
        else:
            print(f"✗ Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            return
    except Exception as e:
        print(f"✗ Login error: {e}")
        return
    
    # Check for frameworks
    print("\n3. Fetching frameworks...")
    try:
        response = requests.get(f"{API_URL}/frameworks/", headers=headers, verify=False)
        if response.status_code == 200:
            frameworks = response.json().get('results', [])
            print(f"✓ Found {len(frameworks)} frameworks")
            
            # Look for HITRUST
            hitrust_found = False
            for framework in frameworks:
                if "HITRUST" in framework.get("name", "") or "hitrust" in framework.get("ref_id", "").lower():
                    hitrust_found = True
                    print(f"\n✓ HITRUST Framework found:")
                    print(f"  - Name: {framework.get('name')}")
                    print(f"  - Ref ID: {framework.get('ref_id')}")
                    print(f"  - Version: {framework.get('version', 'N/A')}")
                    print(f"  - URN: {framework.get('urn')}")
                    print(f"  - ID: {framework.get('id')}")
                    
                    # Get detailed framework info
                    framework_id = framework.get("id")
                    details_response = requests.get(f"{API_URL}/frameworks/{framework_id}/", headers=headers, verify=False)
                    if details_response.status_code == 200:
                        details = details_response.json()
                        
                        # Count controls
                        requirement_nodes = details.get("requirement_nodes", [])
                        print(f"  - Total requirement nodes: {len(requirement_nodes)}")
                        
                        # Count by category
                        categories = {}
                        controls = []
                        for node in requirement_nodes:
                            ref_id = node.get("ref_id", "")
                            if ref_id:
                                if "." not in ref_id and len(ref_id) <= 2:  # Main category
                                    categories[ref_id] = node.get("name", "")
                                else:
                                    controls.append(node)
                        
                        print(f"  - Main categories: {len(categories)}")
                        print(f"  - Sub-controls: {len(controls)}")
                        
                        print("\n  Categories:")
                        for cat_id, cat_name in sorted(categories.items()):
                            # Count subcategory controls
                            cat_controls = [c for c in controls if c.get("ref_id", "").startswith(cat_id + ".")]
                            print(f"    {cat_id}: {cat_name} ({len(cat_controls)} controls)")
                        
                        # Sample some controls
                        print("\n  Sample controls:")
                        for i, control in enumerate(controls[:10]):
                            print(f"    - {control.get('ref_id')}: {control.get('name')}")
                        if len(controls) > 10:
                            print(f"    ... and {len(controls) - 10} more controls")
                        
                        # Check reference controls
                        if "reference_controls" in details:
                            ref_controls = details.get("reference_controls", [])
                            print(f"\n  Reference controls: {len(ref_controls)}")
                            for rc in ref_controls[:5]:
                                print(f"    - {rc.get('ref_id')}: {rc.get('name')}")
                        
                        # Check risk matrix
                        if "risk_matrix" in details:
                            risk_matrix = details.get("risk_matrix")
                            print(f"\n  Risk matrix: {risk_matrix.get('name', 'N/A')}")
                    
            if not hitrust_found:
                print("\n✗ HITRUST framework not found!")
                print("Available frameworks:")
                for framework in frameworks[:10]:
                    print(f"  - {framework.get('name')} ({framework.get('ref_id')})")
                if len(frameworks) > 10:
                    print(f"  ... and {len(frameworks) - 10} more")
        else:
            print(f"✗ Failed to fetch frameworks: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"✗ Error fetching frameworks: {e}")
    
    print("\n" + "="*40)
    print("Test completed")

if __name__ == "__main__":
    test_hitrust_framework()
