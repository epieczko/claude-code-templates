# Claude Code Agents Export

Total agents: 163

## Table of Contents

- [ai-specialists](#ai-specialists)
- [api-graphql](#api-graphql)
- [blockchain-web3](#blockchain-web3)
- [business-marketing](#business-marketing)
- [data-ai](#data-ai)
- [database](#database)
- [deep-research-team](#deep-research-team)
- [development-team](#development-team)
- [development-tools](#development-tools)
- [devops-infrastructure](#devops-infrastructure)
- [documentation](#documentation)
- [expert-advisors](#expert-advisors)
- [ffmpeg-clip-team](#ffmpeg-clip-team)
- [game-development](#game-development)
- [git](#git)
- [mcp-dev-team](#mcp-dev-team)
- [modernization](#modernization)
- [obsidian-ops-team](#obsidian-ops-team)
- [ocr-extraction-team](#ocr-extraction-team)
- [performance-testing](#performance-testing)
- [podcast-creator-team](#podcast-creator-team)
- [programming-languages](#programming-languages)
- [realtime](#realtime)
- [security](#security)
- [web-tools](#web-tools)

---

## ai-specialists

### ai-ethics-advisor

**Description:** AI ethics and responsible AI development specialist. Use PROACTIVELY for bias assessment, fairness evaluation, ethical AI implementation, and regulatory compliance guidance. Expert in AI safety and alignment.

**Tools:** Read, Write, WebSearch, Grep

**Model:** opus

**File:** `cli-tool/components/agents/ai-specialists/ai-ethics-advisor.md`

---

### hackathon-ai-strategist

**Description:** Expert hackathon strategist and judge. Use PROACTIVELY for AI hackathon ideation, project evaluation, feasibility assessment, and presentation strategies. Specializes in winning concepts within time constraints.

**Tools:** Read, WebSearch, WebFetch

**Model:** sonnet

**File:** `cli-tool/components/agents/ai-specialists/hackathon-ai-strategist.md`

---

### llms-maintainer

**Description:** LLMs.txt roadmap file generator and maintainer. Use PROACTIVELY after build completion, content changes, or when implementing AEO (AI Engine Optimization). Scans site structure and updates AI crawler navigation.

**Tools:** Read, Write, Bash, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/ai-specialists/llms-maintainer.md`

---

### model-evaluator

**Description:** AI model evaluation and benchmarking specialist. Use PROACTIVELY for model selection, performance comparison, cost analysis, and evaluation metric design. Expert in LLM capabilities and limitations.

**Tools:** Read, Write, Bash, WebSearch

**Model:** opus

**File:** `cli-tool/components/agents/ai-specialists/model-evaluator.md`

---

### prompt-engineer

**Description:** Expert prompt optimization for LLMs and AI systems. Use PROACTIVELY when building AI features, improving agent performance, or crafting system prompts. Masters prompt patterns and techniques.

**Tools:** Read, Write, Edit

**Model:** opus

**File:** `cli-tool/components/agents/ai-specialists/prompt-engineer.md`

---

### search-specialist

**Description:** Expert web researcher using advanced search techniques and synthesis. Masters search operators, result filtering, and multi-source verification. Handles competitive analysis and fact-checking. Use PROACTIVELY for deep research, information gathering, or trend analysis.

**Model:** haiku

**File:** `cli-tool/components/agents/ai-specialists/search-specialist.md`

---

### task-decomposition-expert

**Description:** Complex goal breakdown specialist. Use PROACTIVELY for multi-step projects requiring different capabilities. Masters workflow architecture, tool selection, and ChromaDB integration for optimal task orchestration.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/ai-specialists/task-decomposition-expert.md`

---

## api-graphql

### graphql-architect

**Description:** GraphQL schema design and API architecture specialist. Use PROACTIVELY for GraphQL schema design, resolver optimization, federation, performance issues, and subscription implementation.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/api-graphql/graphql-architect.md`

---

### graphql-performance-optimizer

**Description:** GraphQL performance analysis and optimization specialist. Use PROACTIVELY for query performance issues, N+1 problems, caching strategies, and production GraphQL API optimization.

**Tools:** Read, Write, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/api-graphql/graphql-performance-optimizer.md`

---

### graphql-security-specialist

**Description:** GraphQL API security and authorization specialist. Use PROACTIVELY for GraphQL security audits, authorization implementation, query validation, and protection against GraphQL-specific attacks.

**Tools:** Read, Write, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/api-graphql/graphql-security-specialist.md`

---

## blockchain-web3

### smart-contract-auditor

**Description:** Use this agent when conducting security audits of smart contracts. Specializes in vulnerability detection, attack vector analysis, and comprehensive security assessments. Examples: <example>Context: User needs to audit a DeFi protocol user: 'Can you audit my yield farming contract for security issues?' assistant: 'I'll use the smart-contract-auditor agent to perform a comprehensive security audit, checking for reentrancy, overflow issues, and economic attacks' <commentary>Security audits require specialized knowledge of attack patterns and vulnerability detection</commentary></example> <example>Context: User found a suspicious transaction user: 'This transaction looks like an exploit, can you analyze it?' assistant: 'I'll use the smart-contract-auditor agent to analyze the transaction and identify the exploit mechanism' <commentary>Exploit analysis requires deep understanding of attack vectors and contract vulnerabilities</commentary></example> <example>Context: User needs pre-deployment security review user: 'My NFT marketplace is ready for deployment, can you check for security issues?' assistant: 'I'll use the smart-contract-auditor agent to conduct a pre-deployment security review with focus on marketplace-specific vulnerabilities' <commentary>Pre-deployment audits require comprehensive security assessment across multiple attack vectors</commentary></example>

**File:** `cli-tool/components/agents/blockchain-web3/smart-contract-auditor.md`

---

### smart-contract-specialist

**Description:** Use this agent when developing production-level smart contracts. Specializes in Solidity development, Hardhat/Foundry toolchains, gas optimization, and secure contract patterns. Examples: <example>Context: User needs to build a new DeFi protocol user: 'I need to create a secure lending protocol with upgradeable contracts' assistant: 'I'll use the smart-contract-specialist agent to architect a secure lending protocol with proper upgradeability patterns and comprehensive testing' <commentary>Complex smart contract development requires specialized Solidity expertise and security knowledge</commentary></example> <example>Context: User wants to optimize contract gas costs user: 'My NFT contract has high gas fees' assistant: 'I'll use the smart-contract-specialist agent to analyze and optimize your NFT contract for gas efficiency' <commentary>Gas optimization requires deep understanding of EVM and Solidity best practices</commentary></example> <example>Context: User needs to implement complex DeFi mechanics user: 'I need to build a DEX with automated market maker functionality' assistant: 'I'll use the smart-contract-specialist agent to design and implement AMM contracts with proper liquidity management' <commentary>DeFi protocols require specialized knowledge of tokenomics and mathematical models</commentary></example>

**File:** `cli-tool/components/agents/blockchain-web3/smart-contract-specialist.md`

---

### web3-integration-specialist

**Description:** Use this agent when building Web3 frontend applications and wallet integrations. Specializes in blockchain connectivity, wallet interactions (RainbowKit, Reown, WalletConnect), ethers.js/viem, and dApp development. Examples: <example>Context: User needs to connect wallet to React app user: 'How do I integrate MetaMask and other wallets into my React dApp?' assistant: 'I'll use the web3-integration-specialist agent to set up RainbowKit with comprehensive wallet support and proper error handling' <commentary>Wallet integration requires specialized knowledge of Web3 connection patterns and user experience best practices</commentary></example> <example>Context: User wants to interact with smart contracts user: 'I need to call my smart contract functions from the frontend' assistant: 'I'll use the web3-integration-specialist agent to implement contract interactions using ethers.js with proper transaction handling and state management' <commentary>Smart contract integration requires understanding of blockchain transactions, gas estimation, and async patterns</commentary></example> <example>Context: User building NFT marketplace frontend user: 'I need to display NFT metadata and handle minting transactions' assistant: 'I'll use the web3-integration-specialist agent to create a complete NFT marketplace interface with metadata fetching and transaction management' <commentary>NFT applications require specialized handling of token standards, IPFS integration, and transaction UX</commentary></example>

**File:** `cli-tool/components/agents/blockchain-web3/web3-integration-specialist.md`

---

## business-marketing

### business-analyst

**Description:** Business metrics analysis and reporting specialist. Use PROACTIVELY for KPI tracking, revenue analysis, growth projections, cohort analysis, and investor reporting. Expert in data-driven decision making.

**Tools:** Read, Write, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/business-analyst.md`

---

### content-marketer

**Description:** Content marketing and SEO optimization specialist. Use PROACTIVELY for blog posts, social media content, email campaigns, content calendars, and SEO strategy. Expert in engagement-driven content.

**Tools:** Read, Write, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/content-marketer.md`

---

### customer-support

**Description:** Customer support and documentation specialist. Use PROACTIVELY for support ticket responses, FAQ creation, troubleshooting guides, help documentation, and customer satisfaction optimization.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/customer-support.md`

---

### legal-advisor

**Description:** Legal documentation and compliance specialist. Use PROACTIVELY for privacy policies, terms of service, GDPR compliance, legal notices, and regulatory documentation. Expert in technology law and data protection.

**Tools:** Read, Write, WebSearch

**Model:** opus

**File:** `cli-tool/components/agents/business-marketing/legal-advisor.md`

---

### marketing-attribution-analyst

**Description:** Marketing attribution and performance analysis specialist. Use PROACTIVELY for campaign tracking, attribution modeling, conversion optimization, ROI analysis, and marketing mix modeling.

**Tools:** Read, Write, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/marketing-attribution-analyst.md`

---

### payment-integration

**Description:** Payment systems integration specialist. Use PROACTIVELY for Stripe, PayPal, and payment processor implementations, checkout flows, subscription billing, webhook handling, and PCI compliance.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/payment-integration.md`

---

### product-strategist

**Description:** Product strategy and roadmap planning specialist. Use PROACTIVELY for product positioning, market analysis, feature prioritization, go-to-market strategy, and competitive intelligence.

**Tools:** Read, Write, WebSearch

**Model:** opus

**File:** `cli-tool/components/agents/business-marketing/product-strategist.md`

---

### risk-manager

**Description:** Risk management and portfolio analysis specialist. Use PROACTIVELY for portfolio risk assessment, position sizing, R-multiple analysis, hedging strategies, and risk-adjusted performance measurement.

**Tools:** Read, Write, Bash

**Model:** opus

**File:** `cli-tool/components/agents/business-marketing/risk-manager.md`

---

### sales-automator

**Description:** Sales automation and outreach specialist. Use PROACTIVELY for cold email campaigns, follow-up sequences, proposal templates, case studies, sales scripts, and conversion optimization.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/business-marketing/sales-automator.md`

---

## data-ai

### ai-engineer

**Description:** LLM application and RAG system specialist. Use PROACTIVELY for LLM integrations, RAG systems, prompt pipelines, vector search, agent orchestration, and AI-powered application development.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/data-ai/ai-engineer.md`

---

### computer-vision-engineer

**Description:** Computer vision and image processing specialist. Use PROACTIVELY for image analysis, object detection, face recognition, OCR implementation, and visual AI applications.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/data-ai/computer-vision-engineer.md`

---

### data-engineer

**Description:** Data pipeline and analytics infrastructure specialist. Use PROACTIVELY for ETL/ELT pipelines, data warehouses, streaming architectures, Spark optimization, and data platform design.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/data-ai/data-engineer.md`

---

### data-scientist

**Description:** Data analysis and statistical modeling specialist. Use PROACTIVELY for exploratory data analysis, statistical modeling, machine learning experiments, hypothesis testing, and predictive analytics.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/data-ai/data-scientist.md`

---

### ml-engineer

**Description:** ML production systems and model deployment specialist. Use PROACTIVELY for ML pipelines, model serving, feature engineering, A/B testing, monitoring, and production ML infrastructure.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/data-ai/ml-engineer.md`

---

### mlops-engineer

**Description:** ML infrastructure and operations specialist. Use PROACTIVELY for ML pipelines, experiment tracking, model registries, automated retraining, data versioning, and MLOps platform implementation.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/data-ai/mlops-engineer.md`

---

### nlp-engineer

**Description:** Natural Language Processing and text analytics specialist. Use PROACTIVELY for text processing, language models, sentiment analysis, named entity recognition, text classification, and conversational AI systems.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/data-ai/nlp-engineer.md`

---

### quant-analyst

**Description:** Quantitative finance and algorithmic trading specialist. Use PROACTIVELY for financial modeling, trading strategy development, backtesting, risk analysis, and portfolio optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/data-ai/quant-analyst.md`

---

## database

### database-admin

**Description:** Database administration specialist for operations, backups, replication, and monitoring. Use PROACTIVELY for database setup, operational issues, user management, or disaster recovery procedures.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/database/database-admin.md`

---

### database-architect

**Description:** Database architecture and design specialist. Use PROACTIVELY for database design decisions, data modeling, scalability planning, microservices data patterns, and database technology selection.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/database/database-architect.md`

---

### database-optimization

**Description:** Database performance optimization and query tuning specialist. Use PROACTIVELY for slow queries, indexing strategies, execution plan analysis, and database performance bottlenecks.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/database/database-optimization.md`

---

### database-optimizer

**Description:** SQL query optimization and database schema design specialist. Use PROACTIVELY for N+1 problems, slow queries, migration strategies, and implementing caching solutions.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/database/database-optimizer.md`

---

### neon-auth-specialist

**Description:** Neon Auth implementation specialist. Use PROACTIVELY for Stack Auth integration, user management setup, authentication flows, and security best practices with Neon database.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/database/neon-auth-specialist.md`

---

### neon-database-architect

**Description:** Neon database architecture specialist. Use PROACTIVELY for database schema design, Drizzle ORM integration, query optimization, and serverless performance tuning. Expert in connection management and database migrations.

**Tools:** Read, Write, Edit, Bash, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/database/neon-database-architect.md`

---

### neon-expert

**Description:** General Neon Serverless Postgres consultant. Use PROACTIVELY for initial Neon setup, general database questions, and coordinating with specialized agents (neon-database-architect for schemas/ORM, neon-auth-specialist for authentication).

**Tools:** Read, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/database/neon-expert.md`

---

### nosql-specialist

**Description:** NoSQL database specialist for MongoDB, Redis, Cassandra, and document/key-value stores. Use PROACTIVELY for schema design, data modeling, performance optimization, and NoSQL architecture decisions.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/database/nosql-specialist.md`

---

### supabase-schema-architect

**Description:** Supabase database schema design specialist. Use PROACTIVELY for database schema design, migration planning, and RLS policy architecture.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/database/supabase-schema-architect.md`

---

## deep-research-team

### academic-researcher

**Description:** Academic research specialist for scholarly sources, peer-reviewed papers, and academic literature. Use PROACTIVELY for research paper analysis, literature reviews, citation tracking, and academic methodology evaluation.

**Tools:** Read, Write, Edit, WebSearch, WebFetch

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/academic-researcher.md`

---

### agent-overview

**Description:** 

**File:** `cli-tool/components/agents/deep-research-team/agent-overview.md`

---

### competitive-intelligence-analyst

**Description:** Competitive intelligence and market research specialist. Use PROACTIVELY for competitor analysis, market positioning research, industry trend analysis, business intelligence gathering, and strategic market insights.

**Tools:** Read, Write, Edit, WebSearch, WebFetch

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/competitive-intelligence-analyst.md`

---

### data-analyst

**Description:** Use this agent when you need quantitative analysis, statistical insights, or data-driven research. This includes analyzing numerical data, identifying trends, creating comparisons, evaluating metrics, and suggesting data visualizations. The agent excels at finding and interpreting data from statistical databases, research datasets, government sources, and market research.\n\nExamples:\n- <example>\n  Context: The user wants to understand market trends in electric vehicle adoption.\n  user: "What are the trends in electric vehicle sales over the past 5 years?"\n  assistant: "I'll use the data-analyst agent to analyze EV sales data and identify trends."\n  <commentary>\n  Since the user is asking for trend analysis of numerical data over time, the data-analyst agent is perfect for finding sales statistics, calculating growth rates, and identifying patterns.\n  </commentary>\n</example>\n- <example>\n  Context: The user needs comparative analysis of different technologies.\n  user: "Compare the performance metrics of different cloud providers"\n  assistant: "Let me launch the data-analyst agent to gather and analyze performance benchmarks across cloud providers."\n  <commentary>\n  The user needs quantitative comparison of metrics, which requires the data-analyst agent to find benchmark data, create comparisons, and identify statistical differences.\n  </commentary>\n</example>\n- <example>\n  Context: After implementing a new feature, the user wants to analyze its impact.\n  user: "We just launched the new recommendation system. Can you analyze its performance?"\n  assistant: "I'll use the data-analyst agent to examine the performance metrics and identify any significant changes."\n  <commentary>\n  Performance analysis requires statistical evaluation of metrics, trend detection, and data quality assessment - all core capabilities of the data-analyst agent.\n  </commentary>\n</example>

**Tools:** Read, Write, Edit, WebSearch, WebFetch

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/data-analyst.md`

---

### fact-checker

**Description:** Fact verification and source validation specialist. Use PROACTIVELY for claim verification, source credibility assessment, misinformation detection, citation validation, and information accuracy analysis.

**Tools:** Read, Write, Edit, WebSearch, WebFetch

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/fact-checker.md`

---

### nia-oracle

**Description:** Expert research agent specialized in leveraging Nia's knowledge tools. Use PROACTIVELY for discovering repos/docs, deep technical research, remote codebases exploration, documentation queries, and cross-agent knowledge handoffs. Automatically indexes and searches discovered resources.

**Tools:** Read, Grep, Glob, mcp__ide__getDiagnostics, mcp__ide__executeCode, mcp__nia__index, mcp__nia__search_codebase, mcp__nia__regex_search, mcp__nia__search_documentation, mcp__nia__manage_resource, mcp__nia__get_github_file_tree, mcp__nia__nia_web_search, mcp__nia__nia_deep_research_agent, mcp__nia__read_source_content, mcp__nia__nia_package_search_grep, mcp__nia__nia_package_search_hybrid, mcp__nia__nia_package_search_read_file, mcp__nia__nia_bug_report, mcp__nia__context

**Model:** inherit

**File:** `cli-tool/components/agents/deep-research-team/nia-oracle.md`

---

### query-clarifier

**Description:** Use this agent when you need to analyze research queries for clarity and determine if user clarification is needed before proceeding with research. This agent should be invoked at the beginning of research workflows to ensure queries are specific and actionable. Examples: <example>Context: The user has created a query-clarifier agent to analyze research queries for clarity. user: "Tell me about AI" assistant: "I'll use the query-clarifier agent to analyze this query for clarity and determine if we need more specific information." <commentary>Since the query is quite broad and could refer to many aspects of AI, the query-clarifier agent should analyze it and likely request clarification about which specific aspect of AI the user is interested in.</commentary></example> <example>Context: The user has created a query-clarifier agent to ensure research queries are actionable. user: "Compare the performance of different sorting algorithms in terms of time complexity" assistant: "Let me analyze this query with the query-clarifier agent to ensure it's clear and specific enough for research." <commentary>This query is relatively clear but the agent should still analyze it to confirm no clarification is needed before proceeding with the research.</commentary></example>

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/query-clarifier.md`

---

### report-generator

**Description:** Use this agent when you need to transform synthesized research findings into a comprehensive, well-structured final report. This agent excels at creating readable narratives from complex research data, organizing content logically, and ensuring proper citation formatting. It should be used after research has been completed and findings have been synthesized, as the final step in the research process. Examples: <example>Context: The user has completed research on climate change impacts and needs a final report. user: 'I've gathered all this research on climate change effects on coastal cities. Can you create a comprehensive report?' assistant: 'I'll use the report-generator agent to create a well-structured report from your research findings.' <commentary>Since the user has completed research and needs it transformed into a final report, use the report-generator agent to create a comprehensive, properly formatted document.</commentary></example> <example>Context: Multiple research threads have been synthesized and need to be presented cohesively. user: 'We have findings from 5 different researchers on AI safety. Need a unified report.' assistant: 'Let me use the report-generator agent to create a cohesive report that integrates all the research findings.' <commentary>The user needs multiple research streams combined into a single comprehensive report, which is exactly what the report-generator agent is designed for.</commentary></example>

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/report-generator.md`

---

### research-brief-generator

**Description:** Use this agent when you need to transform a user's research query into a structured, actionable research brief that will guide subsequent research activities. This agent takes clarified queries and converts them into comprehensive research plans with specific questions, keywords, source preferences, and success criteria. <example>Context: The user has asked a research question that needs to be structured into a formal research brief.\nuser: "I want to understand the impact of AI on healthcare diagnostics"\nassistant: "I'll use the research-brief-generator agent to transform this query into a structured research brief that will guide our research."\n<commentary>Since we need to create a structured research plan from the user's query, use the research-brief-generator agent to break down the question into specific sub-questions, identify keywords, and define research parameters.</commentary></example><example>Context: After query clarification, we need to create a research framework.\nuser: "How are quantum computers being used in drug discovery?"\nassistant: "Let me use the research-brief-generator agent to create a comprehensive research brief for investigating quantum computing applications in drug discovery."\n<commentary>The query needs to be transformed into a structured brief with specific research questions and parameters, so use the research-brief-generator agent.</commentary></example>

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/research-brief-generator.md`

---

### research-coordinator

**Description:** Use this agent when you need to strategically plan and coordinate complex research tasks across multiple specialist researchers. This agent analyzes research requirements, allocates tasks to appropriate specialists, and defines iteration strategies for comprehensive coverage. <example>Context: The user has asked for a comprehensive analysis of quantum computing applications in healthcare. user: "I need a thorough research report on how quantum computing is being applied in healthcare, including current implementations, future potential, and technical challenges" assistant: "I'll use the research-coordinator agent to plan this complex research task across our specialist researchers" <commentary>Since this requires coordinating multiple aspects (technical, medical, current applications), use the research-coordinator to strategically allocate tasks to different specialist researchers.</commentary></example> <example>Context: The user wants to understand the economic impact of AI on job markets. user: "Research the economic impact of AI on job markets, including statistical data, expert opinions, and case studies" assistant: "Let me engage the research-coordinator agent to organize this multi-faceted research project" <commentary>This requires coordination between data analysis, academic research, and current news, making the research-coordinator ideal for planning the research strategy.</commentary></example>

**Tools:** Read, Write, Edit, Task

**Model:** opus

**File:** `cli-tool/components/agents/deep-research-team/research-coordinator.md`

---

### research-orchestrator

**Description:** Use this agent when you need to coordinate a comprehensive research project that requires multiple specialized agents working in sequence. This agent manages the entire research workflow from initial query clarification through final report generation. <example>Context: User wants to conduct thorough research on a complex topic. user: "I need to research the impact of quantum computing on cryptography" assistant: "I'll use the research-orchestrator agent to coordinate a comprehensive research project on this topic" <commentary>Since this is a complex research request requiring multiple phases and specialized agents, the research-orchestrator will manage the entire workflow.</commentary></example> <example>Context: User has a vague research request that needs clarification and systematic investigation. user: "Tell me about AI safety" assistant: "Let me use the research-orchestrator to coordinate a structured research process on AI safety" <commentary>The broad nature of this query requires orchestration of multiple research phases, making the research-orchestrator the appropriate choice.</commentary></example>

**Tools:** Read, Write, Edit, Task, TodoWrite

**Model:** opus

**File:** `cli-tool/components/agents/deep-research-team/research-orchestrator.md`

---

### research-synthesizer

**Description:** Use this agent when you need to consolidate and synthesize findings from multiple research sources or specialist researchers into a unified, comprehensive analysis. This agent excels at merging diverse perspectives, identifying patterns across sources, highlighting contradictions, and creating structured insights that preserve the complexity and nuance of the original research while making it more accessible and actionable. <example>Context: The user has multiple researchers (academic, web, technical, data) who have completed their individual research on climate change impacts. user: "I have research findings from multiple specialists on climate change. Can you synthesize these into a coherent analysis?" assistant: "I'll use the research-synthesizer agent to consolidate all the findings from your specialists into a comprehensive synthesis." <commentary>Since the user has multiple research outputs that need to be merged into a unified analysis, use the research-synthesizer agent to create a structured synthesis that preserves all perspectives while identifying themes and contradictions.</commentary></example> <example>Context: The user has gathered various research reports on AI safety from different sources and needs them consolidated. user: "Here are 5 different research reports on AI safety. I need a unified view of what they're saying." assistant: "Let me use the research-synthesizer agent to analyze and consolidate these reports into a comprehensive synthesis." <commentary>The user needs multiple research reports merged into a single coherent view, which is exactly what the research-synthesizer agent is designed for.</commentary></example>

**Tools:** Read, Write, Edit

**Model:** opus

**File:** `cli-tool/components/agents/deep-research-team/research-synthesizer.md`

---

### technical-researcher

**Description:** Use this agent when you need to analyze code repositories, technical documentation, implementation details, or evaluate technical solutions. This includes researching GitHub projects, reviewing API documentation, finding code examples, assessing code quality, tracking version histories, or comparing technical implementations. <example>Context: The user wants to understand different implementations of a rate limiting algorithm. user: "I need to implement rate limiting in my API. What are the best approaches?" assistant: "I'll use the technical-researcher agent to analyze different rate limiting implementations and libraries." <commentary>Since the user is asking about technical implementations, use the technical-researcher agent to analyze code repositories and documentation.</commentary></example> <example>Context: The user needs to evaluate a specific open source project. user: "Can you analyze the architecture and code quality of the FastAPI framework?" assistant: "Let me use the technical-researcher agent to examine the FastAPI repository and its technical details." <commentary>The user wants a technical analysis of a code repository, which is exactly what the technical-researcher agent specializes in.</commentary></example>

**Tools:** Read, Write, Edit, WebSearch, WebFetch, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/deep-research-team/technical-researcher.md`

---

## development-team

### backend-architect

**Description:** Backend system architecture and API design specialist. Use PROACTIVELY for RESTful APIs, microservice boundaries, database schemas, scalability planning, and performance optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/backend-architect.md`

---

### cli-ui-designer

**Description:** CLI interface design specialist. Use PROACTIVELY to create terminal-inspired user interfaces with modern web technologies. Expert in CLI aesthetics, terminal themes, and command-line UX patterns.

**Tools:** Read, Write, Edit, MultiEdit, Glob, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/cli-ui-designer.md`

---

### devops-engineer

**Description:** DevOps and infrastructure specialist for CI/CD, deployment automation, and cloud operations. Use PROACTIVELY for pipeline setup, infrastructure provisioning, monitoring, security implementation, and deployment optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/devops-engineer.md`

---

### frontend-developer

**Description:** Frontend development specialist for React applications and responsive design. Use PROACTIVELY for UI components, state management, performance optimization, accessibility implementation, and modern frontend architecture.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/frontend-developer.md`

---

### fullstack-developer

**Description:** Full-stack development specialist covering frontend, backend, and database technologies. Use PROACTIVELY for end-to-end application development, API integration, database design, and complete feature implementation.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/development-team/fullstack-developer.md`

---

### ios-developer

**Description:** Native iOS development specialist with Swift and SwiftUI. Use PROACTIVELY for iOS applications, UIKit/SwiftUI components, Core Data integration, app lifecycle management, and App Store optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/ios-developer.md`

---

### mobile-developer

**Description:** Cross-platform mobile development specialist for React Native and Flutter. Use PROACTIVELY for mobile applications, native integrations, offline sync, push notifications, and cross-platform optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/mobile-developer.md`

---

### ui-ux-designer

**Description:** UI/UX design specialist for user-centered design and interface systems. Use PROACTIVELY for user research, wireframes, design systems, prototyping, accessibility standards, and user experience optimization.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/development-team/ui-ux-designer.md`

---

## development-tools

### code-reviewer

**Description:** Expert code review specialist for quality, security, and maintainability. Use PROACTIVELY after writing or modifying code to ensure high development standards.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/code-reviewer.md`

---

### command-expert

**Description:** CLI command development specialist for the claude-code-templates system. Use PROACTIVELY for command design, argument parsing, task automation, and CLI best practices implementation.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/command-expert.md`

---

### context-manager

**Description:** Context management specialist for multi-agent workflows and long-running tasks. Use PROACTIVELY for complex projects, session coordination, and when context preservation is needed across multiple agents.

**Tools:** Read, Write, Edit, TodoWrite

**Model:** opus

**File:** `cli-tool/components/agents/development-tools/context-manager.md`

---

### debugger

**Description:** Debugging specialist for errors, test failures, and unexpected behavior. Use PROACTIVELY when encountering issues, analyzing stack traces, or investigating system problems.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/debugger.md`

---

### dx-optimizer

**Description:** Developer Experience specialist for tooling, setup, and workflow optimization. Use PROACTIVELY when setting up projects, reducing friction, or improving development workflows and automation.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/dx-optimizer.md`

---

### error-detective

**Description:** Log analysis and error pattern detection specialist. Use PROACTIVELY for debugging issues, analyzing logs, investigating production errors, and identifying system anomalies.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/error-detective.md`

---

### flutter-go-reviewer

**Description:** |

**Tools:** Glob, Grep, Read, WebFetch, TodoWrite, WebSearch, BashOutput, KillBash, ListMcpResourcesTool, ReadMcpResourceTool

**Model:** opus

**File:** `cli-tool/components/agents/development-tools/flutter-go-reviewer.md`

---

### mcp-expert

**Description:** Model Context Protocol (MCP) integration specialist for the cli-tool components system. Use PROACTIVELY for MCP server configurations, protocol specifications, and integration patterns.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/mcp-expert.md`

---

### performance-profiler

**Description:** Performance analysis and optimization specialist. Use PROACTIVELY for performance bottlenecks, memory leaks, load testing, optimization strategies, and system performance monitoring.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/performance-profiler.md`

---

### test-engineer

**Description:** Test automation and quality assurance specialist. Use PROACTIVELY for test strategy, test automation, coverage analysis, CI/CD testing, and quality engineering practices.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/test-engineer.md`

---

### unused-code-cleaner

**Description:** Detects and removes unused code (imports, functions, classes) across multiple languages. Use PROACTIVELY after refactoring, when removing features, or before production deployment.

**Tools:** Read, Write, Edit, Bash, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/development-tools/unused-code-cleaner.md`

---

## devops-infrastructure

### cloud-architect

**Description:** Cloud infrastructure design and optimization specialist for AWS/Azure/GCP. Use PROACTIVELY for infrastructure architecture, Terraform IaC, cost optimization, auto-scaling, and multi-region deployments.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/devops-infrastructure/cloud-architect.md`

---

### deployment-engineer

**Description:** CI/CD and deployment automation specialist. Use PROACTIVELY for pipeline configuration, Docker containers, Kubernetes deployments, GitHub Actions, and infrastructure automation workflows.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/deployment-engineer.md`

---

### devops-troubleshooter

**Description:** Production troubleshooting and incident response specialist. Use PROACTIVELY for debugging issues, log analysis, deployment failures, monitoring setup, and root cause analysis.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/devops-troubleshooter.md`

---

### monitoring-specialist

**Description:** Monitoring and observability infrastructure specialist. Use PROACTIVELY for metrics collection, alerting systems, log aggregation, distributed tracing, SLA monitoring, and performance dashboards.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/monitoring-specialist.md`

---

### network-engineer

**Description:** Network connectivity and infrastructure specialist. Use PROACTIVELY for debugging network issues, load balancer configuration, DNS resolution, SSL/TLS setup, CDN optimization, and traffic analysis.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/network-engineer.md`

---

### security-engineer

**Description:** Security infrastructure and compliance specialist. Use PROACTIVELY for security architecture, compliance frameworks, vulnerability management, security automation, and incident response.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/devops-infrastructure/security-engineer.md`

---

### terraform-specialist

**Description:** Terraform and Infrastructure as Code specialist. Use PROACTIVELY for Terraform modules, state management, IaC best practices, provider configurations, workspace management, and drift detection.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/terraform-specialist.md`

---

### vercel-deployment-specialist

**Description:** Expert in Vercel platform features, edge functions, middleware, and deployment strategies. Use PROACTIVELY for Vercel deployments, performance optimization, and platform configuration.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/devops-infrastructure/vercel-deployment-specialist.md`

---

## documentation

### api-documenter

**Description:** Create OpenAPI/Swagger specs, generate SDKs, and write developer documentation. Handles versioning, examples, and interactive docs. Use PROACTIVELY for API documentation or client library generation.

**Tools:** Read, Write, Edit, Bash

**Model:** haiku

**File:** `cli-tool/components/agents/documentation/api-documenter.md`

---

### changelog-generator

**Description:** Changelog and release notes specialist. Use PROACTIVELY for generating changelogs from git history, creating release notes, and maintaining version documentation.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/documentation/changelog-generator.md`

---

### docusaurus-expert

**Description:** Docusaurus documentation specialist. Use PROACTIVELY when working with Docusaurus documentation for site configuration, content management, theming, build troubleshooting, and deployment setup.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/documentation/docusaurus-expert.md`

---

### technical-writer

**Description:** Technical writing and content creation specialist. Use PROACTIVELY for user guides, tutorials, README files, architecture docs, and improving content clarity and accessibility.

**Tools:** Read, Write, Edit, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/documentation/technical-writer.md`

---

## expert-advisors

### agent-expert

**Description:** |-

**File:** `cli-tool/components/agents/expert-advisors/agent-expert.md`

---

### architect-reviewer

**Description:** Use this agent to review code for architectural consistency and patterns. Specializes in SOLID principles, proper layering, and maintainability. Examples: <example>Context: A developer has submitted a pull request with significant structural changes. user: 'Please review the architecture of this new feature.' assistant: 'I will use the architect-reviewer agent to ensure the changes align with our existing architecture.' <commentary>Architectural reviews are critical for maintaining a healthy codebase, so the architect-reviewer is the right choice.</commentary></example> <example>Context: A new service is being added to the system. user: 'Can you check if this new service is designed correctly?' assistant: 'I'll use the architect-reviewer to analyze the service boundaries and dependencies.' <commentary>The architect-reviewer can validate the design of new services against established patterns.</commentary></example>

**Model:** opus

**File:** `cli-tool/components/agents/expert-advisors/architect-review.md`

---

### dependency-manager

**Description:** Use this agent to manage project dependencies. Specializes in dependency analysis, vulnerability scanning, and license compliance. Examples: <example>Context: A user wants to update all project dependencies. user: 'Please update all the dependencies in this project.' assistant: 'I will use the dependency-manager agent to safely update all dependencies and check for vulnerabilities.' <commentary>The dependency-manager is the right tool for dependency updates and analysis.</commentary></example> <example>Context: A user wants to check for security vulnerabilities in the dependencies. user: 'Are there any known vulnerabilities in our dependencies?' assistant: 'I'll use the dependency-manager to scan for vulnerabilities and suggest patches.' <commentary>The dependency-manager can scan for vulnerabilities and help with remediation.</commentary></example>

**File:** `cli-tool/components/agents/expert-advisors/dependency-manager.md`

---

### documentation-expert

**Description:** Use this agent to create, improve, and maintain project documentation. Specializes in technical writing, documentation standards, and generating documentation from code. Examples: <example>Context: A user wants to add documentation to a new feature. user: 'Please help me document this new API endpoint.' assistant: 'I will use the documentation-expert to generate clear and concise documentation for your API.' <commentary>The documentation-expert is the right choice for creating high-quality technical documentation.</commentary></example> <example>Context: The project's documentation is outdated. user: 'Can you help me update our README file?' assistant: 'I'll use the documentation-expert to review and update the README with the latest information.' <commentary>The documentation-expert can help improve existing documentation.</commentary></example>

**File:** `cli-tool/components/agents/expert-advisors/documentation-expert.md`

---

## ffmpeg-clip-team

### audio-mixer

**Description:** Multi-track audio mixing and mastering specialist. Use PROACTIVELY for complex audio arrangements, track balancing, spatial audio, sound design, and professional audio production.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/audio-mixer.md`

---

### audio-quality-controller

**Description:** Audio quality enhancement and analysis specialist. Use PROACTIVELY for loudness normalization, noise reduction, audio standardization, and broadcast-ready quality control.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/audio-quality-controller.md`

---

### podcast-content-analyzer

**Description:** Podcast content analysis specialist. Use PROACTIVELY for identifying viral moments, creating chapter markers, extracting SEO keywords, and scoring engagement potential from transcripts.

**Tools:** Read

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/podcast-content-analyzer.md`

---

### podcast-metadata-specialist

**Description:** Podcast metadata and show notes specialist. Use PROACTIVELY for SEO-optimized titles, chapter markers, platform-specific descriptions, and comprehensive publishing metadata.

**Tools:** Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/podcast-metadata-specialist.md`

---

### podcast-transcriber

**Description:** Audio transcription specialist. Use PROACTIVELY for extracting accurate transcripts from media files with speaker identification, timestamps, and structured output.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/podcast-transcriber.md`

---

### social-media-clip-creator

**Description:** Social media video clip optimization specialist. Use PROACTIVELY for creating platform-specific clips with proper aspect ratios, subtitles, thumbnails, and encoding optimization.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/social-media-clip-creator.md`

---

### timestamp-precision-specialist

**Description:** Frame-accurate timestamp extraction specialist. Use PROACTIVELY for precise cut points, speech boundary detection, silence analysis, and professional podcast editing timestamps.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/timestamp-precision-specialist.md`

---

### video-editor

**Description:** Video editing and production specialist. Use PROACTIVELY for video cuts, transitions, effects, color correction, multi-track editing, and professional video assembly using FFmpeg.

**Tools:** Bash, Read, Write

**Model:** opus

**File:** `cli-tool/components/agents/ffmpeg-clip-team/video-editor.md`

---

## game-development

### 3d-artist

**Description:** 3D art and asset creation specialist for game development. Use PROACTIVELY for 3D modeling, texturing, animation, asset optimization, and technical art workflows for Unity and Unreal Engine.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/game-development/3d-artist.md`

---

### game-designer

**Description:** Game design specialist focusing on mechanics, balancing, player psychology, and system design. Use PROACTIVELY for gameplay mechanics, progression systems, difficulty curves, and user experience optimization.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/game-development/game-designer.md`

---

### unity-game-developer

**Description:** Expert Unity game developer specializing in C# scripting, 3D graphics, mobile optimization, and complete game development workflows. Handles Unity physics, UI systems, asset optimization, and cross-platform deployment. Use PROACTIVELY for Unity projects, performance optimization, and game architecture decisions.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/game-development/unity-game-developer.md`

---

### unreal-engine-developer

**Description:** Expert Unreal Engine developer specializing in C++ programming, Blueprint visual scripting, and AAA game development. Handles Unreal's rendering pipeline, multiplayer systems, and performance optimization. Use PROACTIVELY for Unreal projects, engine modifications, or high-performance game development.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/game-development/unreal-engine-developer.md`

---

## git

### git-flow-manager

**Description:** Git Flow workflow manager. Use PROACTIVELY for Git Flow operations including branch creation, merging, validation, release management, and pull request generation. Handles feature, release, and hotfix branches.

**Tools:** Read, Bash, Grep, Glob, Edit, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/git/git-flow-manager.md`

---

## mcp-dev-team

### mcp-deployment-orchestrator

**Description:** MCP server deployment and operations specialist. Use PROACTIVELY for containerization, Kubernetes deployments, autoscaling, monitoring, security hardening, and production operations.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-deployment-orchestrator.md`

---

### mcp-integration-engineer

**Description:** MCP server integration and orchestration specialist. Use PROACTIVELY for client-server integration, multi-server orchestration, workflow automation, and system architecture design.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-integration-engineer.md`

---

### mcp-protocol-specialist

**Description:** MCP protocol specification and standards specialist. Use PROACTIVELY for protocol design, specification compliance, transport implementation, and maintaining standards across the ecosystem.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-protocol-specialist.md`

---

### mcp-registry-navigator

**Description:** MCP registry discovery and integration specialist. Use PROACTIVELY for finding servers, evaluating capabilities, generating configurations, and publishing to registries.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-registry-navigator.md`

---

### mcp-security-auditor

**Description:** MCP server security specialist. Use PROACTIVELY for security reviews, OAuth implementation, RBAC design, compliance frameworks, and vulnerability assessment.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-security-auditor.md`

---

### mcp-server-architect

**Description:** MCP server architecture and implementation specialist. Use PROACTIVELY for designing servers, implementing transport layers, tool definitions, completion support, and protocol compliance.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-server-architect.md`

---

### mcp-testing-engineer

**Description:** MCP server testing and quality assurance specialist. Use PROACTIVELY for protocol compliance, security testing, performance evaluation, and debugging MCP implementations.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/mcp-dev-team/mcp-testing-engineer.md`

---

## modernization

### architecture-modernizer

**Description:** Software architecture modernization specialist. Use PROACTIVELY for monolith decomposition, microservices design, event-driven architecture, and scalability improvements.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/modernization/architecture-modernizer.md`

---

### cloud-migration-specialist

**Description:** Cloud migration and infrastructure modernization specialist. Use PROACTIVELY for on-premise to cloud migrations, containerization, serverless adoption, and cloud-native transformations.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/modernization/cloud-migration-specialist.md`

---

### legacy-modernizer

**Description:** Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility. Use PROACTIVELY for legacy system updates, framework migrations, or technical debt reduction.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/modernization/legacy-modernizer.md`

---

## obsidian-ops-team

### connection-agent

**Description:** Obsidian vault connection specialist. Use PROACTIVELY for analyzing and suggesting links between related content, identifying orphaned notes, and creating knowledge graph connections.

**Tools:** Read, Grep, Bash, Write, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/connection-agent.md`

---

### content-curator

**Description:** Obsidian content curation and quality specialist. Use PROACTIVELY for identifying outdated content, suggesting content improvements, consolidating similar notes, and maintaining content quality standards.

**Tools:** Read, Write, Edit, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/content-curator.md`

---

### metadata-agent

**Description:** Obsidian metadata management specialist. Use PROACTIVELY for frontmatter standardization, metadata addition, and ensuring consistent file metadata across the vault.

**Tools:** Read, MultiEdit, Bash, Glob, LS

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/metadata-agent.md`

---

### moc-agent

**Description:** Obsidian Map of Content specialist. Use PROACTIVELY for identifying and generating missing MOCs, organizing orphaned assets, and maintaining navigation structure.

**Tools:** Read, Write, Bash, LS, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/moc-agent.md`

---

### review-agent

**Description:** Obsidian vault quality assurance specialist. Use PROACTIVELY for cross-checking enhancement work, validating consistency, and ensuring quality across the vault.

**Tools:** Read, Grep, LS

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/review-agent.md`

---

### tag-agent

**Description:** Obsidian tag taxonomy specialist. Use PROACTIVELY for normalizing and hierarchically organizing tag taxonomy, consolidating duplicates, and maintaining consistent tagging.

**Tools:** Read, MultiEdit, Bash, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/tag-agent.md`

---

### vault-optimizer

**Description:** Obsidian vault performance optimization specialist. Use PROACTIVELY for analyzing vault performance, optimizing file sizes, managing large attachments, and improving search indexing.

**Tools:** Read, Write, Bash, Glob, LS

**Model:** sonnet

**File:** `cli-tool/components/agents/obsidian-ops-team/vault-optimizer.md`

---

## ocr-extraction-team

### document-structure-analyzer

**Description:** Document structure analysis specialist. Use PROACTIVELY for identifying document layouts, analyzing content hierarchy, and mapping visual elements to semantic structure before OCR processing.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/document-structure-analyzer.md`

---

### markdown-syntax-formatter

**Description:** Markdown formatting specialist. Use PROACTIVELY for converting text to proper markdown syntax, fixing formatting issues, and ensuring consistent document structure.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/markdown-syntax-formatter.md`

---

### ocr-grammar-fixer

**Description:** OCR text correction specialist. Use PROACTIVELY for cleaning up and correcting OCR-processed text, fixing character recognition errors, and ensuring proper grammar while maintaining original meaning.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/ocr-grammar-fixer.md`

---

### ocr-preprocessing-optimizer

**Description:** OCR preprocessing and image optimization specialist. Use PROACTIVELY for image enhancement, noise reduction, skew correction, and optimizing image quality for maximum OCR accuracy.

**Tools:** Read, Write, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/ocr-preprocessing-optimizer.md`

---

### ocr-quality-assurance

**Description:** OCR pipeline validation specialist. Use PROACTIVELY for final review and validation of OCR-corrected text against original sources, ensuring accuracy and completeness in the correction pipeline.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/ocr-quality-assurance.md`

---

### text-comparison-validator

**Description:** Text comparison and validation specialist. Use PROACTIVELY for comparing extracted text with existing files, detecting discrepancies, and ensuring accuracy between two text sources.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/text-comparison-validator.md`

---

### visual-analysis-ocr

**Description:** Visual analysis and OCR specialist. Use PROACTIVELY for extracting and analyzing text content from images while preserving formatting, structure, and converting visual hierarchy to markdown.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/ocr-extraction-team/visual-analysis-ocr.md`

---

## performance-testing

### load-testing-specialist

**Description:** Load testing and stress testing specialist. Use PROACTIVELY for creating comprehensive load test scenarios, analyzing performance under stress, and identifying system bottlenecks and capacity limits.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/performance-testing/load-testing-specialist.md`

---

### performance-engineer

**Description:** Profile applications, optimize bottlenecks, and implement caching strategies. Handles load testing, CDN setup, and query optimization. Use PROACTIVELY for performance issues or optimization tasks.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/performance-testing/performance-engineer.md`

---

### react-performance-optimization

**Description:** React performance optimization specialist. Use PROACTIVELY for identifying and fixing performance bottlenecks, bundle optimization, rendering optimization, and memory leak resolution.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/performance-testing/react-performance-optimization.md`

---

### test-automator

**Description:** Create comprehensive test suites with unit, integration, and e2e tests. Sets up CI pipelines, mocking strategies, and test data. Use PROACTIVELY for test coverage improvement or test automation setup.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/performance-testing/test-automator.md`

---

### web-vitals-optimizer

**Description:** Core Web Vitals optimization specialist. Use PROACTIVELY for improving LCP, FID, CLS, and other web performance metrics to enhance user experience and search rankings.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/performance-testing/web-vitals-optimizer.md`

---

## podcast-creator-team

### academic-research-synthesizer

**Description:** Academic research synthesis specialist. Use PROACTIVELY for comprehensive research on academic topics, literature reviews, technical investigations, and well-cited analysis combining multiple sources.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/academic-research-synthesizer.md`

---

### comprehensive-researcher

**Description:** Comprehensive research specialist. Use PROACTIVELY for in-depth research on any topic, requiring multiple sources, cross-verification, and structured reports with citations.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/comprehensive-researcher.md`

---

### episode-orchestrator

**Description:** Episode workflow orchestrator. Use PROACTIVELY for managing episode-based workflows that coordinate multiple specialized agents in sequence, with payload validation and conditional routing.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/episode-orchestrator.md`

---

### guest-outreach-coordinator

**Description:** Podcast guest outreach and coordination specialist. Use PROACTIVELY for guest research, outreach templates, interview scheduling, pre-interview preparation, and guest relationship management.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/guest-outreach-coordinator.md`

---

### market-research-analyst

**Description:** Market research and competitive analysis specialist. Use PROACTIVELY for comprehensive market intelligence, industry trends, competitive analysis, and strategic business insights.

**Tools:** Read, Write, Edit, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/market-research-analyst.md`

---

### podcast-editor

**Description:** Podcast editing and post-production specialist. Use PROACTIVELY for audio editing guidance, show notes creation, chapter markers, timestamp management, and podcast publishing workflows.

**Tools:** Read, Write, Edit

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/podcast-editor.md`

---

### podcast-trend-scout

**Description:** Podcast trend analysis specialist. Use PROACTIVELY for identifying emerging tech topics, breaking developments, and timely content suggestions for podcast episodes.

**Tools:** Read, Write, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/podcast-trend-scout.md`

---

### project-supervisor-orchestrator

**Description:** Project workflow orchestrator. Use PROACTIVELY for managing complex multi-step workflows that coordinate multiple specialized agents in sequence with intelligent routing and payload validation.

**Tools:** Read, Write

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/project-supervisor-orchestrator.md`

---

### seo-podcast-optimizer

**Description:** SEO podcast optimization specialist. Use PROACTIVELY for creating SEO-friendly titles, meta descriptions, and identifying relevant keywords for podcast episodes.

**Tools:** Read, Write, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/seo-podcast-optimizer.md`

---

### social-media-copywriter

**Description:** Social media content creation specialist. Use PROACTIVELY for creating Twitter threads, LinkedIn posts, and Instagram captions from podcast episode information for maximum engagement.

**Tools:** Read, Write, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/social-media-copywriter.md`

---

### twitter-ai-influencer-manager

**Description:** Twitter AI influencer engagement specialist. Use PROACTIVELY for interacting with AI thought leaders, posting AI-focused tweets, analyzing influencer content, and managing AI community engagement.

**Tools:** Read, Write, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/podcast-creator-team/twitter-ai-influencer-manager.md`

---

## programming-languages

### c-pro

**Description:** Write efficient C code with proper memory management, pointer arithmetic, and system calls. Handles embedded systems, kernel modules, and performance-critical code. Use PROACTIVELY for C optimization, memory issues, or system programming.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/c-pro.md`

---

### c-sharp-pro

**Description:** Write idiomatic C# code with modern language features, async patterns, and LINQ. Masters .NET ecosystem, Entity Framework Core, and ASP.NET Core. Use PROACTIVELY for C# optimization, refactoring, or complex .NET solutions.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/c-sharp-pro.md`

---

### cpp-pro

**Description:** Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization. Use PROACTIVELY for C++ refactoring, memory safety, or complex C++ patterns.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/cpp-pro.md`

---

### golang-pro

**Description:** Write idiomatic Go code with goroutines, channels, and interfaces. Optimizes concurrency, implements Go patterns, and ensures proper error handling. Use PROACTIVELY for Go refactoring, concurrency issues, or performance optimization.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/golang-pro.md`

---

### javascript-pro

**Description:** Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. Use PROACTIVELY for JavaScript optimization, async debugging, or complex JS patterns.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/javascript-pro.md`

---

### php-pro

**Description:** Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP applications.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/php-pro.md`

---

### python-pro

**Description:** Write idiomatic Python code with advanced features like decorators, generators, and async/await. Optimizes performance, implements design patterns, and ensures comprehensive testing. Use PROACTIVELY for Python refactoring, optimization, or complex Python features.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/python-pro.md`

---

### rust-pro

**Description:** Write idiomatic Rust with ownership patterns, lifetimes, and trait implementations. Masters async/await, safe concurrency, and zero-cost abstractions. Use PROACTIVELY for Rust memory safety, performance optimization, or systems programming.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/rust-pro.md`

---

### shell-scripting-pro

**Description:** Write robust shell scripts with proper error handling, POSIX compliance, and automation patterns. Masters bash/zsh features, process management, and system integration. Use PROACTIVELY for automation, deployment scripts, or system administration tasks.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/shell-scripting-pro.md`

---

### sql-pro

**Description:** Write complex SQL queries, optimize execution plans, and design normalized schemas. Masters CTEs, window functions, and stored procedures. Use PROACTIVELY for query optimization, complex joins, or database design.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/sql-pro.md`

---

### typescript-pro

**Description:** Write idiomatic TypeScript with advanced type system features, strict typing, and modern patterns. Masters generic constraints, conditional types, and type inference. Use PROACTIVELY for TypeScript optimization, complex types, or migration from JavaScript.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/programming-languages/typescript-pro.md`

---

## realtime

### supabase-realtime-optimizer

**Description:** Supabase realtime performance specialist. Use PROACTIVELY to optimize realtime subscriptions, debug connection issues, and improve realtime application performance.

**Tools:** Read, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/realtime/supabase-realtime-optimizer.md`

---

## security

### api-security-audit

**Description:** API security audit specialist. Use PROACTIVELY for REST API security audits, authentication vulnerabilities, authorization flaws, injection attacks, and compliance validation.

**Tools:** Read, Write, Edit, Bash

**Model:** sonnet

**File:** `cli-tool/components/agents/security/api-security-audit.md`

---

### compliance-specialist

**Description:** Security compliance and regulatory framework specialist. Use PROACTIVELY for compliance assessments, regulatory requirements, audit preparation, and governance implementation.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/security/compliance-specialist.md`

---

### incident-responder

**Description:** Handles production incidents with urgency and precision. Use IMMEDIATELY when production issues occur. Coordinates debugging, implements fixes, and documents post-mortems.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/security/incident-responder.md`

---

### penetration-tester

**Description:** Penetration testing and ethical hacking specialist. Use PROACTIVELY for security assessments, vulnerability exploitation, network penetration, and security posture evaluation.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/security/penetration-tester.md`

---

### security-auditor

**Description:** Review code for vulnerabilities, implement secure authentication, and ensure OWASP compliance. Handles JWT, OAuth2, CORS, CSP, and encryption. Use PROACTIVELY for security reviews, auth flows, or vulnerability fixes.

**Tools:** Read, Write, Edit, Bash

**Model:** opus

**File:** `cli-tool/components/agents/security/security-auditor.md`

---

## web-tools

### nextjs-architecture-expert

**Description:** Master of Next.js best practices, App Router, Server Components, and performance optimization. Use PROACTIVELY for Next.js architecture decisions, migration strategies, and framework optimization.

**Tools:** Read, Write, Edit, Bash, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/nextjs-architecture-expert.md`

---

### react-performance-optimizer

**Description:** Specialist in React performance patterns, bundle optimization, and Core Web Vitals. Use PROACTIVELY for React app performance tuning, rendering optimization, and production performance monitoring.

**Tools:** Read, Write, Edit, Bash, Grep

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/react-performance-optimizer.md`

---

### seo-analyzer

**Description:** SEO analysis and optimization specialist. Use PROACTIVELY for technical SEO audits, meta tag optimization, performance analysis, and search engine optimization recommendations.

**Tools:** Read, Write, WebFetch, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/seo-analyzer.md`

---

### url-context-validator

**Description:** URL validation and contextual analysis specialist. Use PROACTIVELY for validating links not just for functionality but also for contextual appropriateness and alignment with surrounding content.

**Tools:** Read, Write, WebFetch, WebSearch

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/url-context-validator.md`

---

### url-link-extractor

**Description:** URL and link extraction specialist. Use PROACTIVELY for finding, extracting, and cataloging all URLs and links within website codebases, including internal links, external links, API endpoints, and asset references.

**Tools:** Read, Write, Grep, Glob, LS

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/url-link-extractor.md`

---

### web-accessibility-checker

**Description:** Web accessibility compliance specialist. Use PROACTIVELY for WCAG compliance audits, accessibility testing, screen reader compatibility, and inclusive design validation.

**Tools:** Read, Write, Grep, Glob

**Model:** sonnet

**File:** `cli-tool/components/agents/web-tools/web-accessibility-checker.md`

---

