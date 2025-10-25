#!/usr/bin/env python3
"""
Extract all agents from the repository with their descriptions.
Creates a structured output for Claude Code template migration.
"""

import os
import json
import re
from pathlib import Path

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---'
    match = re.search(frontmatter_pattern, content, re.DOTALL)

    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter

def get_agent_content(file_path):
    """Get the full content after frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    return content.strip()

def extract_agents():
    """Extract all agents from the repository."""
    agents_dir = Path('cli-tool/components/agents')
    agents = []

    # Find all .md files
    for agent_file in sorted(agents_dir.rglob('*.md')):
        with open(agent_file, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = extract_frontmatter(content)
        agent_content = get_agent_content(agent_file)

        # Get relative path from agents directory
        rel_path = agent_file.relative_to(agents_dir)
        category = str(rel_path.parent) if rel_path.parent != Path('.') else 'uncategorized'

        agent_data = {
            'name': frontmatter.get('name', agent_file.stem),
            'description': frontmatter.get('description', ''),
            'category': category,
            'tools': frontmatter.get('tools', ''),
            'model': frontmatter.get('model', ''),
            'file_path': str(agent_file),
            'content': agent_content
        }

        agents.append(agent_data)

    return agents

def create_json_output(agents):
    """Create JSON output file."""
    output = {
        'total_agents': len(agents),
        'agents': agents
    }

    with open('agents_export.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Created agents_export.json with {len(agents)} agents")

def create_markdown_output(agents):
    """Create markdown output file."""
    # Group by category
    categories = {}
    for agent in agents:
        cat = agent['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(agent)

    with open('agents_export.md', 'w', encoding='utf-8') as f:
        f.write('# Claude Code Agents Export\n\n')
        f.write(f'Total agents: {len(agents)}\n\n')
        f.write('## Table of Contents\n\n')

        for category in sorted(categories.keys()):
            f.write(f'- [{category}](#{category.replace("/", "-")})\n')

        f.write('\n---\n\n')

        for category in sorted(categories.keys()):
            f.write(f'## {category}\n\n')

            for agent in sorted(categories[category], key=lambda x: x['name']):
                f.write(f'### {agent["name"]}\n\n')
                f.write(f'**Description:** {agent["description"]}\n\n')
                if agent['tools']:
                    f.write(f'**Tools:** {agent["tools"]}\n\n')
                if agent['model']:
                    f.write(f'**Model:** {agent["model"]}\n\n')
                f.write(f'**File:** `{agent["file_path"]}`\n\n')
                f.write('---\n\n')

    print(f"Created agents_export.md with {len(agents)} agents")

def create_claude_template(agents):
    """Create a Claude Code template format for easy migration."""
    # Group by category
    categories = {}
    for agent in agents:
        cat = agent['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(agent)

    with open('agents_claude_template.md', 'w', encoding='utf-8') as f:
        f.write('# Claude Code Agents - Migration Template\n\n')
        f.write(f'This document contains {len(agents)} agents ready for migration to Betty repo.\n\n')
        f.write('## Instructions\n\n')
        f.write('Use the meta.agent task to import these agents into your Betty repository.\n\n')
        f.write('### Quick Reference\n\n')
        f.write('```bash\n')
        f.write('# Example: Create a single agent\n')
        f.write('# Copy the agent content below and use meta.agent to create it\n')
        f.write('```\n\n')
        f.write('---\n\n')

        for category in sorted(categories.keys()):
            f.write(f'## Category: {category}\n\n')
            f.write(f'Total agents in this category: {len(categories[category])}\n\n')

            for agent in sorted(categories[category], key=lambda x: x['name']):
                f.write(f'### Agent: {agent["name"]}\n\n')
                f.write(f'**Description:** {agent["description"]}\n\n')

                if agent['tools']:
                    f.write(f'**Tools:** {agent["tools"]}\n')
                if agent['model']:
                    f.write(f'**Model:** {agent["model"]}\n')

                f.write('\n**Full Agent Definition:**\n\n')
                f.write('```markdown\n')
                f.write('---\n')
                f.write(f'name: {agent["name"]}\n')
                f.write(f'description: {agent["description"]}\n')
                if agent['tools']:
                    f.write(f'tools: {agent["tools"]}\n')
                if agent['model']:
                    f.write(f'model: {agent["model"]}\n')
                f.write('---\n\n')
                f.write(agent["content"])
                f.write('\n```\n\n')
                f.write('---\n\n')

    print(f"Created agents_claude_template.md with {len(agents)} agents in template format")

def create_simple_list(agents):
    """Create a simple list of agents with descriptions."""
    with open('agents_list.txt', 'w', encoding='utf-8') as f:
        f.write('CLAUDE CODE AGENTS LIST\n')
        f.write('=' * 80 + '\n\n')
        f.write(f'Total Agents: {len(agents)}\n\n')

        for i, agent in enumerate(agents, 1):
            f.write(f'{i}. {agent["name"]}\n')
            f.write(f'   Category: {agent["category"]}\n')
            f.write(f'   Description: {agent["description"]}\n')
            f.write(f'   File: {agent["file_path"]}\n')
            f.write('\n')

    print(f"Created agents_list.txt with {len(agents)} agents")

def main():
    print("Extracting agents from repository...")
    agents = extract_agents()

    print(f"\nFound {len(agents)} agents")

    # Create different output formats
    create_json_output(agents)
    create_markdown_output(agents)
    create_claude_template(agents)
    create_simple_list(agents)

    print("\n✓ All export files created successfully!")
    print("\nFiles created:")
    print("  - agents_export.json (structured JSON data)")
    print("  - agents_export.md (formatted markdown reference)")
    print("  - agents_claude_template.md (ready for meta.agent migration)")
    print("  - agents_list.txt (simple text list)")

    # Print some statistics
    categories = {}
    for agent in agents:
        cat = agent['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n\nAgents by category:")
    for category in sorted(categories.keys()):
        print(f"  - {category}: {categories[category]} agents")

if __name__ == '__main__':
    main()
