# Architecture Decision Record
Date: 2026-06-29

Status: Accepted

Context
	We need to process data from four sources (CSV, JSON, text, Excel) for Newham Public Library. The data has quality issues and needs to be cleaned before it can be used for analysis.

Decision
We will use a medallion architecture with three layers:

	Bronze - raw data ingested exactly as received
	Silver - cleaned and validated data
	Gold - analysis-ready aggregations
Reasons
	We are going to use medallion architecture in order to progressively refine our data as it moves along a pipeline.
	This allows us to create an easy to understand and debug process that can be run arbitrarily to recreate issues or to fix issues when needed.
Consequences
	Raw data is always preserved in bronze - we can reprocess if cleaning logic changes
	Silver is the trust boundary - gold always reads from silver, never bronze
