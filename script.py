import json

# Based on the images I can see, I'll extract the data structure and metrics
dashboard_data = {
    "performance_metrics": {
        "application_performance": {
            "response_time": {"current": 245, "target": 300, "unit": "ms", "status": "pass"},
            "throughput": {"current": 1200, "target": 1000, "unit": "req/s", "status": "pass"},
            "error_rate": {"current": 0.02, "target": 0.1, "unit": "%", "status": "pass"},
            "memory_usage": {"current": 78, "target": 80, "unit": "%", "status": "pass"}
        }
    },
    "technical_debt": {
        "breakdown": {
            "high_priority": {"value": 2.1, "unit": "hours"},
            "medium_priority": {"value": 4.2, "unit": "hours"},
            "low_priority": {"value": 6.8, "unit": "hours"},
            "total_debt": {"value": 13.1, "unit": "hours"}
        },
        "hotspots": [
            {"name": "Authentication Module", "type": "Refactoring needed", "effort": 2.5},
            {"name": "Data Processing", "type": "Performance optimization", "effort": 1.8},
            {"name": "API Gateway", "type": "Code duplication", "effort": 1.2}
        ]
    },
    "code_quality": {
        "trends": {
            "v2.6": 80,
            "v2.5": 75,
            "v2.4": 72,
            "v2.3": 68,
            "v2.2": 65,
            "v2.1": 58
        },
        "improvement": 22,
        "cognitive_complexity": {"current": 1204, "previous": 1189, "change": 15}
    },
    "security_compliance": {
        "standards": {
            "owasp_top10": "Compliant",
            "cwe_top25": "Addressed", 
            "nist_guidelines": "Following",
            "soc2": {"status": "In progress", "completion": 85}
        },
        "dependency_security": {
            "total_dependencies": 142,
            "up_to_date": 134,
            "up_to_date_percentage": 94,
            "minor_updates": 6,
            "major_updates": 2,
            "vulnerabilities": 0
        },
        "security_score": 98,
        "scan_results": {
            "snyk": {"status": "Pass", "critical": 0, "high": 0, "medium": 2, "low": 5},
            "sonarqube": {"status": "Pass", "critical": 0, "high": 1, "medium": 3, "low": 12},
            "owasp_dependency": {"status": "Review", "critical": 0, "high": 0, "medium": 1, "low": 8},
            "codeql": {"status": "Pass", "critical": 0, "high": 0, "medium": 0, "low": 4}
        },
        "vulnerability_summary": {
            "critical": 0,
            "high": 1,
            "medium": 6,
            "low": 29
        }
    },
    "testing_qa": {
        "test_coverage": {
            "unit_tests": 82,
            "integration": 74,
            "e2e_tests": 65,
            "api_tests": 91
        },
        "quality_gates": {
            "build": "Passing (All platforms)",
            "unit_tests": "1,247 tests passed",
            "code_coverage": "Above threshold (80%+)",
            "security_scan": "No critical issues",
            "performance": "1 regression identified",
            "dependencies": "Up to date"
        }
    },
    "sonarqube_metrics": {
        "bugs": {"current": 3, "previous": 7, "change": -4},
        "vulnerabilities": {"current": 1, "previous": 2, "change": -1},
        "code_smells": {"current": 47, "previous": 52, "change": -5},
        "duplicated_lines": {"current": 2.1, "previous": 2.8, "change": -0.7},
        "cognitive_complexity": {"current": 1204, "previous": 1189, "change": 15}
    },
    "audit_trail": {
        "recent_audits": [
            {"type": "Security Audit", "date": "2024-09-15", "status": "Passed"},
            {"type": "Code Review", "date": "2024-09-20", "status": "Approved"},
            {"type": "Penetration Test", "date": "2024-09-10", "status": "Minor findings"},
            {"type": "Compliance Check", "date": "2024-09-18", "status": "Compliant"}
        ],
        "action_items": [
            "Address medium priority security findings by 2024-10-01",
            "Increase E2E test coverage to 75% by 2024-10-15",
            "Complete SOC 2 compliance documentation",
            "Resolve performance regression in data processing"
        ]
    },
    "improvement_goals": {
        "code_coverage": {"current": 85, "target": 90, "owner": "QA Team", "due": "2024-10-30"},
        "security_score": {"current": 98, "target": 100, "owner": "Security Team", "due": "2024-10-15"},
        "technical_debt": {"current": "13.1h", "target": "<10h", "owner": "Dev Team", "due": "2024-11-15"},
        "performance": {"current": "Good", "target": "Excellent", "owner": "Platform Team", "due": "2024-10-30"}
    }
}

def generate_md_report(data):
    """Generates a Markdown report from the dashboard data."""
    report = "# Development Quality Dashboard Report\n\n"

    for section, values in data.items():
        report += f"## {section.replace('_', ' ').title()}\n\n"
        if isinstance(values, dict):
            for key, value in values.items():
                report += f"### {key.replace('_', ' ').title()}\n"
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        report += f"- **{sub_key.replace('_', ' ').title()}:** {sub_value}\n"
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            report += "- " + ", ".join([f"{k.replace('_', ' ').title()}: {v}" for k, v in item.items()]) + "\n"
                        else:
                            report += f"- {item}\n"
                else:
                    report += f"- {value}\n"
                report += "\n"
        report += "\n"

    return report

def _create_rst_table(headers, data_rows):
    """A helper function to create a reStructuredText simple table."""
    if not data_rows:
        return ""

    widths = [len(h) for h in headers]
    for row in data_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    separator = ' '.join('=' * w for w in widths)
    header = ' '.join(h.ljust(w) for h, w in zip(headers, widths))
    rows = [' '.join(str(cell).ljust(w) for cell, w in zip(row_data, widths)) for row_data in data_rows]

    return f"{separator}\n{header}\n{separator}\n" + '\n'.join(rows) + f"\n{separator}\n\n"

def generate_rst_report(data):
    """Generates a reStructuredText report from the dashboard data with tables."""
    report = "====================================\n"
    report += "Development Quality Dashboard Report\n"
    report += "====================================\n\n"

    # --- Performance Metrics ---
    report += "Performance Metrics\n-------------------\n\n"
    perf_data = data.get("performance_metrics", {}).get("application_performance", {})
    report += _create_rst_table(
        ["Metric", "Current", "Target", "Status"],
        [[k.replace('_', ' ').title(), f"{v.get('current', '')}{v.get('unit', '')}", v.get('target', ''), v.get('status', '')] for k, v in perf_data.items()]
    )

    # --- Technical Debt ---
    report += "Technical Debt\n--------------\n\n"
    debt_breakdown = data.get("technical_debt", {}).get("breakdown", {})
    report += "Breakdown\n~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Priority", "Value (hours)"],
        [[k.replace('_', ' ').title(), v.get('value')] for k, v in debt_breakdown.items()]
    )

    hotspots = data.get("technical_debt", {}).get("hotspots", [])
    report += "Hotspots\n~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Name", "Type", "Effort (hours)"],
        [[h.get('name'), h.get('type'), h.get('effort')] for h in hotspots]
    )

    # --- Code Quality ---
    report += "Code Quality\n------------\n\n"
    quality_trends = data.get("code_quality", {}).get("trends", {})
    report += "Trends\n~~~~~~\n\n"
    report += _create_rst_table(
        ["Version", "Quality Score (%)"],
        [[k, v] for k, v in quality_trends.items()]
    )
    # Other quality metrics
    report += f"* **Improvement:** {data['code_quality']['improvement']}%\n"
    cc = data['code_quality']['cognitive_complexity']
    report += f"* **Cognitive Complexity:** {cc['current']} (Previous: {cc['previous']}, Change: {cc['change']})\n\n"


    # --- Security Compliance ---
    report += "Security Compliance\n-------------------\n\n"
    sec_standards = data.get("security_compliance", {}).get("standards", {})
    report += "Standards Compliance\n~~~~~~~~~~~~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Standard", "Status"],
        [[k.replace('_', ' ').title(), f"{v['status']} ({v['completion']}%)" if isinstance(v, dict) else v] for k, v in sec_standards.items()]
    )

    vuln_summary = data.get("security_compliance", {}).get("vulnerability_summary", {})
    report += "Vulnerability Summary\n~~~~~~~~~~~~~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Severity", "Count"],
        [[k.title(), v] for k, v in vuln_summary.items()]
    )

    # --- Testing & QA ---
    report += "Testing & QA\n------------\n\n"
    test_coverage = data.get("testing_qa", {}).get("test_coverage", {})
    report += "Test Coverage\n~~~~~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Area", "Coverage (%)"],
        [[k.replace('_', ' ').title(), v] for k, v in test_coverage.items()]
    )

    quality_gates = data.get("testing_qa", {}).get("quality_gates", {})
    report += "Quality Gates\n~~~~~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Gate", "Status"],
        [[k.replace('_', ' ').title(), v] for k, v in quality_gates.items()]
    )

    # --- SonarQube Metrics ---
    report += "SonarQube Metrics\n-----------------\n\n"
    sq_metrics = data.get("sonarqube_metrics", {})
    report += _create_rst_table(
        ["Metric", "Current", "Previous", "Change"],
        [[k.replace('_', ' ').title(), v.get('current'), v.get('previous'), v.get('change')] for k, v in sq_metrics.items()]
    )

    # --- Audit Trail ---
    report += "Audit Trail\n-----------\n\n"
    audits = data.get("audit_trail", {}).get("recent_audits", [])
    report += "Recent Audits\n~~~~~~~~~~~~~\n\n"
    report += _create_rst_table(
        ["Type", "Date", "Status"],
        [[a.get('type'), a.get('date'), a.get('status')] for a in audits]
    )

    action_items = data.get("audit_trail", {}).get("action_items", [])
    report += "Action Items\n~~~~~~~~~~~~\n\n"
    for item in action_items:
        report += f"* {item}\n"
    report += "\n"

    # --- Improvement Goals ---
    report += "Improvement Goals\n-----------------\n\n"
    goals = data.get("improvement_goals", {})
    report += _create_rst_table(
        ["Metric", "Current", "Target", "Owner", "Due Date"],
        [[k.replace('_', ' ').title(), v.get('current'), v.get('target'), v.get('owner'), v.get('due')] for k, v in goals.items()]
    )

    return report

if __name__ == "__main__":
    # Generate Markdown report
    md_report = generate_md_report(dashboard_data)
    with open("report.md", "w") as f:
        f.write(md_report)

    # Generate reStructuredText report
    rst_report = generate_rst_report(dashboard_data)
    with open("docs/report.rst", "w") as f:
        f.write(rst_report)

    print("Dashboard data structure created successfully")
    print(f"Total sections: {len(dashboard_data)}")
    print("Successfully generated report.md and docs/report.rst")