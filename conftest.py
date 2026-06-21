# FIX: Added with Claude (agent mode). Its presence makes pytest add this project
# root to sys.path during collection, so bare `pytest` can import logic_utils/app
# (not just `python -m pytest`, which adds the cwd automatically).
