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
    
    # Test API connectivity
    print("\n1. Testing API connectivity...")
    try:
        response = requests.get(f"{API_URL}/build", verify=False)
        if response.status_code == 200:
            print("✓ API is accessible")
        else:
            print(f"✗ API returned status code: {response.status_code}")
            return
    except Exception as e:
        print(f"✗ Failed to connect to API: {e}")
        print("Make sure CISO Assistant is running on https://localhost:8443")
        return
    
    # Login (you'll need to update credentials)
    print("\n2. Logging in...")
    login_data = {
        "username": "admin",  # Update with your username
        "password": "password"  # Update with your password
    }
    
    try:
        response = requests.post(f"{API_URL}/login", json=login_data, verify=False)
        if response.status_code == 200:
            print("✓ Logged in successfully")
            token = response.json().get("access")
            headers = {"Authorization": f"Bearer {token}"}
        else:
            print(f"✗ Login failed: {response.status_code}")
            print("Please update the credentials in the script")
            return
    except Exception as e:
        print(f"✗ Login error: {e}")
        return
    
    # Check for frameworks
    print("\n3. Fetching frameworks...")
    try:
        response = requests.get(f"{API_URL}/frameworks/", headers=headers, verify=False)
        if response.status_code == 200:
            frameworks = response.json()
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
                    
                    # Get detailed framework info
                    framework_id = framework.get("id")
                    details_response = requests.get(f"{API_URL}/frameworks/{framework_id}/", headers=headers, verify=False)
                    if details_response.status_code == 200:
                        details = details_response.json()
                        
                        # Count controls
                        if "requirement_nodes" in details:
                            controls = details["requirement_nodes"]
                            print(f"  - Total controls: {len(controls)}")
                            
                            # Count by category
                            categories = {}
                            for control in controls:
                                ref_id = control.get("ref_id", "")
                                if ref_id and "." not in ref_id:  # Main category
                                    categories[ref_id] = control.get("name", "")
                            
                            print(f"  - Main categories: {len(categories)}")
                            print("\n  Categories:")
                            for cat_id, cat_name in sorted(categories.items()):
                                print(f"    {cat_id}: {cat_name}")
                            
                            # Sample some controls
                            print("\n  Sample controls:")
                            for i, control in enumerate(controls[:5]):
                                print(f"    - {control.get('ref_id')}: {control.get('name')}")
                            if len(controls) > 5:
                                print(f"    ... and {len(controls) - 5} more controls")
                    
            if not hitrust_found:
                print("\n✗ HITRUST framework not found!")
                print("Available frameworks:")
                for framework in frameworks[:5]:
                    print(f"  - {framework.get('name')} ({framework.get('ref_id')})")
                if len(frameworks) > 5:
                    print(f"  ... and {len(frameworks) - 5} more")
        else:
            print(f"✗ Failed to fetch frameworks: {response.status_code}")
    except Exception as e:
        print(f"✗ Error fetching frameworks: {e}")
    
    print("\n" + "="*40)
    print("Test completed")

if __name__ == "__main__":
    # Wait a moment for the server to be ready if just started
    print("Waiting for server to be ready...")
    time.sleep(5)
    test_hitrust_framework()
