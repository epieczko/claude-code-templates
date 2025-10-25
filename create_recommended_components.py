#!/usr/bin/env python3
"""
Create filtered JSON files with only recommended components for Betty migration.
"""

import json

def create_filtered_json():
    """Create separate JSON files for each component type with recommended items."""

    # Load the full analysis
    with open('components_analysis.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    analysis = data['analysis']
    recommendations = data['recommendations']
    statistics = data['statistics']

    # ==================== HOOKS ====================
    hooks_recommended = (
        recommendations['hooks']['highly_recommended'] +
        recommendations['hooks']['recommended']
    )

    hooks_output = {
        'total_hooks': len(hooks_recommended),
        'source': 'claude-code-templates repository',
        'migration_status': 'recommended_for_betty',
        'categories': {
            'highly_recommended': len(recommendations['hooks']['highly_recommended']),
            'recommended': len(recommendations['hooks']['recommended'])
        },
        'hooks': hooks_recommended
    }

    with open('hooks_recommended_for_betty.json', 'w', encoding='utf-8') as f:
        json.dump(hooks_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Created hooks_recommended_for_betty.json ({len(hooks_recommended)} hooks)")

    # ==================== COMMANDS ====================
    commands_recommended = (
        recommendations['commands']['highly_recommended'] +
        recommendations['commands']['recommended']
    )

    commands_output = {
        'total_commands': len(commands_recommended),
        'source': 'claude-code-templates repository',
        'migration_status': 'recommended_for_betty',
        'categories': {
            'highly_recommended': len(recommendations['commands']['highly_recommended']),
            'recommended': len(recommendations['commands']['recommended'])
        },
        'commands': commands_recommended
    }

    with open('commands_recommended_for_betty.json', 'w', encoding='utf-8') as f:
        json.dump(commands_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Created commands_recommended_for_betty.json ({len(commands_recommended)} commands)")

    # ==================== SKILLS ====================
    skills_recommended = (
        recommendations['skills']['highly_recommended'] +
        recommendations['skills']['recommended']
    )

    skills_output = {
        'total_skills': len(skills_recommended),
        'source': 'claude-code-templates repository',
        'migration_status': 'recommended_for_betty',
        'categories': {
            'highly_recommended': len(recommendations['skills']['highly_recommended']),
            'recommended': len(recommendations['skills']['recommended'])
        },
        'skills': skills_recommended
    }

    with open('skills_recommended_for_betty.json', 'w', encoding='utf-8') as f:
        json.dump(skills_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Created skills_recommended_for_betty.json ({len(skills_recommended)} skills)")

    # ==================== MCPS ====================
    mcps_recommended = (
        recommendations['mcps']['highly_recommended'] +
        recommendations['mcps']['recommended']
    )

    mcps_output = {
        'total_mcps': len(mcps_recommended),
        'source': 'claude-code-templates repository',
        'migration_status': 'recommended_for_betty',
        'categories': {
            'highly_recommended': len(recommendations['mcps']['highly_recommended']),
            'recommended': len(recommendations['mcps']['recommended'])
        },
        'mcps': mcps_recommended
    }

    with open('mcps_recommended_for_betty.json', 'w', encoding='utf-8') as f:
        json.dump(mcps_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Created mcps_recommended_for_betty.json ({len(mcps_recommended)} MCPs)")

    # ==================== SUMMARY ====================
    print("\n" + "=" * 80)
    print("FILTERED JSON FILES CREATED")
    print("=" * 80)

    total_recommended = (
        len(hooks_recommended) +
        len(commands_recommended) +
        len(skills_recommended) +
        len(mcps_recommended)
    )

    print(f"\n📊 Total recommended components: {total_recommended}")
    print(f"\n  - Hooks: {len(hooks_recommended)}")
    print(f"  - Commands: {len(commands_recommended)}")
    print(f"  - Skills: {len(skills_recommended)}")
    print(f"  - MCPs: {len(mcps_recommended)}")

    # Show category breakdowns
    print("\n\nCategory breakdowns:")

    # Hooks by category
    print("\n  HOOKS:")
    hooks_by_cat = {}
    for hook in hooks_recommended:
        cat = hook['category']
        hooks_by_cat[cat] = hooks_by_cat.get(cat, 0) + 1
    for cat in sorted(hooks_by_cat.keys()):
        print(f"    - {cat}: {hooks_by_cat[cat]}")

    # Commands by category (top 10)
    print("\n  COMMANDS (top 10 categories):")
    commands_by_cat = {}
    for cmd in commands_recommended:
        cat = cmd['category']
        commands_by_cat[cat] = commands_by_cat.get(cat, 0) + 1
    sorted_cats = sorted(commands_by_cat.items(), key=lambda x: x[1], reverse=True)[:10]
    for cat, count in sorted_cats:
        print(f"    - {cat}: {count}")

    # Skills by category
    print("\n  SKILLS:")
    skills_by_cat = {}
    for skill in skills_recommended:
        cat = skill['category']
        skills_by_cat[cat] = skills_by_cat.get(cat, 0) + 1
    for cat in sorted(skills_by_cat.keys()):
        print(f"    - {cat}: {skills_by_cat[cat]}")

    # MCPs by category
    print("\n  MCPS:")
    mcps_by_cat = {}
    for mcp in mcps_recommended:
        cat = mcp['category']
        mcps_by_cat[cat] = mcps_by_cat.get(cat, 0) + 1
    for cat in sorted(mcps_by_cat.keys()):
        print(f"    - {cat}: {mcps_by_cat[cat]}")

if __name__ == '__main__':
    create_filtered_json()
