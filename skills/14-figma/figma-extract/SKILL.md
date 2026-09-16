---
name: figma-extract
description: Standardizes extraction and documentation of design tokens, assets, and specs from Figma. Use when the user asks to export from Figma, extract design tokens, get color palettes, document a design system, export SVGs, or prepare Figma designs for development.
---

# Figma Export Skill

## Purpose
Standardize how design tokens, assets, and specifications are extracted from Figma for development handoff or documentation.

## Prerequisites
- Figma MCP must be connected and working
- User should have a Figma file open with relevant elements selected
- Confirm Figma desktop app is running before attempting any MCP calls

## Instructions

### Step 1: Confirm Setup
Before extracting anything:
1. Check Figma MCP is connected
2. Ask user to select the relevant element/frame in Figma
3. Confirm what they want to extract

Ask: "What would you like to export? Options include:
- Design tokens (colors, typography, spacing)
- Component specs (for building in code)
- Asset list (SVGs, images)
- Full design documentation"

### Step 2: Use Appropriate MCP Tool

| Goal | MCP Tool | Output |
|------|----------|--------|
| Get design tokens | `get_variable_defs` | Colors, typography, spacing values |
| Get code specs | `get_design_context` | Component structure, styles |
| Visual reference | `get_screenshot` | Image of selection |
| Layer structure | `get_metadata` | XML hierarchy of layers |

### Step 3: Format Output by Type

---

## Output Formats

### Design Tokens → CSS Variables
```css
:root {
  /* Colors - Primary */
  --color-primary: #675ACD;
  --color-primary-hover: #5449B3;
  
  /* Colors - Text */
  --color-text-primary: #000000;
  --color-text-secondary: #6B7280;
  
  /* Colors - Background */
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F3F4F6;
  
  /* Typography */
  --font-family-base: 'FK Grotesk', sans-serif;
  --font-size-sm: 12px;
  --font-size-base: 16px;
  --font-size-lg: 20px;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
}
```

### Design Tokens → Tailwind Config
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#675ACD',
        'primary-hover': '#5449B3',
        // ... more colors
      },
      fontFamily: {
        base: ['FK Grotesk', 'sans-serif'],
      },
      fontSize: {
        sm: '12px',
        base: '16px',
        lg: '20px',
      },
      spacing: {
        xs: '4px',
        sm: '8px',
        md: '16px',
        lg: '24px',
        xl: '32px',
      },
    },
  },
}
```

### Design Tokens → JSON (for tooling)
```json
{
  "colors": {
    "primary": {
      "value": "#675ACD",
      "type": "color"
    },
    "text": {
      "primary": {
        "value": "#000000",
        "type": "color"
      }
    }
  },
  "typography": {
    "fontFamily": {
      "base": {
        "value": "FK Grotesk",
        "type": "fontFamily"
      }
    }
  }
}
```

### Component Documentation
```markdown
# Component: [Name]

## Visual Reference
[Screenshot from Figma]

## Specifications

### Dimensions
- Width: [value] / [responsive behavior]
- Height: [value] / [auto/fixed]
- Padding: [top] [right] [bottom] [left]
- Border radius: [value]

### Typography
- Font: [family]
- Size: [size]
- Weight: [weight]
- Line height: [value]
- Color: [hex] (token: --color-text-primary)

### Colors
- Background: [hex] (token: --color-bg-card)
- Border: [hex] or none
- Shadow: [value] or none

### States
- Default: [description]
- Hover: [changes]
- Active: [changes]
- Disabled: [changes]

### Variants
- [Variant name]: [differences from default]

## Usage Notes
[Any context from the designer]
```

---

## Workflow Examples

### "Export design tokens"
1. Ask user to select a component or frame with their design system
2. Call `get_variable_defs` 
3. Ask preferred format: CSS, Tailwind, JSON, or SCSS
4. Format and output tokens
5. Offer to save as file

### "Document this component"
1. Ask user to select the component in Figma
2. Call `get_screenshot` for visual reference
3. Call `get_design_context` for specs
4. Call `get_variable_defs` for any tokens used
5. Compile into component documentation markdown
6. Offer to save as file

### "Prepare for development handoff"
1. Get screenshot of full design
2. Extract all tokens
3. Document each unique component
4. List all assets that need export
5. Create handoff document with everything

---

## Limitations to Communicate

Be upfront with users:
- **Cannot write to Figma** — extraction only
- **Cannot export actual SVG files** — can only identify what needs export
- **Complex components may need manual review** — especially nested or variant-heavy ones
- **Tokens depend on Figma setup** — if designer didn't use variables, extraction is limited

## What NOT to Do
- Don't assume token structure—extract what's actually there
- Don't skip the visual screenshot—developers need reference
- Don't export without confirming format preference
- Don't proceed if MCP connection fails—troubleshoot first

## Troubleshooting

### MCP not connected
"Figma MCP isn't responding. Please check:
1. Is Figma desktop app open?
2. Is MCP enabled in Figma preferences?
3. Try restarting Figma"

### No tokens found
"No design variables found in this selection. This might mean:
- The design doesn't use Figma variables
- Try selecting a different frame
- Tokens may need to be manually documented"
