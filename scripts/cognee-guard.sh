#!/bin/sh
# Guarded recycle for the shared Cognee container.
#
# Cognee wedges every few hours: memory climbs toward its 10 GiB cap and the
# HTTP server stops answering, which poisons recall_memory for every run on
# every box until it clears itself. Docker's own health flag does NOT discriminate
# -- it has reported "healthy" with a failing streak of 7 -- so the only trusted
# signal is a probe issued from *inside* the container.
#
# This restarts on that signal alone. It never restarts on memory, on CPU, or on
# a slow-but-answering probe, because those are the normal cycle and a restart
# then would throw away live work.

set -u

# Cognee only, by construction: it watches one named Cognee container. It is a
# launchd/cron job rather than something a launcher calls, so it names the
# engine here rather than reading `MATH_AGENT_MEMORY` from an environment it
# does not have. Under `MATH_AGENT_MEMORY=cortex` nothing should schedule it.

DOCKER=/usr/local/bin/docker
CONTAINER=math-agent-shared-cognee-1
STATE_DIR="$HOME/math-agent-shared/.cognee-guard"
FAIL_FILE="$STATE_DIR/consecutive_failures"
LAST_FILE="$STATE_DIR/last_restart"
HIST_FILE="$STATE_DIR/restart_history"
LOG="$HOME/math-agent-shared/cognee-guard.log"

FAILS_BEFORE_RESTART=2   # ~10 min wedged at a 5-min tick, so a single blip is ignored
COOLDOWN=1800            # no second restart inside 30 min
LOCKOUT_WINDOW=7200      # 3 restarts in 2 h means it is not a wedge
LOCKOUT_COUNT=3
PROBE_TIMEOUT=25

mkdir -p "$STATE_DIR"
now=$(date +%s)
log() { echo "$(date '+%Y-%m-%dT%H:%M:%S') $*" >> "$LOG"; }

read_int() { [ -f "$1" ] && cat "$1" 2>/dev/null || echo 0; }

# --- probe -----------------------------------------------------------------
if ! "$DOCKER" inspect -f '{{.State.Running}}' "$CONTAINER" 2>/dev/null | grep -q true; then
  log "SKIP container not running; compose owns it, not this guard"
  exit 0
fi

probe=$("$DOCKER" exec "$CONTAINER" sh -c \
  "curl -s -o /dev/null -w '%{http_code} %{time_total}' --max-time $PROBE_TIMEOUT http://127.0.0.1:8000/health" \
  2>/dev/null)
code=$(echo "$probe" | awk '{print $1}')
secs=$(echo "$probe" | awk '{print $2}')
[ -z "$code" ] && code=exec-failed

if [ "$code" = "200" ]; then
  prev=$(read_int "$FAIL_FILE")
  if [ "$prev" -gt 0 ]; then
    log "RECOVER probe 200 in ${secs}s after $prev failure(s); no restart needed"
  fi
  echo 0 > "$FAIL_FILE"
  exit 0
fi

fails=$(( $(read_int "$FAIL_FILE") + 1 ))
echo "$fails" > "$FAIL_FILE"
log "FAIL probe=$code timeout=${PROBE_TIMEOUT}s consecutive=$fails"

[ "$fails" -lt "$FAILS_BEFORE_RESTART" ] && exit 0

# --- cooldown --------------------------------------------------------------
last=$(read_int "$LAST_FILE")
if [ "$last" -gt 0 ] && [ $(( now - last )) -lt "$COOLDOWN" ]; then
  log "HOLD restarted $(( (now - last) / 60 ))m ago; cooldown ${COOLDOWN}s not elapsed"
  exit 0
fi

# --- lockout: a restart loop is a different fault, and hammering makes it worse
if [ -f "$HIST_FILE" ]; then
  recent=$(awk -v c=$(( now - LOCKOUT_WINDOW )) '$1 > c' "$HIST_FILE" | wc -l | tr -d ' ')
  if [ "$recent" -ge "$LOCKOUT_COUNT" ]; then
    log "LOCKOUT $recent restarts in the last $(( LOCKOUT_WINDOW / 3600 ))h; refusing to restart again -- needs a human"
    exit 0
  fi
fi

# --- restart ---------------------------------------------------------------
mem=$("$DOCKER" stats --no-stream --format '{{.MemUsage}}' "$CONTAINER" 2>/dev/null)
log "RESTART probe=$code mem=$mem after $fails consecutive failures"
echo "$now" >> "$HIST_FILE"
echo "$now" > "$LAST_FILE"
echo 0 > "$FAIL_FILE"

"$DOCKER" restart "$CONTAINER" >/dev/null 2>&1 || { log "RESTART-ERROR docker restart failed"; exit 1; }

i=0
while [ "$i" -lt 24 ]; do
  sleep 5
  i=$(( i + 1 ))
  after=$("$DOCKER" exec "$CONTAINER" sh -c \
    "curl -s -o /dev/null -w '%{http_code}' --max-time 10 http://127.0.0.1:8000/health" 2>/dev/null)
  if [ "$after" = "200" ]; then
    log "RESTART-OK healthy after $(( i * 5 ))s"
    exit 0
  fi
done
log "RESTART-UNCONFIRMED still not answering 120s after restart"
exit 1
