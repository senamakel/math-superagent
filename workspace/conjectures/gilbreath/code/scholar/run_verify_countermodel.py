# Scholar run artifacts: not execution artifacts.
# This runner is a HANDBOFF for tool_builder -- scholar has no execution tool.
# It will run code/scholar/verify_countermodel_only.py and capture to
# code/out/verify_two_point_countermodel.captured.txt. Do not treat the
# .captured.txt as existing until tool_builder runs it.
import os
os.chdir('/workspace')
