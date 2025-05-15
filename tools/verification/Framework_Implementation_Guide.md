# Quick Reference Guide: Implementing Frameworks in CISO Assistant

## File Structure Requirements

### Excel File Structure
Each framework requires an Excel file with specific sheets:

1. **library_content** (required)
   - Contains metadata about the framework
   - Defines which tabs are used and their types

2. **requirements** (for frameworks with controls)
   - Contains the hierarchical control structure
   - Headers: assessable | depth | ref_id | name | description | ...

3. **reference_controls** (optional)
   - Reusable controls that can be referenced
   - Headers: ref_id | name | description | category | ...

4. **scores** (optional)
   - Scoring/maturity levels for the framework
   - Headers: score | name | description

5. **risk_matrix** (optional)
   - Risk assessment matrix
   - Headers: type | id | color | abbreviation | name | description | grid

### YAML File Location
- Converted YAML files must be placed in: `backend/library/libraries/`
- File naming convention: `framework-name-version.yaml`

## Conversion Process

```bash
# Navigate to tools directory
cd /path/to/ciso-assistant-community/tools

# Convert Excel to YAML
python3 convert_library.py path/to/your-framework.xlsx

# Move generated YAML to correct location
mv your-framework.yaml ../backend/library/libraries/
```

## Framework Implementation Checklist

### Phase 1: Planning
- [ ] Obtain official framework documentation
- [ ] Identify all control categories and hierarchies
- [ ] Determine required metadata fields
- [ ] Plan control numbering scheme

### Phase 2: Excel Creation
- [ ] Create Excel file with required sheets
- [ ] Populate library_content with metadata
- [ ] Add all controls to requirements sheet
- [ ] Define scores/maturity levels if applicable
- [ ] Create risk matrix if needed

### Phase 3: Conversion & Testing
- [ ] Run convert_library.py
- [ ] Check for conversion errors
- [ ] Verify YAML structure
- [ ] Test in CISO Assistant application

### Phase 4: Quality Assurance
- [ ] Validate all controls are present
- [ ] Check control descriptions for accuracy
- [ ] Verify hierarchy and relationships
- [ ] Test assessment functionality

## Common Issues & Solutions

### Issue: Missing Controls
**Solution**: Cross-reference with official documentation and add missing items

### Issue: Incorrect Hierarchy
**Solution**: Ensure depth values match the control structure

### Issue: Conversion Errors
**Solution**: Check Excel formatting, ensure no merged cells or special characters

### Issue: Controls Not Displaying
**Solution**: Verify assessable flag is set correctly for leaf nodes

## Best Practices

1. **Version Control**
   - Always include version in framework name
   - Document changes in commit messages

2. **Documentation**
   - Include source documentation references
   - Add notes about any customizations

3. **Testing**
   - Test with sample assessments
   - Verify all controls are accessible
   - Check scoring calculations

4. **Maintenance**
   - Regular updates when frameworks change
   - Keep mapping tables current
   - Document any deviations from official sources

---
*Last Updated: [Current Date]*
