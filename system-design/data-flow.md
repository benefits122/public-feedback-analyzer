# Data Flow: Public Feedback Analyzer

## Overview
This system collects community feedback, analyzes it using NLP and LLM, 
and produces structured insights for decision-makers.

## Step-by-Step Workflow

1. **Input Collection**
   - Feedback messages collected via Airtable (or Google Form).
   - Each entry includes: Feedback_Text, Category, Location, Date, Status.

2. **Automation Trigger**
   - Make.com scenario triggers when a new record is added.
   - Sends Feedback_Text to the LLM API for processing.

3. **LLM Processing**
   - LLM categorizes messages, summarizes key concerns, and flags urgent issues.
   - Uses a pre-defined prompt stored in `prompts/feedback_analysis_prompt.md`.

4. **Storage of Insights**
   - LLM output is saved back in Airtable in a `Summary` column.
   - Airtable tables now contain raw feedback + structured summaries.

5. **Output / Reporting**
   - Structured insights are exported to Markdown (`results/insights_report.md`) or dashboards.
   - Decision-makers can view categorized summaries and urgent issues at a glance.

