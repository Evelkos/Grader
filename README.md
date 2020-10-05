# Grader

## Installation
1. Install pyenv - https://github.com/pyenv/pyenv-installer ( $ curl https://pyenv.run | bash )
2. Install poetry - https://poetry.eustace.io/docs/#introduction
3. Go to `<repository>/src` folder
4. [Optional] Force poetry to create venv inside the repository:
```
poetry config virtualenvs.in-project true
```
5. Install Python 3.7.2
```
sh
$ pyenv install 3.7.2
$ pyenv local 3.7.2  # Activate Python 3.7.2 for the current project
```
6. Install dependencies with poetry
```
poetry install
```

You can find required packages in '''pyproject.toml''' file.


## Database model

```
+---------------+      +-------------+
|   Candidate   |      |  Recruiter  |
+---------------+      +-------------+
|pk             |      |pk           |
|first_name     |      |first_name   |
|last_name      |      |last_name    |
+-------+-------+      +------+------+
        ^                     ^
        |                     |
        |                     |
        |                     |
+-------+------+              |
|    Grade     +--------------+
+--------------+
|pk            |          +----------+
|value         |          |   Task   |
|task          |          +----------+
|candidate     +--------->+pk        |
|recruiter     |          |title     |
+--------------+          +----------+
```


## Pages
1. /api/add-mark/ - add new grade (you need to create candidate, recruiter and task first)
2. /api/get-candidates/ - show list of candidates, their grades and average grades

Warning: To add new candidate, recruiter or task you need to use Django Admin page.