#!/usr/bin/env python3
"""
Analyze agents and create quality scores for migration decisions.
"""

import json
import re
from pathlib import Path

# Platform-specific keywords that might indicate environment-specific agents
PLATFORM_SPECIFIC_KEYWORDS = [
    'netlify', 'vercel', 'supabase', 'neon', 'aws', 'azure', 'gcp',
    'heroku', 'firebase', 'cloudflare', 'github', 'gitlab', 'bitbucket',
    'stripe', 'twilio', 'sendgrid', 'shopify', 'wordpress', 'woocommerce',
    'salesforce', 'hubspot', 'zendesk', 'intercom', 'slack', 'discord',
    'telegram', 'twitter', 'facebook', 'linkedin', 'youtube', 'tiktok',
    'obsidian', 'notion', 'airtable', 'monday', 'jira', 'asana',
    'unity', 'unreal', 'godot', 'blender', 'maya', 'photoshop',
    'ffmpeg', 'podcast', 'video-editor', 'audio-mixer'
]

# Highly specialized or niche categories
NICHE_CATEGORIES = [
    'ffmpeg-clip-team',
    'podcast-creator-team',
    'obsidian-ops-team',
    'ocr-extraction-team',
    'game-development'
]

# Core/universal categories that are broadly applicable
CORE_CATEGORIES = [
    'development-team',
    'development-tools',
    'devops-infrastructure',
    'database',
    'security',
    'documentation',
    'expert-advisors',
    'programming-languages',
    'ai-specialists',
    'data-ai',
    'performance-testing'
]

def load_agents():
    """Load agents from the JSON export."""
    with open('agents_export.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['agents']

def is_platform_specific(agent):
    """Check if agent is tied to a specific platform/service."""
    text = (agent['name'] + ' ' + agent['description'] + ' ' + agent['content']).lower()

    matches = []
    for keyword in PLATFORM_SPECIFIC_KEYWORDS:
        if keyword in text:
            matches.append(keyword)

    return matches

def calculate_quality_score(agent):
    """
    Calculate a quality score for an agent (0-100).

    Scoring factors:
    - Description quality (0-20): Length, clarity, completeness
    - Content depth (0-25): Substantial instructions vs thin content
    - Tools configured (0-15): Has explicit tool configuration
    - Model specified (0-10): Has model preference
    - Documentation quality (0-15): Well-structured with sections
    - Proactive usage indicator (0-15): Has "Use PROACTIVELY" guidance
    """
    score = 0
    details = {}

    # 1. Description Quality (0-20)
    desc = agent['description']
    desc_score = 0
    if desc:
        length_score = min(len(desc) / 20, 15)  # Up to 15 points for length
        desc_score += length_score
        if 'Use PROACTIVELY' in desc or 'use proactively' in desc.lower():
            desc_score += 5  # Bonus for proactive guidance
    details['description_score'] = round(desc_score, 1)
    score += desc_score

    # 2. Content Depth (0-25)
    content = agent['content']
    content_score = 0
    if content:
        # Length-based scoring
        word_count = len(content.split())
        if word_count > 500:
            content_score += 15
        elif word_count > 250:
            content_score += 10
        elif word_count > 100:
            content_score += 5

        # Structure indicators (headers, lists, code blocks)
        has_headers = bool(re.search(r'^#+\s', content, re.MULTILINE))
        has_lists = bool(re.search(r'^\s*[-*]\s', content, re.MULTILINE))
        has_code = bool(re.search(r'```', content))

        if has_headers:
            content_score += 4
        if has_lists:
            content_score += 3
        if has_code:
            content_score += 3

    details['content_score'] = round(content_score, 1)
    score += content_score

    # 3. Tools Configuration (0-15)
    tools_score = 0
    if agent['tools']:
        tools_count = len(agent['tools'].split(','))
        tools_score = min(tools_count * 3, 15)
    details['tools_score'] = round(tools_score, 1)
    score += tools_score

    # 4. Model Specified (0-10)
    model_score = 10 if agent['model'] else 0
    details['model_score'] = model_score
    score += model_score

    # 5. Documentation Quality (0-15)
    doc_score = 0
    # Check for common documentation sections
    sections_found = 0
    common_sections = [
        r'##\s*(Focus|Core|Expertise|Specialization)',
        r'##\s*(Approach|Method|Process|Workflow)',
        r'##\s*(Output|Deliverable|Result)',
        r'##\s*(Best Practice|Guideline|Principle)',
        r'##\s*(Example|Usage|Implementation)'
    ]
    for pattern in common_sections:
        if re.search(pattern, content, re.IGNORECASE):
            sections_found += 1

    doc_score = min(sections_found * 3, 15)
    details['documentation_score'] = doc_score
    score += doc_score

    # 6. Proactive Usage Indicator (0-15)
    proactive_score = 0
    if 'PROACTIVELY' in agent['description']:
        proactive_score = 15
    details['proactive_score'] = proactive_score
    score += proactive_score

    details['total_score'] = round(score, 1)
    return score, details

def categorize_agent(agent):
    """
    Categorize agent by specificity and applicability.

    Returns:
    - 'core': Broadly applicable, fundamental agents
    - 'specialized': Useful but domain-specific
    - 'niche': Very specific use cases
    - 'platform': Tied to specific platforms/services
    """
    name = agent['name'].lower()
    description = agent['description'].lower()
    category = agent['category']

    # Check for platform-specific
    platform_matches = is_platform_specific(agent)
    if platform_matches and len(platform_matches) >= 2:
        return 'platform'

    # Check for niche categories
    if category in NICHE_CATEGORIES:
        return 'niche'

    # Check for core categories
    if category in CORE_CATEGORIES:
        return 'core'

    # Default to specialized
    return 'specialized'

def analyze_agents():
    """Perform comprehensive agent analysis."""
    agents = load_agents()

    analysis = []
    for agent in agents:
        quality_score, score_details = calculate_quality_score(agent)
        specificity = categorize_agent(agent)
        platform_deps = is_platform_specific(agent)

        analysis.append({
            'name': agent['name'],
            'category': agent['category'],
            'description': agent['description'],
            'quality_score': round(quality_score, 1),
            'score_details': score_details,
            'specificity': specificity,
            'platform_dependencies': platform_deps,
            'tools': agent['tools'],
            'model': agent['model'],
            'file_path': agent['file_path']
        })

    # Sort by quality score (descending)
    analysis.sort(key=lambda x: x['quality_score'], reverse=True)

    return analysis

def generate_recommendations(analysis):
    """Generate migration recommendations based on analysis."""
    recommendations = {
        'highly_recommended': [],  # Core agents with high quality
        'recommended': [],          # Good quality, broadly applicable
        'conditional': [],          # Platform-specific or specialized but high quality
        'not_recommended': []       # Low quality or very niche
    }

    for agent_analysis in analysis:
        score = agent_analysis['quality_score']
        specificity = agent_analysis['specificity']

        # Decision logic
        if specificity == 'core' and score >= 70:
            recommendations['highly_recommended'].append(agent_analysis)
        elif specificity == 'core' and score >= 50:
            recommendations['recommended'].append(agent_analysis)
        elif specificity == 'specialized' and score >= 70:
            recommendations['recommended'].append(agent_analysis)
        elif specificity == 'specialized' and score >= 50:
            recommendations['conditional'].append(agent_analysis)
        elif specificity == 'platform' and score >= 70:
            recommendations['conditional'].append(agent_analysis)
        else:
            recommendations['not_recommended'].append(agent_analysis)

    return recommendations

def create_reports(analysis, recommendations):
    """Create analysis reports."""

    # 1. Full analysis JSON
    with open('agents_analysis.json', 'w', encoding='utf-8') as f:
        json.dump({
            'analysis': analysis,
            'recommendations': recommendations,
            'statistics': {
                'total_agents': len(analysis),
                'highly_recommended': len(recommendations['highly_recommended']),
                'recommended': len(recommendations['recommended']),
                'conditional': len(recommendations['conditional']),
                'not_recommended': len(recommendations['not_recommended'])
            }
        }, f, indent=2, ensure_ascii=False)

    # 2. Markdown report
    with open('agents_migration_report.md', 'w', encoding='utf-8') as f:
        f.write('# Agent Migration Analysis Report\n\n')

        stats = {
            'total': len(analysis),
            'highly_recommended': len(recommendations['highly_recommended']),
            'recommended': len(recommendations['recommended']),
            'conditional': len(recommendations['conditional']),
            'not_recommended': len(recommendations['not_recommended'])
        }

        f.write('## Executive Summary\n\n')
        f.write(f'Total agents analyzed: **{stats["total"]}**\n\n')
        f.write(f'- ✅ **Highly Recommended**: {stats["highly_recommended"]} agents\n')
        f.write(f'- 👍 **Recommended**: {stats["recommended"]} agents\n')
        f.write(f'- ⚠️  **Conditional**: {stats["conditional"]} agents\n')
        f.write(f'- ❌ **Not Recommended**: {stats["not_recommended"]} agents\n\n')

        f.write('## Recommendation Criteria\n\n')
        f.write('### Quality Score Components (0-100)\n\n')
        f.write('- **Description Quality** (0-20): Length, clarity, proactive usage guidance\n')
        f.write('- **Content Depth** (0-25): Word count, structure, examples\n')
        f.write('- **Tools Configuration** (0-15): Explicit tool specifications\n')
        f.write('- **Model Specification** (0-10): Model preference defined\n')
        f.write('- **Documentation Quality** (0-15): Well-structured sections\n')
        f.write('- **Proactive Indicator** (0-15): "Use PROACTIVELY" guidance\n\n')

        f.write('### Specificity Categories\n\n')
        f.write('- **Core**: Broadly applicable, fundamental development agents\n')
        f.write('- **Specialized**: Domain-specific but widely useful\n')
        f.write('- **Niche**: Very specific use cases\n')
        f.write('- **Platform**: Tied to specific platforms/services\n\n')

        f.write('### Migration Recommendations\n\n')
        f.write('- **Highly Recommended**: Core agents with quality score ≥ 70\n')
        f.write('- **Recommended**: Core agents ≥ 50 OR specialized agents ≥ 70\n')
        f.write('- **Conditional**: Review based on your needs (platform-specific or specialized)\n')
        f.write('- **Not Recommended**: Low quality or very niche\n\n')

        # Detailed sections
        for category, title, emoji in [
            ('highly_recommended', 'Highly Recommended Agents', '✅'),
            ('recommended', 'Recommended Agents', '👍'),
            ('conditional', 'Conditional Agents (Review Required)', '⚠️'),
        ]:
            f.write(f'## {emoji} {title}\n\n')
            agents_list = recommendations[category]
            f.write(f'Total: {len(agents_list)}\n\n')

            for agent in sorted(agents_list, key=lambda x: x['quality_score'], reverse=True):
                f.write(f'### {agent["name"]} (Score: {agent["quality_score"]}/100)\n\n')
                f.write(f'**Category**: {agent["category"]} | **Specificity**: {agent["specificity"]}\n\n')
                f.write(f'**Description**: {agent["description"]}\n\n')

                if agent['platform_dependencies']:
                    f.write(f'**Platform Dependencies**: {", ".join(agent["platform_dependencies"])}\n\n')

                f.write(f'**Quality Breakdown**:\n')
                for key, value in agent['score_details'].items():
                    if key != 'total_score':
                        label = key.replace('_', ' ').title()
                        f.write(f'- {label}: {value}\n')
                f.write('\n---\n\n')

    # 3. Top agents for migration (CSV-like)
    with open('agents_top_recommendations.txt', 'w', encoding='utf-8') as f:
        f.write('TOP AGENTS FOR BETTY MIGRATION\n')
        f.write('=' * 80 + '\n\n')

        top_agents = recommendations['highly_recommended'] + recommendations['recommended']
        top_agents.sort(key=lambda x: x['quality_score'], reverse=True)

        f.write(f'Total recommended agents: {len(top_agents)}\n\n')

        for i, agent in enumerate(top_agents, 1):
            f.write(f'{i}. {agent["name"]} (Score: {agent["quality_score"]}/100)\n')
            f.write(f'   Category: {agent["category"]} | Type: {agent["specificity"]}\n')
            f.write(f'   {agent["description"][:100]}...\n\n')

def main():
    print("Analyzing agents...")
    analysis = analyze_agents()

    print("Generating recommendations...")
    recommendations = generate_recommendations(analysis)

    print("Creating reports...")
    create_reports(analysis, recommendations)

    stats = {
        'total': len(analysis),
        'highly_recommended': len(recommendations['highly_recommended']),
        'recommended': len(recommendations['recommended']),
        'conditional': len(recommendations['conditional']),
        'not_recommended': len(recommendations['not_recommended'])
    }

    print("\n" + "=" * 80)
    print("AGENT MIGRATION ANALYSIS COMPLETE")
    print("=" * 80)
    print(f"\nTotal agents analyzed: {stats['total']}")
    print(f"\n✅ Highly Recommended: {stats['highly_recommended']} agents")
    print(f"👍 Recommended: {stats['recommended']} agents")
    print(f"⚠️  Conditional (review needed): {stats['conditional']} agents")
    print(f"❌ Not Recommended: {stats['not_recommended']} agents")
    print(f"\n📊 Total suitable for migration: {stats['highly_recommended'] + stats['recommended']}")

    print("\n\nFiles created:")
    print("  - agents_analysis.json (complete analysis data)")
    print("  - agents_migration_report.md (detailed migration guide)")
    print("  - agents_top_recommendations.txt (quick reference)")

    # Show top 10
    top_10 = analysis[:10]
    print("\n\nTOP 10 HIGHEST QUALITY AGENTS:")
    print("-" * 80)
    for i, agent in enumerate(top_10, 1):
        print(f"{i}. {agent['name']} ({agent['quality_score']}/100) - {agent['category']}")

if __name__ == '__main__':
    main()
