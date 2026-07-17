from datetime import datetime
import os

# ==========================================
# 1. CORE UTILITY & METRIC FUNCTIONS
# ==========================================

def calculate_health_score(cpu: float, mem: float, disk: float) -> int:
    """
    Calculates a health score from 0-100.
    Deducts:
      - 1 point per % CPU above 60%
      - 1 point per % memory above 70%
      - 2 points per % disk above 80%
    """
    score = 100
    
    if cpu > 60:
        score -= (cpu - 60)
    if mem > 70:
        score -= (mem - 70)
    if disk > 80:
        score -= (disk - 80) * 2
        
    return max(0, int(score))


def classify_server(score: int) -> tuple[str, str]:
    """Returns a tuple of (Status String, Emoji) based on the health score."""
    if score >= 80:
        return "Healthy", "🟢"
    elif score >= 55:
        return "Degraded", "🟡"
    else:
        return "Critical", "🔴"


# ==========================================
# 2. DATA PROCESSING FUNCTIONS
# ==========================================

def generate_server_report(servers: list[dict]) -> list[dict]:
    """Enriches server dictionaries with health scores, status strings, and emojis."""
    enriched_report = []
    for server in servers:
        # Create a shallow copy to prevent mutation of the original data
        s_copy = server.copy()
        
        score = calculate_health_score(s_copy["cpu"], s_copy["mem"], s_copy["disk"])
        status, emoji = classify_server(score)
        
        s_copy["score"] = score
        s_copy["status"] = status
        s_copy["emoji"] = emoji
        
        enriched_report.append(s_copy)
        
    return enriched_report


def summary_by_environment(report: list[dict]) -> dict:
    """Groups report metrics by environment and tallies counts and averages."""
    summary = {}
    
    for s in report:
        env = s["env"]
        if env not in summary:
            summary[env] = {
                "count": 0,
                "total_score": 0,
                "statuses": {"Healthy": 0, "Degraded": 0, "Critical": 0}
            }
            
        summary[env]["count"] += 1
        summary[env]["total_score"] += s["score"]
        summary[env]["statuses"][s["status"]] += 1

    # Format the final dictionary with averages
    final_summary = {}
    for env, data in summary.items():
        final_summary[env] = {
            "server_count": data["count"],
            "avg_score": round(data["total_score"] / data["count"], 1),
            "status_counts": data["statuses"]
        }
        
    return final_summary


# ==========================================
# 3. PRESENTATION FUNCTIONS
# ==========================================

def print_report_header() -> None:
    """Helper to generate a uniform header using os and datetime."""
    monitor_env = os.environ.get("MONITOR_ENV", "local")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 70)
    print(f"SERVER MONITORING REPORT | ENVIRONMENT: {monitor_env.upper()}")
    print(f"Generated at: {timestamp}")
    print("=" * 70)


def print_report(report: list[dict]) -> None:
    """Prints the individual server metrics table using clean f-string padding."""
    print_report_header()
    
    # Table Header
    print(f"{'Server Name':<12} {'Env':<8} {'CPU%':<6} {'MEM%':<6} {'DSK%':<6} {'Score':<6} {'Status':<10}")
    print("-" * 70)
    
    # Table Rows
    for s in report:
        status_display = f"{s['emoji']} {s['status']}"
        print(f"{s['name']:<12} {s['env']:<8} {s['cpu']:<6} {s['mem']:<6} {s['disk']:<6} {s['score']:<6} {status_display:<10}")
    print("\n")


def print_summary(summary: dict) -> None:
    """Prints the environmental rollup metric tables."""
    print("=" * 70)
    print("ENVIRONMENT ROLLUP SUMMARY")
    print("=" * 70)
    
    # Table Header
    print(f"{'Environment':<12} {'Count':<6} {'Avg Score':<10} {'🟢 Healthy':<10} {'🟡 Degraded':<12} {'🔴 Critical':<10}")
    print("-" * 70)
    
    # Table Rows
    for env, data in summary.items():
        sc = data["status_counts"]
        print(f"{env:<12} {data['server_count']:<6} {data['avg_score']:<10} {sc['Healthy']:<10} {sc['Degraded']:<12} {sc['Critical']:<10}")
    print("=" * 70)


# ==========================================
# 4. EXECUTION MAIN ENTRY
# ==========================================

if __name__ == "__main__":
    # Mock source data
    raw_servers = [
        {"name": "web-prod-01", "env": "production",  "cpu": 45, "mem": 65, "disk": 40},
        {"name": "db-prod-01",  "env": "production",  "cpu": 75, "mem": 85, "disk": 85}, # (100 - 15 - 15 - 10) = 60 (Degraded)
        {"name": "api-prod-01", "env": "production",  "cpu": 90, "mem": 95, "disk": 92}, # (100 - 30 - 25 - 24) = 21 (Critical)
        {"name": "web-dev-01",  "env": "development", "cpu": 30, "mem": 40, "disk": 50},
        {"name": "test-node",   "env": "staging",     "cpu": 65, "mem": 72, "disk": 78},
        {"name": "db-dev-01",   "env": "development", "cpu": 55, "mem": 75, "disk": 60},
    ]

    # Process pipeline
    server_report = generate_server_report(raw_servers)
    env_summary = summary_by_environment(server_report)
    
    # Render UI outputs
    print_report(server_report)
    print_summary(env_summary)