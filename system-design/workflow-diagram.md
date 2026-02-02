# Workflow Diagram: Public Feedback Analyzer

## ASCII Diagram

[Community Feedback Form / CSV]
                │
                ▼
         [Airtable Table]
      (Raw feedback stored here)
                │
                ▼
        [Make.com Scenario]
  - Trigger: New record in Airtable
  - Action: Send Feedback_Text to LLM
                │
                ▼
          [LLM Processing]
  - Categorizes messages
  - Summarizes key concerns
  - Flags urgent issues
                │
                ▼
       [Airtable Summary Table]
  - Stores structured insights
  - Adds 'Summary' column
                │
                ▼
        [Markdown Report / Results]
  - insights_report.md
  - Decision-makers can read summaries

## Step-by-Step Explanation

1. **Community Feedback Form / CSV**
   - Users submit messages via forms or CSV import.

2. **Airtable Table**
   - Acts as the database for raw feedback.
   - Stores: Feedback_Text, Category, Location, Date, Status.

3. **Make.com Scenario**
   - Low-code automation triggers every time a new record is added.
   - Sends the feedback text to the LLM for processing.

4. **LLM Processing**
   - Uses the prompt to summarize and categorize messages.
   - Flags urgent issues.

5. **Airtable Summary Table**
   - Stores the AI-generated summaries.
   - Keeps the original data for reference.

6. **Markdown Report / Results**
   - Outputs structured insights in `results/insights_report.md`.
   - Can be shared or pushed to GitHub.
