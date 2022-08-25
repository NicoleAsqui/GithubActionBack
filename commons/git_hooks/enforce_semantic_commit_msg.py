import re
import sys

ERROR_MSG = """
Commit failed!
Please use semantic commit message format. Examples:
    'feat (developer): name field added to the model'
    'fix: A bug fix'
    'docs: Documentation only changes'
"""

SUCCESS_MSG = "Commit succeed!. Semantic commit message is correct."

COMMIT_MSG_REGEX = r'(feat|fix|style|refactor|perf|test|build|docs)(\([\w\-]+\))?: .*'

# Get the commit message file
with open(sys.argv[1], encoding="utf-8") as commit_msg_file: # The first argument is the file
    commit_msg = commit_msg_file.read()

if re.match(COMMIT_MSG_REGEX, commit_msg) is None:
    print(ERROR_MSG)
    sys.exit(1)

print(SUCCESS_MSG)
sys.exit(0)
