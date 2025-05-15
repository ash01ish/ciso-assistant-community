# CISO Assistant Demo Guide

This guide outlines how to set up and demonstrate the key features of CISO Assistant, focusing on compliance management for frameworks like SOC 2 Type 2, HITRUST, HIPAA, and ISO 27001.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Setting Up Compliance Assessments](#setting-up-compliance-assessments)
3. [Working with Controls](#working-with-controls)
4. [Evidence Management](#evidence-management)
5. [Reporting and Dashboards](#reporting-and-dashboards)
6. [Advanced Features](#advanced-features)

## Getting Started

### Login and Dashboard Overview

1. Access CISO Assistant at `https://localhost:8443`
2. Login with credentials:
   - Username: `admin@pestle.in`
   - Password: `admin123`

### System Navigation

- **Left Sidebar**: Access main modules (Compliance, Risk, Assets, etc.)
- **Top Bar**: Search, notifications, and user settings
- **Main Area**: Content and working area

## Setting Up Compliance Assessments

CISO Assistant supports multiple compliance frameworks. Here's how to set up assessments for key standards:

### Creating a SOC 2 Type 2 Assessment

1. Navigate to **Compliance > Assessments**
2. Click **+ New Assessment**
3. Fill in the form:
   - **Name**: `SOC 2 Type 2 Assessment 2025`
   - **Framework**: Select `AICPA - SOC2-2017 Trust Services Criteria (revision 2022)`
   - **Perimeter**: Select your business scope or create a new one
   - **Status**: `In Progress`
   - **Due Date**: Set 6 months from current date
   - **Description**: `SOC 2 Type 2 audit covering Security, Availability, and Confidentiality trust service criteria`
4. Click **Create**

### Creating a HITRUST CSF Assessment

1. Navigate to **Compliance > Assessments**
2. Click **+ New Assessment**
3. Fill in the form:
   - **Name**: `HITRUST CSF v11 Certification`
   - **Framework**: Select `HITRUST Alliance - HITRUST CSF v11`
   - **Perimeter**: Select your business scope
   - **Implementation Groups**: Select all that apply (IG1, IG2, IG3)
   - **Status**: `In Progress`
   - **Due Date**: Set 8 months from current date
   - **Description**: `HITRUST CSF v11 certification covering all 14 control domains`
4. Click **Create**

### Creating a HIPAA Assessment

1. Navigate to **Compliance > Assessments**
2. Click **+ New Assessment**
3. Fill in the form:
   - **Name**: `HIPAA Compliance Assessment`
   - **Framework**: Search for and select `HHS - HIPAA Security Rule`
   - **Perimeter**: Select your healthcare-related perimeter
   - **Status**: `In Progress`
   - **Due Date**: Set 3 months from current date
   - **Description**: `HIPAA Security Rule compliance assessment for healthcare operations`
4. Click **Create**

### Creating an ISO 27001 Assessment

1. Navigate to **Compliance > Assessments**
2. Click **+ New Assessment**
3. Fill in the form:
   - **Name**: `ISO 27001:2022 Certification`
   - **Framework**: Select `ISO/IEC - International standard ISO/IEC 27001:2022`
   - **Perimeter**: Select organization-wide perimeter
   - **Implementation Groups**: Select `Clauses` and `Statement of Applicability`
   - **Status**: `In Progress`
   - **Due Date**: Set 10 months from current date
   - **Description**: `ISO 27001:2022 certification covering all controls in Annex A`
4. Click **Create**

## Working with Controls

### Viewing and Assessing Controls

1. Open any compliance assessment (e.g., SOC 2 Type 2)
2. Navigate to the **Requirements** tab
3. You'll see the hierarchical structure of control domains and requirements
4. Click on any requirement (e.g., `CC1.1 - COSO Principle 1`) to expand its details

### Updating Control Status

1. Click on a specific requirement (e.g., `CC1.1.1: Sets the Tone at the Top`)
2. In the right panel, update the following:
   - **Status**: Choose from `Not Applicable`, `Not Implemented`, `Partially Implemented`, `Implemented`
   - **Score**: Assign a score based on maturity (typically 1-5)
   - **Documentation Score**: Rate the quality of documentation
   - **Notes**: Add implementation notes or observations
2. Click **Save** to update the control status

### Linking Controls to Evidence

1. While viewing a control requirement
2. Scroll to the **Evidence** section
3. Click **+ Add Evidence Link**
4. Select from existing evidence or upload new evidence
5. Add description explaining how the evidence supports the control
6. Click **Save**

### Bulk Control Updates

1. From the requirements list, select multiple controls using checkboxes
2. Click the **Bulk Update** button at the top
3. Update status, scores, or other attributes for all selected controls
4. Click **Apply** to save changes

## Evidence Management

### Adding Evidence

1. Navigate to **Compliance > Evidence**
2. Click **+ New Evidence**
3. Fill in the form:
   - **Name**: Clear name describing the evidence (e.g., `Access Control Policy v2.3`)
   - **Type**: Select from `Document`, `Screenshot`, `Configuration`, etc.
   - **Description**: Add details about what the evidence demonstrates
   - **Upload**: Attach the evidence file (PDF, image, etc.)
4. Click **Save**

### Reusing Evidence Across Assessments

1. Navigate to a different compliance assessment (e.g., ISO 27001)
2. Find a relevant control
3. Link to existing evidence from the evidence library
4. Add a note explaining how it applies to this specific control

## Reporting and Dashboards

### Generating Compliance Reports

1. Navigate to the assessment's main page
2. Click the **Reports** button
3. Select the report type:
   - **Executive Summary**: High-level overview with charts
   - **Detailed Assessment**: Complete control-by-control report
   - **Gap Analysis**: Focusing on controls not yet fully implemented
4. Click **Generate Report**
5. Download in PDF or export to other formats

### Viewing Dashboards

1. Navigate to **Dashboards** from the main menu
2. View key metrics across all assessments:
   - Overall compliance progress by framework
   - Controls by status (implemented, partial, not implemented)
   - Upcoming assessment deadlines
   - Recent control updates
   - Evidence coverage gaps

## Advanced Features

### Mappings Between Frameworks

1. Navigate to **Compliance > Framework Mappings**
2. Select source and target frameworks (e.g., HITRUST CSF to SOC 2)
3. View how controls map between frameworks
4. Use this to leverage work done for one framework when addressing another

### Risk Integration

1. Navigate to **Risk > Risk Assessments**
2. Create or view risk scenarios
3. Link compliance control weaknesses to risks
4. Demonstrate how compliance and risk management work together

### Applied Controls

1. Navigate to **Controls > Applied Controls**
2. View organization-specific controls implemented across systems
3. Link applied controls to compliance requirements
4. Update implementation status and track progress

## Demo Scenarios

Here are some effective demo scenarios to showcase CISO Assistant capabilities:

### Scenario 1: Compliance Readiness Assessment

1. Show SOC 2 assessment overview
2. Highlight control gaps and implementation status
3. Demonstrate how to update control status
4. Generate readiness report showing progress and remaining work

### Scenario 2: Evidence Management Workflow

1. Upload a new security policy document as evidence
2. Link it to multiple controls across different frameworks
3. Show how a single evidence item can satisfy requirements in SOC 2, HITRUST, and ISO 27001
4. Demonstrate the time-saving aspects of cross-framework evidence mapping

### Scenario 3: Audit Preparation

1. Show how to export assessment reports for auditors
2. Demonstrate the evidence traceability from requirement to supporting documentation
3. Highlight how easy it is for auditors to verify compliance with clear documentation

### Scenario 4: Multi-Framework Management

1. Show dashboard with progress across all frameworks
2. Demonstrate how work on one framework (e.g., HITRUST) helps with another (e.g., SOC 2)
3. Highlight efficiency gains from the integrated approach

## Tips for an Effective Demo

1. **Prepare Sample Data**: Ensure you have realistic data including policies, screenshots, and configurations as evidence
2. **Focus on Workflows**: Rather than features, show complete workflows from start to finish
3. **Highlight Pain Points**: Address common compliance challenges and how CISO Assistant solves them
4. **Tell a Story**: Create a narrative around preparing for a specific audit or certification
5. **Show Time Savings**: Emphasize how the platform reduces manual work and spreadsheet management

---

This guide covers the essentials for demonstrating CISO Assistant's capabilities for managing multiple compliance frameworks. Customize the demo based on the specific interests and needs of your audience.