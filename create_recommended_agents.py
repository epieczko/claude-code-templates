#!/usr/bin/env python3
"""
Create a JSON file with only the 87 recommended agents for Betty migration.
"""

import json

def main():
    # Load the analysis with recommendations
    with open('agents_analysis.json', 'r', encoding='utf-8') as f:
        analysis_data = json.load(f)

    # Load the full agent export
    with open('agents_export.json', 'r', encoding='utf-8') as f:
        full_export = json.load(f)

    # Get the recommended agent names
    recommended_names = set()

    # Add highly recommended
    for agent in analysis_data['recommendations']['highly_recommended']:
        recommended_names.add(agent['name'])

    # Add recommended
    for agent in analysis_data['recommendations']['recommended']:
        recommended_names.add(agent['name'])

    # Filter the full export to only include recommended agents
    recommended_agents = []
    for agent in full_export['agents']:
        if agent['name'] in recommended_names:
            recommended_agents.append(agent)

    # Create the output
    output = {
        'total_agents': len(recommended_agents),
        'source': 'claude-code-templates repository',
        'migration_status': 'recommended_for_betty',
        'categories': {
            'highly_recommended': len(analysis_data['recommendations']['highly_recommended']),
            'recommended': len(analysis_data['recommendations']['recommended'])
        },
        'agents': recommended_agents
    }

    # Write the JSON file
    with open('agents_recommended_for_betty.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Created agents_recommended_for_betty.json")
    print(f"📊 Total agents: {len(recommended_agents)}")
    print(f"   - Highly recommended: {output['categories']['highly_recommended']}")
    print(f"   - Recommended: {output['categories']['recommended']}")

    # Show breakdown by category
    categories_count = {}
    for agent in recommended_agents:
        cat = agent['category']
        categories_count[cat] = categories_count.get(cat, 0) + 1

    print("\n📁 Breakdown by category:")
    for category in sorted(categories_count.keys()):
        print(f"   - {category}: {categories_count[category]} agents")

if __name__ == '__main__':
    main()
