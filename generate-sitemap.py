# .github/workflows/update-sitemap.yml
name: Update Sitemap

on:
  push:
    branches: [ main, master ]
    paths:
      - '*/README.md'
      - '*/index.md'
      - '*/lyrics.txt'
      - 'index.md'
  workflow_dispatch:

jobs:
  update-sitemap:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0  # Get full history for accurate dates
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    
    - name: Generate sitemap
      run: |
        cd songs
        python generate-sitemap.py
    
    - name: Commit and push if changed
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add songs/sitemap.xml
        git diff --quiet && git diff --staged --quiet || (git commit -m "Auto-update sitemap.xml" && git push)
