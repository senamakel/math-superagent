import sys, time
sys.path.insert(0, "/workspace/code")
t = time.time()
exec(open("/workspace/code/out/scholar_oracle_run.py").read())
print("elapsed", round(time.time()-t, 2))
