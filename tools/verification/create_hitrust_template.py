#!/usr/bin/env python3
"""
Create HITRUST CSF Framework Excel Template for CISO Assistant
Based on HITRUST CSF v11 structure
"""

# Note: This script creates a template structure. 
# You will need to manually populate it with actual HITRUST controls
# or use the official HITRUST documentation to fill in the details.

def create_hitrust_template():
    """Create HITRUST Excel template structure"""
    
    print("=== HITRUST CSF FRAMEWORK TEMPLATE ===")
    print("\nThis script will create the Excel file structure needed")
    print("for HITRUST CSF framework in CISO Assistant format.\n")
    
    # Define the Excel structure based on convert_library.py conventions
    template_structure = {
        "library_content": {
            "library_urn": "urn:intuitem:risk:library:hitrust-csf-v11",
            "library_version": "11.0",
            "library_locale": "en",
            "library_ref_id": "HITRUST-CSF-v11",
            "library_name": "HITRUST CSF v11",
            "library_description": "HITRUST Common Security Framework (CSF) version 11 provides prescriptive security, privacy and regulatory compliance requirements",
            "library_copyright": "© 2024 HITRUST Alliance",
            "library_provider": "HITRUST Alliance",
            "library_packager": "intuitem",
            "framework_urn": "urn:intuitem:risk:framework:hitrust-csf-v11",
            "framework_ref_id": "HITRUST-CSF-v11",
            "framework_name": "HITRUST CSF v11",
            "framework_description": "HITRUST Common Security Framework version 11",
            "reference_control_base_urn": "urn:intuitem:risk:reference_control:hitrust-csf-v11",
            "threat_base_urn": "urn:intuitem:risk:threat:hitrust-csf-v11",
            "tab": {
                "requirements": "requirements",
                "reference_controls": "reference_controls",
                "threats": "threats",
                "scores": "scores",
                "implementation_groups": "implementation_groups",
                "risk_matrix": "risk_matrix"
            }
        },
        
        "requirements_headers": [
            "assessable",
            "depth", 
            "ref_id",
            "name",
            "description",
            "threats",
            "reference_controls",
            "annotation",
            "typical_evidence",
            "questions"
        ],
        
        "reference_controls_headers": [
            "ref_id",
            "name",
            "description",
            "category",
            "csf_function",
            "annotation"
        ],
        
        "scores_headers": [
            "score",
            "name", 
            "description"
        ],
        
        "implementation_groups_headers": [
            "ref_id",
            "name",
            "description"
        ],
        
        "threats_headers": [
            "ref_id",
            "name",
            "description",
            "annotation"
        ],
        
        "risk_matrix_headers": [
            "type",
            "id",
            "color",
            "abbreviation",
            "name",
            "description",
            "grid"
        ]
    }
    
    # HITRUST Control Categories
    control_categories = [
        {"id": "01", "name": "Information Security Management Program"},
        {"id": "02", "name": "Organizational"},
        {"id": "03", "name": "Human Resources Security"},
        {"id": "04", "name": "Asset Management"},
        {"id": "05", "name": "Access Control"},
        {"id": "06", "name": "Cryptography"},
        {"id": "07", "name": "Physical and Environmental Security"},
        {"id": "08", "name": "Operations Security"},
        {"id": "09", "name": "Communications Security"},
        {"id": "10", "name": "System Development and Maintenance"},
        {"id": "11", "name": "Supplier Relationships"},
        {"id": "12", "name": "Information Security Incident Management"},
        {"id": "13", "name": "Business Continuity Management"},
        {"id": "14", "name": "Compliance"}
    ]
    
    # Implementation levels for HITRUST
    implementation_levels = [
        {"score": 1, "name": "Policy", "description": "Policy established"},
        {"score": 2, "name": "Procedure", "description": "Procedure documented and implemented"},
        {"score": 3, "name": "Implemented", "description": "Control implemented"},
        {"score": 4, "name": "Tested", "description": "Control tested"},
        {"score": 5, "name": "Managed", "description": "Control managed and monitored"}
    ]
    
    # Risk matrix for HITRUST (simplified)
    risk_matrix = {
        "probability": [
            {"id": 0, "abbreviation": "VL", "name": "Very Low", "description": "Probability < 10%"},
            {"id": 1, "abbreviation": "L", "name": "Low", "description": "Probability 10-35%"},
            {"id": 2, "abbreviation": "M", "name": "Medium", "description": "Probability 35-65%"},
            {"id": 3, "abbreviation": "H", "name": "High", "description": "Probability 65-90%"},
            {"id": 4, "abbreviation": "VH", "name": "Very High", "description": "Probability > 90%"}
        ],
        "impact": [
            {"id": 0, "abbreviation": "VL", "name": "Very Low", "description": "Minimal impact"},
            {"id": 1, "abbreviation": "L", "name": "Low", "description": "Minor impact"},
            {"id": 2, "abbreviation": "M", "name": "Medium", "description": "Moderate impact"},
            {"id": 3, "abbreviation": "H", "name": "High", "description": "Major impact"},
            {"id": 4, "abbreviation": "VH", "name": "Very High", "description": "Severe impact"}
        ],
        "risk": [
            {"id": 0, "abbreviation": "VL", "name": "Very Low", "description": "Minimal risk"},
            {"id": 1, "abbreviation": "L", "name": "Low", "description": "Low risk"},
            {"id": 2, "abbreviation": "M", "name": "Medium", "description": "Medium risk"},
            {"id": 3, "abbreviation": "H", "name": "High", "description": "High risk"},
            {"id": 4, "abbreviation": "VH", "name": "Very High", "description": "Critical risk"}
        ]
    }
    
    print("Template structure created. To complete the HITRUST framework:")
    print("\n1. Create an Excel file with the following sheets:")
    print("   - library_content")
    print("   - requirements")
    print("   - reference_controls")
    print("   - scores")
    print("   - implementation_groups")
    print("   - risk_matrix")
    print("   - threats (optional)")
    
    print("\n2. For the 'library_content' sheet, create rows with:")
    for key, value in template_structure["library_content"].items():
        if key != "tab":
            print(f"   - {key} | {value}")
    
    print("\n3. For tabs configuration in library_content:")
    for tab_name, tab_type in template_structure["library_content"]["tab"].items():
        print(f"   - tab | {tab_name} | {tab_type}")
    
    print("\n4. For the 'requirements' sheet:")
    print("   Headers:", " | ".join(template_structure["requirements_headers"]))
    print("   Add controls with structure:")
    for cat in control_categories:
        print(f"   - Category {cat['id']}: {cat['name']}")
        print(f"     Example: {cat['id']}.1, {cat['id']}.1.1, {cat['id']}.1.2, etc.")
    
    print("\n5. For the 'reference_controls' sheet:")
    print("   Headers:", " | ".join(template_structure["reference_controls_headers"]))
    
    print("\n6. For the 'scores' sheet:")
    print("   Headers:", " | ".join(template_structure["scores_headers"]))
    print("   Implementation levels:")
    for level in implementation_levels:
        print(f"   - {level['score']} | {level['name']} | {level['description']}")
    
    print("\n7. For the 'risk_matrix' sheet:")
    print("   Headers:", " | ".join(template_structure["risk_matrix_headers"]))
    print("   Add probability, impact, and risk levels as defined")
    
    print("\n8. Once Excel file is complete, convert to YAML using:")
    print("   python3 convert_library.py hitrust/HITRUST_CSF_v11.xlsx")
    
    return template_structure


def create_sample_controls():
    """Generate sample HITRUST control structure"""
    
    sample_controls = []
    
    # Sample control structure for HITRUST
    control_examples = [
        {
            "assessable": "x",
            "depth": 1,
            "ref_id": "01",
            "name": "Information Security Management Program",
            "description": "Controls related to establishing and maintaining an information security management program"
        },
        {
            "assessable": "x", 
            "depth": 2,
            "ref_id": "01.1",
            "name": "Security Policy",
            "description": "Information security policy and procedures"
        },
        {
            "assessable": "x",
            "depth": 3,
            "ref_id": "01.1.a",
            "name": "Policy Development",
            "description": "The organization develops, documents, and implements an information security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance."
        },
        {
            "assessable": "x",
            "depth": 3,
            "ref_id": "01.1.b",
            "name": "Policy Review",
            "description": "The organization reviews and updates the information security policy at least annually or when significant changes occur."
        }
    ]
    
    return control_examples


if __name__ == "__main__":
    template = create_hitrust_template()
    
    print("\n" + "="*50)
    print("SAMPLE CONTROL STRUCTURE")
    print("="*50)
    
    sample_controls = create_sample_controls()
    print("\nExample of how controls should be structured:")
    print("assessable | depth | ref_id | name | description")
    print("-"*50)
    
    for control in sample_controls:
        print(f"{control['assessable']} | {control['depth']} | {control['ref_id']} | {control['name']} | {control['description'][:50]}...")
    
    print("\n" + "="*50)
    print("NEXT STEPS")
    print("="*50)
    print("\n1. Create Excel file: HITRUST_CSF_v11.xlsx")
    print("2. Add all HITRUST controls following the structure above")
    print("3. Convert to YAML using convert_library.py")
    print("4. Place YAML file in backend/library/libraries/")
    print("5. Test in CISO Assistant application")
