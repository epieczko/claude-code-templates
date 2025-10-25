#!/usr/bin/env python3
"""
Comprehensive analysis of all Claude Code components:
- Hooks (40 JSON files)
- Commands (210 MD files)
- Skills (48 MD files)
- MCPs (57 JSON files)
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Platform-specific keywords for filtering
PLATFORM_SPECIFIC_KEYWORDS = [
    'netlify', 'vercel', 'supabase', 'neon', 'aws', 'azure', 'gcp',
    'heroku', 'firebase', 'cloudflare', 'github', 'gitlab', 'bitbucket',
    'stripe', 'twilio', 'sendgrid', 'shopify', 'wordpress', 'woocommerce',
    'salesforce', 'hubspot', 'zendesk', 'intercom', 'slack', 'discord',
    'telegram', 'twitter', 'facebook', 'linkedin', 'youtube', 'tiktok',
    'obsidian', 'notion', 'airtable', 'monday', 'jira', 'asana',
    'unity', 'unreal', 'godot', 'blender', 'maya', 'photoshop',
    'ffmpeg', 'playwright', 'browserbase', 'google-ads', 'facebook-ads'
]

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

def get_content_after_frontmatter(content):
    """Get content after frontmatter."""
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    return content.strip()

def is_platform_specific(text):
    """Check if text is tied to specific platforms/services."""
    text_lower = text.lower()
    matches = []
    for keyword in PLATFORM_SPECIFIC_KEYWORDS:
        if keyword in text_lower:
            matches.append(keyword)
    return matches

# ==================== HOOKS EXTRACTION ====================

def extract_hooks():
    """Extract all hooks from JSON files."""
    hooks_dir = Path('cli-tool/components/hooks')
    hooks = []

    for hook_file in sorted(hooks_dir.rglob('*.json')):
        if hook_file.name == 'HOOK_PATTERNS_COMPRESSED.json':
            continue

        try:
            with open(hook_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Get relative path from hooks directory
            rel_path = hook_file.relative_to(hooks_dir)
            category = str(rel_path.parent) if rel_path.parent != Path('.') else 'uncategorized'

            hook_data = {
                'name': hook_file.stem,
                'description': data.get('description', ''),
                'category': category,
                'file_path': str(hook_file),
                'hook_config': data.get('hooks', {})
            }

            hooks.append(hook_data)
        except Exception as e:
            print(f"Error reading {hook_file}: {e}")

    return hooks

def score_hook(hook):
    """Calculate quality score for a hook (0-100)."""
    score = 0
    details = {}

    # 1. Description Quality (0-30)
    desc = hook['description']
    desc_score = 0
    if desc:
        length_score = min(len(desc) / 15, 20)
        desc_score += length_score
        # Well-structured descriptions
        if any(word in desc.lower() for word in ['enforce', 'validate', 'prevent', 'ensure', 'notify']):
            desc_score += 10
    details['description_score'] = round(desc_score, 1)
    score += desc_score

    # 2. Hook Configuration Completeness (0-40)
    config_score = 0
    hook_config = hook['hook_config']
    if hook_config:
        config_score += 20
        # Multiple hook types defined
        if len(hook_config.keys()) > 1:
            config_score += 10
        # Has matcher and command
        for hook_type, hooks_list in hook_config.items():
            if hooks_list and len(hooks_list) > 0:
                config_score += 10
                break
    details['config_score'] = config_score
    score += config_score

    # 3. Category Appropriateness (0-20)
    category_score = 0
    if hook['category'] in ['git', 'security', 'development-tools', 'testing']:
        category_score = 20  # Core categories
    elif hook['category'] in ['automation', 'performance']:
        category_score = 15  # Useful categories
    else:
        category_score = 10
    details['category_score'] = category_score
    score += category_score

    # 4. Usefulness (0-10)
    usefulness_score = 10  # Hooks are generally useful
    details['usefulness_score'] = usefulness_score
    score += usefulness_score

    details['total_score'] = round(score, 1)
    return score, details

# ==================== COMMANDS EXTRACTION ====================

def extract_commands():
    """Extract all commands from MD files."""
    commands_dir = Path('cli-tool/components/commands')
    commands = []

    for cmd_file in sorted(commands_dir.rglob('*.md')):
        try:
            with open(cmd_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter = extract_frontmatter(content)
            cmd_content = get_content_after_frontmatter(content)

            # Get relative path from commands directory
            rel_path = cmd_file.relative_to(commands_dir)
            category = str(rel_path.parent) if rel_path.parent != Path('.') else 'uncategorized'

            command_data = {
                'name': cmd_file.stem,
                'description': frontmatter.get('description', ''),
                'category': category,
                'allowed_tools': frontmatter.get('allowed-tools', ''),
                'argument_hint': frontmatter.get('argument-hint', ''),
                'file_path': str(cmd_file),
                'content': cmd_content
            }

            commands.append(command_data)
        except Exception as e:
            print(f"Error reading {cmd_file}: {e}")

    return commands

def score_command(command):
    """Calculate quality score for a command (0-100)."""
    score = 0
    details = {}

    # 1. Description Quality (0-20)
    desc = command['description']
    desc_score = 0
    if desc:
        length_score = min(len(desc) / 10, 15)
        desc_score += length_score
        if any(word in desc.lower() for word in ['generate', 'setup', 'configure', 'optimize', 'migrate']):
            desc_score += 5
    details['description_score'] = round(desc_score, 1)
    score += desc_score

    # 2. Content Depth (0-30)
    content = command['content']
    content_score = 0
    if content:
        word_count = len(content.split())
        if word_count > 200:
            content_score += 20
        elif word_count > 100:
            content_score += 15
        elif word_count > 50:
            content_score += 10

        # Has structured sections
        has_headers = bool(re.search(r'^#+\s', content, re.MULTILINE))
        if has_headers:
            content_score += 10
    details['content_score'] = round(content_score, 1)
    score += content_score

    # 3. Tools Configuration (0-20)
    tools_score = 0
    if command['allowed_tools']:
        tools_count = len(command['allowed_tools'].split(','))
        tools_score = min(tools_count * 5, 20)
    details['tools_score'] = tools_score
    score += tools_score

    # 4. Argument Configuration (0-15)
    arg_score = 15 if command['argument_hint'] else 0
    details['argument_score'] = arg_score
    score += arg_score

    # 5. Category Appropriateness (0-15)
    category_score = 0
    if command['category'] in ['testing', 'setup', 'performance', 'migration', 'git']:
        category_score = 15  # Core categories
    elif command['category'] not in ['game-development', 'podcast']:
        category_score = 10
    else:
        category_score = 5
    details['category_score'] = category_score
    score += category_score

    details['total_score'] = round(score, 1)
    return score, details

# ==================== SKILLS EXTRACTION ====================

def extract_skills():
    """Extract all skills from MD files."""
    skills_dir = Path('cli-tool/components/skills')
    skills = []

    # Only get SKILL.md files, not theme files
    for skill_file in sorted(skills_dir.rglob('SKILL.md')):
        try:
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter = extract_frontmatter(content)
            skill_content = get_content_after_frontmatter(content)

            # Get category from parent directory
            parent_dirs = skill_file.parts
            skills_idx = parent_dirs.index('skills')
            category = '/'.join(parent_dirs[skills_idx+1:-1]) if len(parent_dirs) > skills_idx + 2 else 'uncategorized'

            skill_data = {
                'name': frontmatter.get('name', skill_file.parent.name),
                'description': frontmatter.get('description', ''),
                'category': category,
                'license': frontmatter.get('license', ''),
                'file_path': str(skill_file),
                'content': skill_content
            }

            skills.append(skill_data)
        except Exception as e:
            print(f"Error reading {skill_file}: {e}")

    return skills

def score_skill(skill):
    """Calculate quality score for a skill (0-100)."""
    score = 0
    details = {}

    # 1. Description Quality (0-25)
    desc = skill['description']
    desc_score = 0
    if desc:
        length_score = min(len(desc) / 15, 20)
        desc_score += length_score
        if 'applies when' in desc.lower() or 'use when' in desc.lower():
            desc_score += 5
    details['description_score'] = round(desc_score, 1)
    score += desc_score

    # 2. Content Depth (0-40)
    content = skill['content']
    content_score = 0
    if content:
        word_count = len(content.split())
        if word_count > 1000:
            content_score += 25
        elif word_count > 500:
            content_score += 20
        elif word_count > 200:
            content_score += 15

        # Well-structured with code examples
        has_code = bool(re.search(r'```', content))
        has_headers = bool(re.search(r'^#+\s', content, re.MULTILINE))
        if has_code:
            content_score += 10
        if has_headers:
            content_score += 5
    details['content_score'] = round(content_score, 1)
    score += content_score

    # 3. License/Documentation (0-15)
    license_score = 15 if skill['license'] else 10
    details['license_score'] = license_score
    score += license_score

    # 4. Practical Applicability (0-20)
    # Skills are generally specialized tools
    applicability_score = 15
    if skill['category'] in ['development', 'utilities']:
        applicability_score = 20
    details['applicability_score'] = applicability_score
    score += applicability_score

    details['total_score'] = round(score, 1)
    return score, details

# ==================== MCPS EXTRACTION ====================

def extract_mcps():
    """Extract all MCPs from JSON files."""
    mcps_dir = Path('cli-tool/components/mcps')
    mcps = []

    for mcp_file in sorted(mcps_dir.rglob('*.json')):
        try:
            with open(mcp_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Get relative path from mcps directory
            rel_path = mcp_file.relative_to(mcps_dir)
            category = str(rel_path.parent) if rel_path.parent != Path('.') else 'uncategorized'

            # MCPs have nested structure
            mcp_servers = data.get('mcpServers', {})
            for server_name, server_config in mcp_servers.items():
                mcp_data = {
                    'name': server_name,
                    'file_name': mcp_file.stem,
                    'description': server_config.get('description', ''),
                    'category': category,
                    'command': server_config.get('command', ''),
                    'args': server_config.get('args', []),
                    'env': server_config.get('env', {}),
                    'file_path': str(mcp_file)
                }

                mcps.append(mcp_data)
        except Exception as e:
            print(f"Error reading {mcp_file}: {e}")

    return mcps

def score_mcp(mcp):
    """Calculate quality score for an MCP (0-100)."""
    score = 0
    details = {}

    # 1. Description Quality (0-30)
    desc = mcp['description']
    desc_score = 0
    if desc:
        length_score = min(len(desc) / 12, 25)
        desc_score += length_score
        if 'model context protocol' in desc.lower() or 'mcp' in desc.lower():
            desc_score += 5
    details['description_score'] = round(desc_score, 1)
    score += desc_score

    # 2. Configuration Completeness (0-30)
    config_score = 0
    if mcp['command']:
        config_score += 15
    if mcp['args'] and len(mcp['args']) > 0:
        config_score += 10
    if mcp['env']:
        config_score += 5
    details['config_score'] = config_score
    score += config_score

    # 3. Category Appropriateness (0-20)
    category_score = 0
    core_categories = ['filesystem', 'database', 'development', 'api']
    platform_categories = ['browser_automation', 'marketing', 'social-media']

    if mcp['category'] in core_categories:
        category_score = 20
    elif mcp['category'] in platform_categories:
        category_score = 10
    else:
        category_score = 15
    details['category_score'] = category_score
    score += category_score

    # 4. Platform Dependency Check (0-20)
    platform_deps = is_platform_specific(mcp['name'] + ' ' + mcp['description'])
    if not platform_deps:
        dependency_score = 20  # No platform dependency is good
    elif len(platform_deps) == 1:
        dependency_score = 15  # Single platform
    else:
        dependency_score = 10  # Multiple platforms
    details['dependency_score'] = dependency_score
    score += dependency_score

    details['total_score'] = round(score, 1)
    return score, details

# ==================== MAIN ANALYSIS ====================

def analyze_all_components():
    """Analyze all component types."""
    print("Extracting components...")

    hooks = extract_hooks()
    commands = extract_commands()
    skills = extract_skills()
    mcps = extract_mcps()

    print(f"Found {len(hooks)} hooks")
    print(f"Found {len(commands)} commands")
    print(f"Found {len(skills)} skills")
    print(f"Found {len(mcps)} MCPs")

    print("\nAnalyzing quality scores...")

    # Score all components
    hooks_analysis = []
    for hook in hooks:
        quality_score, score_details = score_hook(hook)
        platform_deps = is_platform_specific(hook['description'])

        hooks_analysis.append({
            **hook,
            'quality_score': round(quality_score, 1),
            'score_details': score_details,
            'platform_dependencies': platform_deps
        })

    commands_analysis = []
    for command in commands:
        quality_score, score_details = score_command(command)
        platform_deps = is_platform_specific(command['name'] + ' ' + command['description'] + ' ' + command['content'])

        commands_analysis.append({
            **command,
            'quality_score': round(quality_score, 1),
            'score_details': score_details,
            'platform_dependencies': platform_deps
        })

    skills_analysis = []
    for skill in skills:
        quality_score, score_details = score_skill(skill)
        platform_deps = is_platform_specific(skill['name'] + ' ' + skill['description'] + ' ' + skill['content'])

        skills_analysis.append({
            **skill,
            'quality_score': round(quality_score, 1),
            'score_details': score_details,
            'platform_dependencies': platform_deps
        })

    mcps_analysis = []
    for mcp in mcps:
        quality_score, score_details = score_mcp(mcp)
        platform_deps = is_platform_specific(mcp['name'] + ' ' + mcp['description'])

        mcps_analysis.append({
            **mcp,
            'quality_score': round(quality_score, 1),
            'score_details': score_details,
            'platform_dependencies': platform_deps
        })

    # Sort by quality score
    hooks_analysis.sort(key=lambda x: x['quality_score'], reverse=True)
    commands_analysis.sort(key=lambda x: x['quality_score'], reverse=True)
    skills_analysis.sort(key=lambda x: x['quality_score'], reverse=True)
    mcps_analysis.sort(key=lambda x: x['quality_score'], reverse=True)

    return {
        'hooks': hooks_analysis,
        'commands': commands_analysis,
        'skills': skills_analysis,
        'mcps': mcps_analysis
    }

def generate_recommendations(analysis):
    """Generate migration recommendations for all component types."""
    recommendations = {
        'hooks': {'highly_recommended': [], 'recommended': [], 'conditional': [], 'not_recommended': []},
        'commands': {'highly_recommended': [], 'recommended': [], 'conditional': [], 'not_recommended': []},
        'skills': {'highly_recommended': [], 'recommended': [], 'conditional': [], 'not_recommended': []},
        'mcps': {'highly_recommended': [], 'recommended': [], 'conditional': [], 'not_recommended': []}
    }

    # Hooks recommendations
    for hook in analysis['hooks']:
        score = hook['quality_score']
        platform_deps = hook['platform_dependencies']

        if score >= 70 and not platform_deps:
            recommendations['hooks']['highly_recommended'].append(hook)
        elif score >= 60:
            recommendations['hooks']['recommended'].append(hook)
        elif score >= 50 or platform_deps:
            recommendations['hooks']['conditional'].append(hook)
        else:
            recommendations['hooks']['not_recommended'].append(hook)

    # Commands recommendations
    for command in analysis['commands']:
        score = command['quality_score']
        platform_deps = command['platform_dependencies']

        if score >= 70 and len(platform_deps) == 0:
            recommendations['commands']['highly_recommended'].append(command)
        elif score >= 60 and len(platform_deps) <= 1:
            recommendations['commands']['recommended'].append(command)
        elif score >= 50:
            recommendations['commands']['conditional'].append(command)
        else:
            recommendations['commands']['not_recommended'].append(command)

    # Skills recommendations
    for skill in analysis['skills']:
        score = skill['quality_score']
        platform_deps = skill['platform_dependencies']

        if score >= 70 and not platform_deps:
            recommendations['skills']['highly_recommended'].append(skill)
        elif score >= 60:
            recommendations['skills']['recommended'].append(skill)
        elif score >= 50:
            recommendations['skills']['conditional'].append(skill)
        else:
            recommendations['skills']['not_recommended'].append(skill)

    # MCPs recommendations
    for mcp in analysis['mcps']:
        score = mcp['quality_score']
        platform_deps = mcp['platform_dependencies']

        if score >= 70 and len(platform_deps) <= 1:
            recommendations['mcps']['highly_recommended'].append(mcp)
        elif score >= 60:
            recommendations['mcps']['recommended'].append(mcp)
        elif score >= 50 or platform_deps:
            recommendations['mcps']['conditional'].append(mcp)
        else:
            recommendations['mcps']['not_recommended'].append(mcp)

    return recommendations

def create_reports(analysis, recommendations):
    """Create comprehensive reports."""

    # Save full analysis
    with open('components_analysis.json', 'w', encoding='utf-8') as f:
        json.dump({
            'analysis': analysis,
            'recommendations': recommendations,
            'statistics': {
                'hooks': {
                    'total': len(analysis['hooks']),
                    'highly_recommended': len(recommendations['hooks']['highly_recommended']),
                    'recommended': len(recommendations['hooks']['recommended']),
                    'conditional': len(recommendations['hooks']['conditional']),
                    'not_recommended': len(recommendations['hooks']['not_recommended'])
                },
                'commands': {
                    'total': len(analysis['commands']),
                    'highly_recommended': len(recommendations['commands']['highly_recommended']),
                    'recommended': len(recommendations['commands']['recommended']),
                    'conditional': len(recommendations['commands']['conditional']),
                    'not_recommended': len(recommendations['commands']['not_recommended'])
                },
                'skills': {
                    'total': len(analysis['skills']),
                    'highly_recommended': len(recommendations['skills']['highly_recommended']),
                    'recommended': len(recommendations['skills']['recommended']),
                    'conditional': len(recommendations['skills']['conditional']),
                    'not_recommended': len(recommendations['skills']['not_recommended'])
                },
                'mcps': {
                    'total': len(analysis['mcps']),
                    'highly_recommended': len(recommendations['mcps']['highly_recommended']),
                    'recommended': len(recommendations['mcps']['recommended']),
                    'conditional': len(recommendations['mcps']['conditional']),
                    'not_recommended': len(recommendations['mcps']['not_recommended'])
                }
            }
        }, f, indent=2, ensure_ascii=False)

    print("\n✅ Created components_analysis.json")

    # Create summary report
    with open('components_migration_summary.md', 'w', encoding='utf-8') as f:
        f.write('# Components Migration Analysis Summary\n\n')

        for comp_type in ['hooks', 'commands', 'skills', 'mcps']:
            stats = {
                'total': len(analysis[comp_type]),
                'highly_recommended': len(recommendations[comp_type]['highly_recommended']),
                'recommended': len(recommendations[comp_type]['recommended']),
                'conditional': len(recommendations[comp_type]['conditional']),
                'not_recommended': len(recommendations[comp_type]['not_recommended'])
            }

            f.write(f'## {comp_type.upper()}\n\n')
            f.write(f'Total analyzed: **{stats["total"]}**\n\n')
            f.write(f'- ✅ **Highly Recommended**: {stats["highly_recommended"]}\n')
            f.write(f'- 👍 **Recommended**: {stats["recommended"]}\n')
            f.write(f'- ⚠️  **Conditional**: {stats["conditional"]}\n')
            f.write(f'- ❌ **Not Recommended**: {stats["not_recommended"]}\n')
            f.write(f'- 📊 **Total suitable**: {stats["highly_recommended"] + stats["recommended"]}\n\n')

            # Top 5
            f.write(f'### Top 5 {comp_type.title()}\n\n')
            for i, item in enumerate(analysis[comp_type][:5], 1):
                f.write(f'{i}. **{item["name"]}** (Score: {item["quality_score"]}/100)\n')
                f.write(f'   - Category: {item["category"]}\n')
                if item.get('description'):
                    f.write(f'   - {item["description"][:120]}...\n')
                f.write('\n')

    print("✅ Created components_migration_summary.md")

def main():
    print("=" * 80)
    print("COMPREHENSIVE COMPONENTS ANALYSIS")
    print("=" * 80)

    analysis = analyze_all_components()
    recommendations = generate_recommendations(analysis)
    create_reports(analysis, recommendations)

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

    # Print summary
    for comp_type in ['hooks', 'commands', 'skills', 'mcps']:
        total = len(analysis[comp_type])
        high = len(recommendations[comp_type]['highly_recommended'])
        rec = len(recommendations[comp_type]['recommended'])
        cond = len(recommendations[comp_type]['conditional'])
        not_rec = len(recommendations[comp_type]['not_recommended'])

        print(f"\n{comp_type.upper()}:")
        print(f"  Total: {total}")
        print(f"  ✅ Highly Recommended: {high}")
        print(f"  👍 Recommended: {rec}")
        print(f"  ⚠️  Conditional: {cond}")
        print(f"  ❌ Not Recommended: {not_rec}")
        print(f"  📊 Suitable for migration: {high + rec}")

if __name__ == '__main__':
    main()
