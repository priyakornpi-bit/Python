import json

# Load the notebook
with open('/Users/tonton210/Python/Gemini teach me Python/Pyhton_Basic.ipynb', 'r') as f:
    notebook = json.load(f)

# Collect all markdown sources
markdown_sources = []
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        # Join the source lines
        source_text = ''.join(cell['source'])
        markdown_sources.append(source_text)

# Concatenate with double newlines
concatenated = '\n\n'.join(markdown_sources)

# Create new cell
new_cell = {
    "cell_type": "markdown",
    "id": "merged_markdown",  # or keep some id
    "metadata": {},
    "source": [concatenated]
}

# Update notebook
notebook['cells'] = [new_cell]

# Write back
with open('/Users/tonton210/Python/Gemini teach me Python/Pyhton_Basic.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)