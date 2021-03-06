# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ main ]
  schedule:
    - cron: "* * 7 * *"

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@master
      name: settingup
    - name: Set up Python
      run: |
        cd ${GITHUB_WORKSPACE}/
        python main.py
    - name: 🚀 Deploy
      run: |
          git config user.name "${GITHUB_ACTOR}"
          git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
          git add .
          git commit -am "feat(auto generate): Updated content"
          git push --all -f https://${{ secrets.GITHUB_TOKEN }}@github.com/${GITHUB_REPOSITORY}.git
