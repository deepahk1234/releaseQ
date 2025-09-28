import json

# Data structure for the dashboard
dashboard_data = {
    "performance_metrics": {
        "response_time": {"current": 245, "target": "<300ms", "unit": "ms", "status": "pass"},
        "throughput": {"current": 1200, "target": ">1000", "unit": "req/s", "status": "pass"},
        "error_rate": {"current": 0.02, "target": "<0.1%", "unit": "%", "status": "fail"},
        "memory_usage": {"current": 78, "target": "<80%", "unit": "%", "status": "pass"}
    },
    "technical_debt": {
        "total_debt": 13.1,
        "breakdown": [
            {"priority": "High", "value": 2.1, "unit": "h"},
            {"priority": "Medium", "value": 4.2, "unit": "h"},
            {"priority": "Low", "value": 6.8, "unit": "h"}
        ]
    },
    "code_quality": {
        "trends": {'v2.1': 58, 'v2.2': 65, 'v2.3': 68, 'v2.4': 72, 'v2.5': 75, 'v2.6': 80},
        "improvement": 22
    },
    "testing_qa": {
        "test_coverage": {
            "Unit Tests": 82,
            "Integration": 74,
            "E2E Tests": 65,
            "API Tests": 91
        }
    },
    "audit_trail": {
        "action_items": [
            "Address medium priority security findings by 2024-10-01",
            "Increase E2E test coverage to 75% by 2024-10-15",
            "Complete SOC 2 compliance documentation",
            "Resolve performance regression in data processing"
        ]
    }
}

# --- Rst/HTML Report Generation ---

def _generate_metric_card(title, metric):
    """Generates HTML for a single metric card."""
    status_class = "card-status-pass" if metric['status'] == 'pass' else "card-status-fail"
    return f"""
    <div class="card">
        <div class="card-title">{title.replace('_', ' ').title()}</div>
        <div class="card-content">{metric['current']}{metric['unit']}</div>
        <div class="card-target">Target: {metric['target']} <span class="{status_class}">●</span></div>
    </div>
    """

def _generate_progress_bar(label, value, max_value=100):
    """Generates HTML for a progress bar."""
    percentage = (value / max_value) * 100
    return f"""
    <div class="progress-bar-container">
        <div class="progress-bar-label">
            <span>{label}</span>
            <span>{value}%</span>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width: {percentage}%;"></div>
        </div>
    </div>
    """

def _generate_bar_chart(data):
    """Generates a simple HTML/CSS bar chart."""
    max_val = max(data.values())
    chart_html = '<div class="bar-chart-container">'
    for label, value in data.items():
        height = (value / max_val) * 100
        chart_html += f"""
        <div class="bar-chart-bar" style="height: {height}%;">
            <div class="value">{value}</div>
            <div class="label">{label}</div>
        </div>
        """
    chart_html += '</div>'
    return chart_html

def generate_rst_report_visual(data):
    """Generates a reStructuredText report with embedded HTML for visual components."""

    report = "====================================\n"
    report += "Development Quality Dashboard Report\n"
    report += "====================================\n\n"

    # --- Performance Metrics ---
    report += "Key Performance Metrics\n"
    report += "-----------------------\n\n"
    report += ".. raw:: html\n\n"
    report += '   <div class="card-grid">\n'
    for title, metric in data["performance_metrics"].items():
        report += "      " + _generate_metric_card(title, metric).replace('\n', '\n      ')
    report += '   </div>\n\n'

    # --- Test Coverage ---
    report += "Test Coverage\n"
    report += "-------------\n\n"
    report += ".. raw:: html\n\n"
    report += '   <div class="card">\n'
    report += '      <div class="card-title">Overall Test Coverage</div>\n'
    for label, value in data["testing_qa"]["test_coverage"].items():
        report += "      " + _generate_progress_bar(label, value).replace('\n', '\n      ')
    report += '   </div>\n\n'

    # --- Code Quality Trends ---
    report += "Code Quality Trends\n"
    report += "-------------------\n\n"
    report += ".. raw:: html\n\n"
    report += '   <div class="card">\n'
    report += '      <div class="card-title">Quality Score Over Versions</div>\n'
    report += "      " + _generate_bar_chart(data["code_quality"]["trends"]).replace('\n', '\n      ')
    report += '   </div>\n\n'

    # --- Action Items ---
    report += "Action Items\n"
    report += "------------\n\n"
    report += ".. raw:: html\n\n"
    report += '   <div class="card">\n'
    report += '      <div class="card-title">Pending Action Items</div>\n'
    report += '      <ul class="styled-list">\n'
    for item in data["audit_trail"]["action_items"]:
        report += f'         <li>{item}</li>\n'
    report += '      </ul>\n'
    report += '   </div>\n\n'

    return report

# --- Markdown Report Generation ---

def _create_md_progress_bar(value, length=20):
    """Creates a text-based progress bar for Markdown."""
    filled_len = int(length * value / 100)
    bar = '█' * filled_len + '░' * (length - filled_len)
    return f"`{bar}`"

def generate_md_report_visual(data):
    """Generates a visually enhanced Markdown report."""
    report = "# Development Quality Dashboard\n\n"

    # --- Performance Metrics ---
    report += "## 📊 Key Performance Metrics\n\n"
    report += "| Metric          | Current   | Target   | Status |\n"
    report += "|-----------------|-----------|----------|--------|\n"
    for title, metric in data["performance_metrics"].items():
        status_emoji = '✅' if metric['status'] == 'pass' else '⚠️'
        report += f"| {title.replace('_', ' ').title()} | {metric['current']}{metric['unit']} | {metric['target']} | {status_emoji} |\n"
    report += "\n"

    # --- Test Coverage ---
    report += "## 🧪 Test Coverage\n\n"
    report += "| Area        | Coverage | Visualisation      |\n"
    report += "|-------------|----------|--------------------|\n"
    for label, value in data["testing_qa"]["test_coverage"].items():
        bar = _create_md_progress_bar(value)
        report += f"| {label} | {value}%    | {bar} |\n"
    report += "\n"

    # --- Code Quality Trends ---
    report += "## 📈 Code Quality Trends\n\n"
    report += "| Version | Score | Trend                |\n"
    report += "|---------|-------|----------------------|\n"
    for version, score in data["code_quality"]["trends"].items():
        bar = _create_md_progress_bar(score, length=25)
        report += f"| {version}   | {score}    | {bar} |\n"
    report += "\n"

    # --- Action Items ---
    report += "## 📋 Action Items\n\n"
    for item in data["audit_trail"]["action_items"]:
        report += f"- [ ] {item}\n"
    report += "\n"

    return report


if __name__ == "__main__":
    # Generate the visual RST/HTML report
    rst_report = generate_rst_report_visual(dashboard_data)
    with open("docs/report.rst", "w") as f:
        f.write(rst_report)
    print("Successfully generated visual report at docs/report.rst")

    # Generate the visual Markdown report
    md_report = generate_md_report_visual(dashboard_data)
    with open("report.md", "w") as f:
        f.write(md_report)
    print("Successfully generated visual report at report.md")