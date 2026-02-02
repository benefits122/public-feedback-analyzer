# Tech Stack: Public Feedback Analyzer

## Tools Used

1. **Airtable**
   - Stores raw and structured feedback.
   - Serves as database for automation.

2. **Make.com**
   - Low-code automation platform.
   - Triggers LLM requests on new feedback records.
   - Stores output back to Airtable.

3. **LLM (OpenRouter / OpenAI)**
   - Summarizes feedback, categorizes concerns, highlights urgent issues.
   - Prompt documented in `prompts/feedback_analysis_prompt.md`.

4. **Markdown / GitHub**
   - Stores structured insights and documentation.
   - Enables version control and project tracking.

5. **Optional**
   - Google Forms / Tally for input collection.
   - Airtable interfaces for dashboards.
