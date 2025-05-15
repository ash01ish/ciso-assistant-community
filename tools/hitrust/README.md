# HITRUST CSF v11 Framework Implementation

This directory contains the complete implementation of the HITRUST Common Security Framework (CSF) version 11 for CISO Assistant.

## Files

- `HITRUST_CSF_v11_Complete.xlsx` - The comprehensive Excel file containing all HITRUST CSF v11 controls, reference controls, implementation groups, and risk matrix
- `create_complete_hitrust_excel.py` - Python script to generate the HITRUST Excel file
- `README.md` - This documentation file

## Framework Structure

The HITRUST CSF v11 framework includes:

- **14 Control Categories** (00-13):
  - 00: Information Security Management Program
  - 01: Access Control
  - 02: Human Resources Security
  - 03: Risk Management
  - 04: Asset Management
  - 05: Physical and Environmental Security
  - 06: Communications and Operations Management
  - 07: System Development and Maintenance
  - 08: Information Security Incident Management
  - 09: Business Continuity Management
  - 10: Compliance
  - 11: Mobile Security
  - 12: Supplier Relationships
  - 13: Cloud Security

- **142 Individual Controls** with detailed requirements and evidence
- **16 Reference Controls** (RC-01 through RC-16)
- **3 Implementation Groups** (IG1, IG2, IG3)
- **5x5 Risk Matrix** with probability and impact levels
- **5 Maturity Levels** for scoring

## Generation Process

The framework is generated following the CISO Assistant repository pattern:

1. Run the Python script to create the Excel file:
   ```bash
   cd /path/to/tools/hitrust
   python3 create_complete_hitrust_excel.py
   ```

2. Convert Excel to YAML using the repository's create_library.py:
   ```bash
   cd /path/to/tools
   python3 create_library.py hitrust/HITRUST_CSF_v11_Complete.xlsx
   ```

3. Move the generated YAML to the backend libraries:
   ```bash
   mv hitrust/HITRUST_CSF_v11_Complete.yaml ../backend/library/libraries/hitrust-csf-v11.yaml
   ```

## Features

- Complete control families with parent-child relationships
- Assessable controls with implementation groups
- Typical evidence for each control
- Risk matrix with color-coded risk levels
- Reference controls for grouping related requirements
- Maturity scoring from Policy (1) to Managed (5)

## Maintenance

To update the framework:
1. Modify the `create_complete_hitrust_excel.py` script
2. Regenerate the Excel file
3. Convert to YAML
4. Replace the library file in the backend

## Version

- HITRUST CSF Version: 11
- Implementation Date: May 2025
- Provider: HITRUST Alliance
- Packager: intuitem
