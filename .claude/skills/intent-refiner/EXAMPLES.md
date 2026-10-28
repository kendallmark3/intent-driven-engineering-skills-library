# Examples

## Rough request

"Add CSV export to reports. Maybe make a new microservice and put it on a queue."

## Good refinement

Focus on exporting the currently visible report data, preserving authorization, producing valid CSV, and proving row/header correctness. Do not require a microservice or queue unless an actual constraint or later evidence makes that necessary.

## Trigger examples

- "Give me the intent."
- "Turn this into an intent file."
- "Clean this requirement up."
- "Write the success criteria without telling the team how to code it."
